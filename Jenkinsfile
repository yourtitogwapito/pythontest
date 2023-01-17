pipeline {
    agent { dockerfile true }
    stages {
        stage('Checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: '83b1f9ed-82a6-4e86-bf38-208a8dbae56d', url: 'https://github.com/yourtitogwapito/pythontest.git/']])
                }
            }
        stage('Build') {
            steps {
                sh 'docker build -t omegle_jenkins:$BUILD_NUMBER .'
                sh 'docker container run -it --name omegle_jenkins$BUILD_NUMBER'
                }
            }
    }
}
