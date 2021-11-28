pipeline {
  agent any
  stages {
    stage("Build image") {
      steps {
        catchError {
          script {
            docker.build("python-web-tests", "-f Dockerfile .")
          }
         }
      }
    }
    stage('Pull browser') {
      steps {
        catchError {
          script {
          docker.image('selenoid/chrome:92.0')
          }
        }
      }
    }

    stage('Run tests') {
      steps {
        catchError {
          script {
              docker.image('aerokube/selenoid:1.10.4').withRun('-p 4444:4444 -v /run/docker.sock:/var/run/docker.sock -v $PWD:/etc/selenoid/',
                '-service-startup-timeout 120s -session-attempt-timeout 120s -session-delete-timeout 120s -timeout 600s -limit 4') { c ->
                  docker.image('python-web-tests').inside("--link ${c.id}:selenoid") {
                        sh "pytest -n 2 --reruns 1 ${CMD_PARAMS}"
                    }
               }
            }
          }
        }
    }

  }
}
