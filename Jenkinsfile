pipeline {
	agent any	 
	
	

     environment {
    AWS_CREDENTIALS = credentials('AWS_KEY')
}

stages {
    stage('Deploy') {
        steps {
            withCredentials([string(credentialsId: 'AWS_KEY', variable: 'AWS_CREDENTIALS')]) {
                script {
                    def awsCredentials = AWS_CREDENTIALS.split(':')
                    sh "export AWS_ACCESS_KEY_ID=${awsCredentials[0]}"
                    sh "export AWS_SECRET_ACCESS_KEY=${awsCredentials[1]}"
                    // Now you can use $AWS_ACCESS_KEY_ID and $AWS_SECRET_ACCESS_KEY in your commands
                    sh 'serverless deploy'
                }
            }
        }
    }
}

	
	
	

}
