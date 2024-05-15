pipeline {
    agent any	 
    environment {
        AWS_ACCESS_KEY_ID = credentials('AWS_ACCESS_KEY_ID')
        AWS_SECRET_ACCESS_KEY = credentials('AWS_SECRET_ACCESS_KEY')
    }
    stages {
        stage('Deploy') {
            steps {
                sh 'serverless deploy'
                sh 'serverless invoke  --function hell'
            }
        }
    }
}
