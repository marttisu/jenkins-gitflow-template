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
      }
    }
    stage('Deploy') {
      parallel {
        stage('Deploy to dev') {
          agent {
            label 'dev'
          }
          steps {
            sh './deployment/deploy.py dev'
          }
        }
        stage('Deploy to tst') {
          agent {
            label 'ts'
          }
          steps {
            sh './deployment/deploy.py tst'
          }
        }
        stage('Deploy to qa') {
          agent {
            label 'qa'
          }
          steps {
            sh './deployment/deploy.py qa'
          }
        }
      }
    }
    stage('UAT') {
      steps {
        input 'Deploy to Production (prd)?'
      }
    }
    stage('Release') {
      steps {
        sh './deployment/deploy.py prd'
      }
    }
  }
}
