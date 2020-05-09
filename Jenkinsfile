pipeline {
  agent {
    dockerfile {
      filename "Dockerfile"
      args '-i --entrypoint='
               }
        }  
  stages {
    stage('build') {
      steps {
        echo 'hello world'
      }
    }
    stage('test') {
      steps {
        sh 'python3 test.py'
      }
      post {
        always {
          junit 'test-results/*.xml'
        }
      }    
    }
    stage('InitialDeployment') {
       def dockerHome = tool 'myDocker'
       env.PATH = "${dockerHome}/bin:${env.PATH}"
    }
    stage('Deploy') {
      when {
        expression {
          currentBuild.result == null || currentBuild.result == 'SUCCESS' 
        }
      }
      steps {
        sh 'docker rm flaskapp'
        sh 'docker build -t flaskimage .'
        sh 'docker run -p 5000:5000 flaskimage --name flaskapp'
      }
  }
 }
}
