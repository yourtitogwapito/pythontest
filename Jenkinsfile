pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: '83b1f9ed-82a6-4e86-bf38-208a8dbae56d', url: 'https://github.com/yourtitogwapito/pythontest.git/']])
            }
        }
        stage('Test') {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: '83b1f9ed-82a6-4e86-bf38-208a8dbae56d', url: 'https://github.com/yourtitogwapito/pythontest.git/']])
            }
        }
        stage('Deploy'){
            agent any
            steps{
            sh label: '', script: '''
touch dockerfile
sudo docker build -t omegle_jenkins:$BUILD_NUMBER .
sudo docker container run -it --name omegle_jenkins$BUILD_NUMBER '''
      }
    }
    }
}
