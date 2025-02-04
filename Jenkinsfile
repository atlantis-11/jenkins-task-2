pipeline {
    agent any
    
    environment {
        IMAGE_TAG = "atlantisj11/weather_app:${BUILD_ID}"
    }

    stages {
        stage("Test") {
            steps {
                script {
                    docker.build("${IMAGE_TAG}-tests", '--target=tests .')
                }
            }
        }
        stage("Build") {
            steps {
                script {
                    def image = docker.build(IMAGE_TAG)
                    
                    docker.withRegistry('', 'atlantisj11-dockerhub') {
                        image.push()
                    }
                }
            }
        }
        stage('Deploy') {
            steps {
                withCredentials([file(credentialsId: 'kubeconfig-9', variable: 'KUBECONFIG')]) {
                    sh """
                    cd manifests
                    kustomize edit set image weather_app=${IMAGE_TAG}
                    kubectl apply -k .
                    """
                }
            }
        }
    }
}
