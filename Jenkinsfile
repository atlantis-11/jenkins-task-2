@Library('my-shared-lib') _

pipeline {
    agent any

    stages {
        stage('Install dependencies') {
            steps {
                sh 'python3 -m venv .venv'
                sh '''
                . .venv/bin/activate
                pip install .
                pip install pytest
                '''
            }
        }
        stage('Parallel Tests') {
            parallel {
                stage('Unit Tests') {
                    steps {
                        runTests 'tests/unit'
                    }
                }
                stage('Integration Tests') {
                    steps {
                        runTests 'tests/integration'
                    }
                }
            }
        }
    }
    
    post {
        always {
            withCredentials([string(credentialsId: 'discord_secret', variable: 'discord_webhook')]) {
                discordSend(
                    title: env.JOB_NAME,
                    link: env.BUILD_URL,
                    description: "${env.JOB_NAME} build result: ${currentBuild.currentResult}",
                    result: currentBuild.currentResult,
                    webhookURL: discord_webhook
                )
            }
        }
        cleanup {
            deleteDir()
        }
    }
}
