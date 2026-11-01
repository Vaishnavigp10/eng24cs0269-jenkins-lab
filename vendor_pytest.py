        stage('Docker image') {
            steps {
                sh 'python3 vendor_pytest.py'
                sh 'docker build -t ${APP_NAME}:${BUILD_NUMBER} .'
                sh 'docker run --rm ${APP_NAME}:${BUILD_NUMBER}'
                sh 'docker images ${APP_NAME}'
            }
        }
