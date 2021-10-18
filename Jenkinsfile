// pipeline{

// 	agent { label 'slave' }

// 	environment {
// 		DOCKERHUB_CREDENTIALS=credentials('dockerHub-khCred')
// 	}

// 	stages {

//     stage('Cloning Git') {
//       steps {
//           git 'https://github.com/khalidsadek/Docker-BitCoinPrice.git'
//       }
//     }

// 		stage('Build') {

// 			steps {
// 				sh 'docker build -t khalid-bitcoinapp:latest .'
// 			}
// 		}

// 		stage('Login') {

// 			steps {
// 				sh 'sudo usermod -aG docker $USER'
// 				sh 'echo $DOCKERHUB_CREDENTIALS_PSW | sudo docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
// 			}
// 		}

// 		stage('Push') {

// 			steps {
// 				sh 'docker push khalid-bitcoinapp:latest'
// 			}
// 		}
// 	}

// 	post {
// 		always {
// 			sh 'docker logout'
// 		}
// 	}

// }





pipeline
{

agent {label 'slave'};
environment {
		DOCKERHUB_CREDENTIALS=credentials('dockerhub-cred5')
	}
stages{
	stage('Git Clone'){
		steps{
            git 'https://github.com/khalidsadek/Docker-BitCoinPrice.git'   
			 }
	    }
	    

	stage('Build Image') {
      steps {
        sh 'docker build -t khalidsadek/bitcoin .'
      }
    }
    
   
    stage('Login To Dockerhub') {
      steps {
        sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
      }
    }

 stage('Push Image') {
      steps {
        sh 'docker push khalidsadek/bitcoin'
      }
    }
 
  }
  post {
    always {
      sh 'docker logout'
    }
  }
}
