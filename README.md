# QA DevOps Core Practical Project: Fortune Teller



## Contents
1. [Brief](#brief)
2. [My Application](#my-application)
3. [Architecture](#architecture)
4. [Project Tracking](#project-tracking)
5. [Risk Assessment](#risk-assessment)
6. [Testing and Bugs](#testing-and-bugs)
7. [Front-End Design](#front-end-design)
8. [Future Improvements](#future-improvements)
9. [Acknowledgements](#acknowledgements)
10. [Author](#author)




## Brief 

The aim of this project was to create a service-orientated architecture for my application. The application was required to be composed of at least 4 services that work together.

* ### Service 1
The core service which renders the Jinja2 templates and is responsible for communicating with the other 3 services as well as persisting some data in an SQL database.

* ### Service 2/3
Services generating a random “Object” such as random number, randor letter etc. 

* ### Service 4
Service creating an “Object” based on the results of services 2 and 3 using a set of pre-defined rules.
Please see below for an example of how this logic can look.

## My project

For this project, I have decided to produce a basic 'fortune teller' application. More specifically, this application is inspired by Omikuji, a type of Japanese fortune-telling. Based on the results from services 2 and 3, service 4 will determine the user's luck:

(大吉): great blessing
(吉) blessing
(半吉): half-blessing
(凶): curse
(大凶): great curse

## Architecture

## Project tracking

Here you can view my trello board: https://trello.com/b/ruKaSkGE/qaproject2


## Risk Assessment


## Testing and bugs 


## Front-End Design


## Future improvements

## Acknowledgements

## Author 

Produced by Pawel Stypulkowski

pstyp94@gmail.com
