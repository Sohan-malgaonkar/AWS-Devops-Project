pipeline {
    agent any

    stages {
        stage('Clone Code') {
            steps {
                git 'https://github.com/Sohan-malgaonkar/AWS-Devops-Project'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask-ci-cd-app .'
            }
        }

        stage('Run Docker Container') {
            steps {
                sh '''
                    docker stop flask-app || true
                    docker rm flask-app || true
                    docker run -d -p 5000:5000 --name flask-app flask-ci-cd-app
                '''
            }
        }
    }
}
