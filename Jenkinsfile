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
                    export PATH=$PATH:/var/jenkins_home/.local/bin
                    pip install pysonar --break-system-packages
                    python3 /var/jenkins_home/.local/lib/python3.*/site-packages/pysonar/__main__.py \
                      --sonar-host-url=http://172.18.0.3:9000 \
                      --sonar-token=sqa_2487e6f461c73ba6658165f902f6d9ee3b3a9049 \
                      --sonar-project-key=devops-project \
                      --verbose
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
