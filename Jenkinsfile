pipeline {
  agent { dockerfile true}
  stages {
    stage('build') {
      steps {
        sh 'curl -L localhost:5000'
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
