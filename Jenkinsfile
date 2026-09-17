pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/saquib-18/jenkins-project-2.git'
            }
        }

        stage('Build') {
            steps {
                bat 'python -m py_compile app.py'
                echo 'Application build successful.'
            }
        }

        stage('Test') {
            steps {
                bat 'python -m unittest test_app.py -v'
            }
        }

        stage('Generate Report') {
            steps {
                bat 'python generate_report.py'
            }
        }

        stage('Archive Report') {
            steps {
                archiveArtifacts artifacts: 'report.txt',
                                  fingerprint: true
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application...'
                echo 'Deployment completed successfully.'
            }
        }
    }

    post {
        success {
            echo 'Build, Test, Archive and Deployment completed successfully.'
        }

        failure {
            echo 'Pipeline failed.'
        }
    }
}
