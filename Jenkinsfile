pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: ''
            }
        }

        stage('Build') {
            steps {
                bat '"C:/Users/User/AppData/Local/Programs/Python/Python314/python.exe" -m py_compile app.py'

                echo 'Application build successful.'
            }
        }

        stage('Test') {
            steps {
                bat '"C:/Users/User/AppData/Local/Programs/Python/Python314/python.exe" -m unittest discover -v'
            }
        }

        stage('Generate Report') {
            steps {
                bat '"C:/Users/User/AppData/Local/Programs/Python/Python314/python.exe" generate_report.py'
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
            echo 'Build, Test, Report Generation, Archiving and Deployment completed successfully.'
        }

        failure {
            echo 'Pipeline failed.'
        }
    }
}
