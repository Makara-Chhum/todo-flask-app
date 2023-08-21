pipeline {
    agent {label 'dockeragent'}
    stages {
        stage ("Clone code") {
            steps {
                git branch: 'jenkinstry', changelog: false, url: 'https://github.com/kunal-gohrani/todo-flask-app.git'
            }
        }
        
        stage ("Build Image") {
            steps {
                sh 'docker build . -t todo-cicd'
                withCredentials([usernamePassword(credentialsId: 'dockerhub', passwordVariable: 'password', usernameVariable: 'username')]) {
                    sh "docker login -u ${env.username} -p ${env.password}"
                    sh "docker tag todo-cicd ${env.username}/todo-cicd:latest"
                    sh "docker push ${env.username}/todo-cicd:latest"
                }
            }
        } 
        
        stage ("Start Container") {
            steps {
                sh 'docker compose down'
                sh 'docker compose up -d'
            }
        }
    }
}
