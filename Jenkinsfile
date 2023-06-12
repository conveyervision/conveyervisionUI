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
        stage('Build and push Docker images') {
            steps {
                script {
                    sh 'docker buildx create --use'
                    sh "docker buildx build --push --platform linux/amd64 --tag ${registry}/${imageName}-amd64:${tag} ."
                    sh "docker buildx build --push --platform linux/arm64 --tag ${registry}/${imageName}-arm64:${tag} ."
                }
            }
        }
        stage('Deploy to Server') {
            steps {
                // Clone the cv-dockercompose repository
                git branch: 'main', 
                    credentialsId: 'cv-jks-deploy', // You'll need to set up Git credentials in Jenkins
                    url: 'https://github.com/conveyervision/cv-dockercompose.git'
                
                // Run Docker Compose
                sh 'docker-compose down' // Get rid of currently running containers
                sh 'docker-compose pull' // Pulls the latest images
                sh 'docker-compose up -d' // Runs the Docker Compose services in detached mode
            }
        }
    }
}

