pipeline {
    agent {
        label 'docker'
    }
    stages {
        stage('Build') {
            steps {
                echo 'Building stage!'
                sh 'make build'
            }
        }
        stage('Unit tests') {
            steps {
                sh 'make test-unit'
                // Archivar y publicar el informe JUnit para las pruebas unitarias
                archiveArtifacts artifacts: 'results/unit_result.xml'
                junit 'results/unit_result.xml'
                // Archivar el archivo de cobertura y la carpeta de cobertura
                archiveArtifacts artifacts: 'results/coverage.xml'
                archiveArtifacts artifacts: 'results/coverage/**'
            }
        }
        stage('API tests') {
            steps {
                sh 'make test-api'
                // Archivar y publicar el informe JUnit para las pruebas de API
                archiveArtifacts artifacts: 'results/api_result.xml'
                junit 'results/api_result.xml'
            }
        }
        stage('e2e tests') {
            steps {
                sh 'make test-e2e'
                // Archivar y publicar el informe JUnit para las pruebas e2e
                archiveArtifacts artifacts: 'results/cypress_result.xml'
                junit 'results/cypress_result.xml'
            }
        }  
    }
    post {
        always {
            cleanWs()
        }
        failure {
            script {
                def fullDisplayName = currentBuild.fullDisplayName
                def buildNumber = env.BUILD_NUMBER
                def buildUrl = env.BUILD_URL

                echo "Pipeline failed: ${fullDisplayName}"
                echo "Build number: ${buildNumber}"
                echo "Now the following email would be sent:"
                echo """
                mail to: 'mi@correo.com',
                     subject: "Pipeline failed: ${fullDisplayName} (Build #${buildNumber})",
                     body: "Something is wrong with ${buildUrl}"
                """
            }
        }
    }
}
