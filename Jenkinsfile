pipeline {
    agent any
    environment {
        registry = 'docker.gensosekai.com'
        registryCredential = 'dockerHubCredentialID' // This is the ID of the credentials you set up in Jenkins
        imageName = 'cv'
        tag = 'jenkins-latest'
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm // This checks out the code from your repository
            }
        }
        stage('Build and push Docker image') {
            steps {
                script {
                    def dockerImage = docker.build("${registry}/${imageName}:${tag}")
                    docker.withRegistry("https://${registry}", "${registryCredential}") {
                        dockerImage.push("${tag}")
                    }
                }
            }
        }
    }
}

