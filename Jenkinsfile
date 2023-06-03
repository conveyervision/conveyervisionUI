pipeline {
    agent any
    environment {
        registry = 'docker.gensosekai.com'
        registryCredential = 'dockerHubCredentialID'
        imageName = 'cv'
        tag = 'latest'
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm // This checks out the code from your repository
            }
        }
        stage('Setup buildx') {
            steps {
                script {
                    sh 'docker buildx create --use'
                }
            }
        }
        stage('Build and push Docker image') {
            steps {
                script {
                    sh """
                    docker buildx build --platform linux/amd64,linux/arm64 -t ${registry}/${imageName}:${tag} --push .
                    """
                }
            }
        }
    }
}

