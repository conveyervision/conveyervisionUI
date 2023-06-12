pipeline {
    agent { label 'cv' }
    environment {
        registry = 'docker.gensosekai.com'
        registryCredential = 'dockerHubCredentialID' // This is the ID of the credentials you set up in Jenkins
        imageName = 'cv'
        tag = 'jenkins'
        deploymentDir = '/home/saad/git/bytevision/cv-deploymain'
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
                    def dockerImage = docker.build("${registry}/${imageName}:${tag}", ".")
                    docker.withRegistry("https://${registry}", "${registryCredential}") {
                        dockerImage.push("${tag}")
                    }
                }
            }
        }
        stage('Deploy to Server') {
            steps {
                // Clone the cv-dockercompose repository
                git branch: 'main', 
                    credentialsId: 'cv-jks-deploy', // You'll need to set up Git credentials in Jenkins
                    url: 'https://github.com/conveyervision/cv-dockercompose.git'
                
                // Move the cloned repository to the desired directory
                sh "mv cv-dockercompose/* ${deploymentDir}"
                
                // Run Docker Compose
                dir("${deploymentDir}") {
                    sh 'docker-compose down' // Get rid of currently running containers
                    sh 'docker-compose pull' // Pulls the latest images
                    sh 'docker-compose up -d' // Runs the Docker Compose services in detached mode
                }
            }
        }
    }
}

