pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/yourusername/my-s3-csv-processor.git'
            }
        }
        stage('Build') {
            steps {
                sh 'npm install -g serverless'
                sh 'serverless deploy' # Or any other command to build/deploy your service
            }
        }
    }
}
