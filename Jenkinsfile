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
                      --sonar-host-url=http://172.17.0.3:9000 \
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
