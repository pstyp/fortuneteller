pipeline {
    agent any 
    stages {
       stage('Add the executable permission'){
            steps {
               sh 'chmod 755 ./jenkins_scripts/*'
       }
        }
        stage('Test'){ 
            steps {
               sh './jenkins_scripts/pytest.sh'
                  
            }
        }
        stage('Ansible') { 
            steps {
              sh './jenkins_scripts/ansible.sh'
            }
        }
        stage('Deploy') { 
            steps {
              sh './jenkins_scripts/deploy.sh'   
            }
        }
    }
}
