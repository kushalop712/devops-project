pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                echo 'Pulling code from GitHub...'
                checkout scm
            }
        }

        stage('Security Scan') {
            steps {
                echo 'Running SonarQube security scan...'
                sh '''
                    pip install pysonar --break-system-packages
                    pysonar \
                      --sonar-host-url=http://sonarqube:9000 \
                      --sonar-token=sqp_3fa5f38a254be3250e52d3325dc9136c314e93fc \
                      --sonar-project-key=devops-project
                '''
            }
        }
        
        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                sh 'docker build -t devops-project .'
            }
        }
        
        stage('Run App') {
            steps {
                echo 'Running the container...'
                sh '''
                    docker stop devops-app || true
                    docker rm devops-app || true
                    docker run -d -p 5000:5000 --name devops-app devops-project
                '''
            }
        }
    }
    
    post {
        success {
            echo '✅ Pipeline succeeded!'
        }
        failure {
            echo '❌ Pipeline failed!'
        }
    }
}
