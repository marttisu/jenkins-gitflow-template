pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh './deployment/build.py'
      }
    }
    stage('Test') {
      steps {
        sh './deployment/test.py'
        sh './deployment/deploy.py dev'
        sh './deployment/deploy.py tst'
        sh './deployment/deploy.py qa'
      }
    }
    stage('Release') {
      steps {
        sh './deployment/deploy.py prd'
      }
    }
  }
}