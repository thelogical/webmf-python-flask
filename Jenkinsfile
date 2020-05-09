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
    stage('Deploy') {
      when {
        expression {
          currentBuild.result == null || currentBuild.result == 'SUCCESS' 
        }
      }
      steps {
        sh 'sudo docker rm flaskapp'
        sh 'sudo docker build -t flaskimage .'
        sh 'sudo docker run -p 5000:5000 flaskimage --name flaskapp'
      }
  }
 }
}
