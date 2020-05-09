pipeline {
  agent { dockerfile true}
  stages {
    stage('build') {
      steps {
        echo 'hello world'
        sh 'echo myCustomEnvVar = $myCustomEnvVar'
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
