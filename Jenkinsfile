pipeline {
    agent any
    stages {
        stage('testing') {
            steps {
                sh "bash test.sh"
            }
        }
        stage('building') {
            steps {

            }
        }
        stage('deploying') {
            steps {

            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: "htmlcov/*"
        }
    }
}