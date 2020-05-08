pipeline {
  agent { docker { image 'python:3.7.6' } }
  stages {
    stage('build') {
      steps {
        sh 'pip install -r requirements.txt'
      }
    }
    stage('test') {
      steps {
        sh 'python3 test.py > mylog.txt'
      }
      post {
        always {
          junit 'test-results/*.xml'
        }
      }    
    }
  }
}