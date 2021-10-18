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
		DOCKERHUB_CREDENTIALS=credentials('dockerHub-khCred')
	}
stages{
	stage('Clone The Project'){
		steps{
            git 'https://github.com/khalidsadek/Docker-BitCoinPrice.git'   
			 }
	    }
	    
	//    stage('SET UP THE ENVIROMENT TO USE DOCKER'){// the ref .... https://stackoverflow.com/questions/60583847/aws-ecr-saying-cannot-perform-an-interactive-login-from-a-non-tty-device-after
	// 	steps{// + make this change sudo chmod 666 /var/run/docker.sock from  https://github.com/palantir/gradle-docker/issues/188
    //         sh 'sudo usermod -aG docker $USER'

	//     } 
	//    }

	stage('Build The image') {
      steps {
        sh 'docker build -t khalid-bitcoinapp/docker1 .'
      }
    }
    
   
    stage('Login To Dockerhub') {
      steps {
        sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
      }
    }

 stage('PUSH THE IMAGE') {
      steps {
        sh 'docker push khalid-bitcoinapp/docker1'
      }
    }
 
  }
  post {
    always {
      sh 'docker logout'
    }
  }
}
