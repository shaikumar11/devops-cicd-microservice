pipeline {
  agent any
  environment { IMAGE = "devops-backend" }
  stages {
    stage('Test') {
      steps {
        sh '''
          cd backend
          python3 -m venv .venv
          . .venv/bin/activate
          pip install -r requirements-dev.txt
          pytest
        '''
      }
    }
    stage('Build Image') {
      steps { sh 'docker build -t $IMAGE:$BUILD_NUMBER backend' }
    }
  }
}