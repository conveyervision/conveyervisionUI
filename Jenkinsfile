pipeline {
    agent { label 'cv' }
    environment {
        registry = 'docker.gensosekai.com'
        registryCredential = 'dockerHubCredentialID' // This is the ID of the credentials you set up in Jenkins
        imageName = 'cv'
        tag = 'latest'
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm // This checks out the code from your repository
            }
        }
        stage('Setup Docker Buildx') {
            steps {
                script {
                    sh 'docker buildx create --use'
                }
            }
        }
        stage('Build Docker Image - AMD64') {
            steps {
                script {
                    sh "docker buildx build --platform linux/amd64 --tag ${registry}/${imageName}-amd64:${tag} . --load"
                }
            }
        }
        stage('Push Docker Image - AMD64') {
            steps {
                script {
                    sh "docker push ${registry}/${imageName}-amd64:${tag}"
                }
            }
        }
        stage('Build Docker Image - ARM64') {
            steps {
                script {
                    sh "docker buildx build --platform linux/arm64 --tag ${registry}/${imageName}-arm64:${tag} . --load"
                }
            }
        }
        stage('Push Docker Image - ARM64') {
            steps {
                script {
                    sh "docker push ${registry}/${imageName}-arm64:${tag}"
                }
            }
        }
        stage('Clone Deployment Repo') {
            steps {
                git branch: 'main',
                    credentialsId: 'cv-jks-deploy', // You'll need to set up Git credentials in Jenkins
                    url: 'https://github.com/conveyervision/cv-dockercompose.git'
            }
        }
        stage('Start Deployment') {
            steps {
                sh 'docker-compose down' // Get rid of currently running containers
                sh 'docker-compose pull' // Pulls the latest images
                sh 'docker-compose up -d' // Runs the Docker Compose services in detached mode
            }
        }
    }
}

