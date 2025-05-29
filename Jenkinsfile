pipeline {
    agent any

    environment {
        IMAGE_NAME = "flask-todo-game"
        CONTAINER_NAME = "todo-container"
    }

    stages {
        stage('Build') {
            steps {
                echo '🔨 Building Docker image...'
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Test') {
            steps {
                echo '🧪 Running unit tests...'
                sh '''
                pip install pytest
                PYTHONPATH=$PYTHONPATH:. pytest tests/
                '''
            }
        }

        stage('Code Quality') {
            steps {
                echo '🧹 Running Pylint...'
                sh '''
                pip install pylint
                pylint app.py || true
                '''
            }
        }

        stage('Security Scan') {
            steps {
                echo '🔒 Running Bandit scan...'
                sh '''
                pip install bandit
                bandit -r . || true
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo '🚀 Deploying Docker container...'
                sh '''
                docker stop $CONTAINER_NAME || true
                docker rm $CONTAINER_NAME || true
                docker run -d -p 15000:5050 --name $CONTAINER_NAME $IMAGE_NAME
                '''
            }
        }
    }

    post {
        always {
            echo 'Pipeline execution complete.'
        }
    }
}

