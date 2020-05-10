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
      steps {
        sh 'echo $PATH'
        sh 'whoami'
      }
    }
 }
}
