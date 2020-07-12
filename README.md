# QA DevOps Core Practical Project: Fortune Teller



## Contents
1. [Brief](#brief)
2. [My Application](#my-application)
3. [Second Implementation](#second-implementation)
4. [Architecture](#architecture)
5. [Project Tracking](#project-tracking)
6. [Risk Assessment](#risk-assessment)
7. [Testing and Bugs](#testing-and-bugs)
8. [Front-End Design](#front-end-design)
9. [Future Improvements](#future-improvements)
10. [Acknowledgements](#acknowledgements)
11. [Author](#author)




## Brief 

The aim of this project was to create a service-orientated architecture for my application. The application was required to be composed of at least 4 services that work together.

* ### Service 1
The core service which renders the Jinja2 templates and is responsible for communicating with the other 3 services as well as persisting some data in an SQL database.

* ### Service 2/3
Services generating a random “Object” such as random number, random letter etc. 

* ### Service 4
Service creating an “Object” based on the results of services 2 and 3 using a set of pre-defined rules.
Please see below for an example of how this logic can look.

## My Application

For this project, I have decided to produce a basic 'fortune teller' application. More specifically, this application is inspired by Omikuji, a type of Japanese fortune-telling. In short, Omikuji are fortune-telling paper strips that can be found at shrines and temples throughout Japan. 

Service 2 and 3 generate random letters (A or B and X and Y respectively). Based on the results from services 2 and 3, service 4 will determine the user's luck and add it to my SQL database. Specifically, it adds the letter generated by service 2 and the letter generated by service 3 creating a 'code' (AX, AY, BX or BY). The codes are assigned to different results (see below). Service 1 gets a response from service 4 and queries the database in order to display the results on the homepage. Services are located on different ports. 

Possible results:

* (大吉): great blessing (indicates that the user will be very lucky)
* (吉) blessing (indicates that the user will be somewhat lucky)
* (凶): curse (indicates that the user will be rather unlucky)
* (大凶): great curse (indicates that the user will be extremely unlucky)

## Second implementation

As part of my presentation, I am required to make a push to my GitHub repository and demonstrate that Jenkins will rebuild my application with minimal downtime. I made slight changes to all services. For service 1, I changed the background. Service 2 can generate letters A, B and C in this implemenation. Service 3 can generate letters X, Y, Z. I also slightly changed the output of service 4. As there are far more code options in this implementation, the user is far more likely to get '(大凶): great curse' as their fortune. In other words, the aim of this implemetation is to drastically decrease the chance of receiving other results. 

## Architecture

* Database

For this project I created a database with only one table. As such, there was no entity relationship. To create my database, I used a MYSQL container. Additionally, I created another database for my tests. This database is stored on Google Cloud Platform. The reason why I decided to do this is because I believed it would make testing my application easier as I would not have to run a container. 

![table](https://github.com/pstyp/images/blob/master/table.png)

* CI Pipepline

Here you can see my initial CI pipeline as envisioned when I started working on this project:

![cipipeline](https://github.com/pstyp/images/blob/master/CI%20pipeline%20PROJECT2.png)

This pipeline has evolved a lot and this is the final result:

![ci2](https://github.com/pstyp/images/blob/master/CI%20pipeline%20PROJECT2%20v2.png) 

My application is stored on a Virtual Machine (Ubuntu) managed by Google Cloud Platform. This Virtual Machine is also my Docker swarm manager. Additionally, I have two worker Virtual Machines. My CI server is also stored on a seperate Virutal Machine.

For this application, I used Python as my source code with Flask as my micro-framework. I used Git as my version control system and GitHub as my remote repository. I also used Jenkins as my CI server. Pytest was used for unit testing and a Trello board for project tracking. My Docker images are stored on DockerHub which is my artifact repository. 

My continuous integration pipeline allows for a very efficient development-to-deployment cycle. Whenever I make a commit to my GitHub repository, GitHub sends a request to my Jenkins build server via web hook. Jenkins then automotically runs my pipeline using my Jenkinsfile and Jenkins scripts. As Jenkins stores all my variables, I do not need to export them manually. Jenkins first tests my application using pytest (after adding more permissions to the script). Then, it uses Ansible to install docker and connect my swarm manager to my workers (see my playbook and roles for details). Jenkins then builds new Docker images using docker-compose and pushes them to DockerHub. Finally, Docker stack deploy uses my images to create new containers. Nginx (stored on a separate VM) acts as a reverse-proxy and load balancer. The application should be accessible on port 80.

![jenkins](https://github.com/pstyp/images/blob/master/jenkins_finished.png)

Not only does Jenkins automate the deployment process, it also allows you to view the logs of your previous builds. They can be extremely useful as they allow you to see what exactly went wrong and when. This helps you fix all the problems with your build. 

![console](https://github.com/pstyp/images/blob/master/jenkins_console_output.png) 

![logs](https://github.com/pstyp/images/blob/master/jenkins_job.png)

## Project tracking

![kanban2](https://github.com/pstyp/images/blob/master/kanban2.png)


I used a Trello board for project tracking. I created several user stories that relate to features that I wanted like to include in my application. Although I initially planned to divide them into two categories - 'must-have' features (green) and 'could-have' features (yellow), I then changed my mind and decided that all of them are necessary. I managed to implement all the features I wanted to in some capacity as my application was not very complex. 


Here you can view my trello board: https://trello.com/b/ruKaSkGE/qaproject2


## Risk Assessment

![risk](https://github.com/pstyp/images/blob/master/risk_ass2.png)

As part of the project, I conducted a comprehensive risk assessment. I tried to include all risks I thought would be significant. Nevertheless, it is possible I forgot to include some risks. At the end of the project I revisited my risk assessment. 

You can view me risk assessment here: https://docs.google.com/spreadsheets/d/1hV65p2aIRSzcAKAiYkczFPUz5rHyst5qW958FkKglDg/edit?usp=sharing

## Testing and bugs 

As I mentioned earlier, I used pytest to test the application. I tested all four services of my application. My unit test coverage was a hundred per cent for all of them. All tests passed successfully. In order to test my responses, I had to use requests_mock and patch modules to mock them. This is because service 4 and service 1 are dependant on other services. Although I could add more tests, I believe that for the purpose of this project, my unit tests should be sufficient as they tested databases, responses and all functionality. Given more time, I would try to add further tests.

![serv1](https://github.com/pstyp/images/blob/master/service1_test.png)
![serv2](https://github.com/pstyp/images/blob/master/service2_test.png)
![serv3](https://github.com/pstyp/images/blob/master/service3_test.png)
![serv4](https://github.com/pstyp/images/blob/master/service4_test.png)

Aside from unit tests, I also added an integration test. This test also passed successfully when I ran it manually. Unfortunately, this test did not work when it was run by Jenkins. This is because I needed all the services to be running in order to run this test which was not possible because of the way in which my pipeline job was structured. This test can still be seen on the development branch of this project and in my test result report. Given more time, I would attempt to make it work with Jenkins.  

![int](https://github.com/pstyp/images/blob/master/service1_int.png)

Despite my efforts, I have not been able to find any major bugs, which does not necessarily there are not any. The only error I noticed occurs when I leave the application on for a long time. It is a so-called 'OperationalError' which disappears if I refresh the application. However, it is important to mention that my application was rather simplistic which means that there are not many opportunities for bugs. Given more time, I would spend more time looking for any potential bugs.

## Front-End Design

Front-end design was not the focus of this project. However, to make my application slightly more aesthetically pleasing, I added a simple background and a photo. 


![frontend](https://github.com/pstyp/images/blob/master/frontend2.png)

## Future improvements

 As my time for this project was extremely limited, there are a number of improvements I would like to make. Here is a list of a few improvements I would like to make:
 
 * I would add more web pages (e.g. an about page and a page with previous fortune results).
 * I would try to improve my front-end design. 
 * Japanese omikuji has actually far more than four results (e.g. 'small curse', 'middle curse', 'future curse'). I would like to implement all of them.
 * I would like to make my integration test work with Jenkins.
 * I would like to add full CRUD (Create, Read, Update, Delete) functionality (e.g. deleting previous fortune results). 
 * I think it would be beneficial if users were able to register and save their results.
 * I think different fortunes should have more detailed descriptions. 
 
 This list is not exhaustive and there are many other improvements I could make. 
 

## Acknowledgements

I would like to thank my trainers for their guidance and invaluable help throughout the project.

## Author 

Produced by Pawel Stypulkowski

pstyp94@gmail.com
