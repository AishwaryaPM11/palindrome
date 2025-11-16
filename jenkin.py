pipeline {
  agent any

  triggers {
    cron('*/3 * * * *')  
  }

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Run Script') {
      steps {
        sh 'python3 palindrome.py "A man a plan a canal Panama"'
      }
    }
  }
}