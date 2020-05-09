pipeline {
  agent { dockerfile true 
          args  "--entrypoint='' "
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
  }
}
