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
                    /opt/sonar-scanner/bin/sonar-scanner \
                      -Dsonar.projectKey=devops-project \
                      -Dsonar.sources=. \
                      -Dsonar.host.url=http://172.18.0.3:9000 \
                      -Dsonar.token=sqa_2487e6f461c73ba6658165f902f6d9ee3b3a9049
                '''
            }
        }
        
        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                sh 'docker build -t devops-project .'
            }
        }

        stage('Deploy with Ansible') {
            steps {
                echo 'Deploying with Ansible...'
                sh '''
                    export PATH=$PATH:/var/jenkins_home/.local/bin
                    pip install ansible --break-system-packages
                    python3 -m ansible playbook -i localhost, deploy.yml
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
