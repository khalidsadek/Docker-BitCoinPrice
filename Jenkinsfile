pipeline{

	agent { label 'slave' }

	environment {
		DOCKERHUB_CREDENTIALS=credentials('dockerHub-khCred')
	}

	stages {

    stage('Cloning Git') {
      steps {
          git 'https://github.com/khalidsadek/Docker-BitCoinPrice.git'
      }
    }

		stage('Build') {

			steps {
				sh 'docker build -t khalid-bitcoinapp:latest .'
			}
		}

		stage('Login') {

			steps {
				sh 'sudo usermod -aG docker $USER'
				sh 'echo $DOCKERHUB_CREDENTIALS_PSW | sudo docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
			}
		}

		stage('Push') {

			steps {
				sh 'docker push khalid-bitcoinapp:latest'
			}
		}
	}

	post {
		always {
			sh 'docker logout'
		}
	}

}







// pipeline {
//   environment {
//     registry = "khalidsadek/bitcoin-image"
//     registryCredential = '4713c7db-0c71-44a5-a233-695f49fc1469'
//     dockerImage = ''
//   }
//   agent any
//   stages {
//     stage('Cloning Git') {
//       steps {
//           git 'https://github.com/khalidsadek/Docker-BitCoinPrice.git'
//       }
//     }

//      stage('SET UP THE ENVIROMENT'){// the ref .... https://stackoverflow.com/questions/60583847/aws-ecr-saying-cannot-perform-an-interactive-login-from-a-non-tty-device-after
// 		steps{// + make this change sudo chmod 666 /var/run/docker.sock from  https://github.com/palantir/gradle-docker/issues/188
//             sh 'sudo usermod -aG docker $USER'

// 	    } 
// 	   }
//     stage('Building image') {
//       steps{
//         sh 'sudo usermod -aG docker $USER'
//         script {
//           dockerImage = docker.build registry + ":$BUILD_NUMBER"
//         }
//       }
//     }
//     stage('Deploy Image') {
//       steps{
//         script {
//           docker.withRegistry( '', registryCredential ) {
//             dockerImage.push()
//           }
//         }
//       }
//     }
//     stage('Remove Unused docker image') {
//       steps{
//         sh "docker rmi $registry:$BUILD_NUMBER"
//       }
//     }
//   }
// }
