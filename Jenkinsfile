pipeline {
    agent {
        label 'docker' // Usa el agente 'docker' definido en Jekins
    }
    stages {
        stage('Build') {
            steps {
                echo 'Building stage!' // Mensaje indicando el inicio de la etapa de construcción
                sh 'make build' // Ejecutar el comando de construcción
            }
        }
        stage('Unit tests') {
            steps {
                sh 'make test-unit' // Ejecutar las pruebas unitarias
                // Archivar y publicar el informe JUnit para las pruebas unitarias
                archiveArtifacts artifacts: 'results/unit_result.xml'
                junit 'results/unit_result.xml'
                // Archivar el archivo de cobertura y la carpeta de cobertura
                //archiveArtifacts artifacts: 'results/coverage.xml'
                //archiveArtifacts artifacts: 'results/coverage/**'
                recordCoverage(tools: [[parser: 'JUNIT']], id: 'junit', pattern: 'results/coverage.xml', sourceCodeRetention: 'EVERY_BUILD')
            }
        }
        stage('API tests') {
            steps {
                sh 'make test-api' // Ejecutar las pruebas de API
                // Archivar y publicar el informe JUnit para las pruebas de API
                archiveArtifacts artifacts: 'results/api_result.xml'
                junit 'results/api_result.xml'
            }
        }
        stage('e2e tests') {
            steps {
                sh 'make test-e2e' // Ejecutar las pruebas end-to-end (e2e)
                // Archivar y publicar el informe JUnit para las pruebas e2e
                archiveArtifacts artifacts: 'results/cypress_result.xml'
                junit 'results/cypress_result.xml'
            }
        }  
    }
    post {
        always {
            cleanWs() // Limpiar el espacio de trabajo después de cada ejecución
        }
        failure {
            script {
                def fullDisplayName = currentBuild.fullDisplayName // Obtener el nombre completo de la compilación
                def buildNumber = env.BUILD_NUMBER // Obtener el número de compilación
                def buildUrl = env.BUILD_URL // Obtener la URL de la compilación

                // Mostrar mensajes de error y detalles de la compilación fallida
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
