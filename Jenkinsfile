pipeline {
    agent any
    
    environment {
        AWS_DEFAULT_REGION = 'us-east-1'
	 	AWS_ACCESS_KEY_ID = credentials('AWS_ACCESS_KEY_ID')
		AWS_SECRET_ACCESS_KEY = credentials('AWS_SECRET_ACCESS_KEY')
	 }
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Serverless Framework') {
            steps {
                script {
                    sh 'npm install -g serverless'
                }
            }
        }

        stage('Deploy Serverless Application') {
            steps {
                script {
                    sh 'serverless deploy --stage production'
                }
            }
        }
    }

    post {
        success {
            echo 'Deployment succeeded!'
        }
        failure {
            echo 'Deployment failed.'
        }
    }
}
