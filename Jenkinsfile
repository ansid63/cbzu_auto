pipeline {
  stages {
    stage("Build image") {
      steps {
        catchError {
          checkout scm
          docker.build("python-web-tests:1.0", ".")
          }
      }
    }
    stage('Pull browser') {
      steps {
        catchError {
          checkout scm
          docker.image('selenoid/chrome:92.0').pull()
        }
      }
    }

    stage('Run tests') {
      steps {
        catchError {
          script {
              docker.image('aerokube/selenoid:1.10.4').withRun('-p 4444:4444 -v /run/docker.sock:/var/run/docker.sock -v $PWD:/etc/selenoid/',
                '-service-startup-timeout 120s -session-attempt-timeout 120s -session-delete-timeout 120s -timeout 600s -limit 4') { c ->
                  docker.image('python-web-tests:1.0'){
                    withEnv(["PYTHON_HOME=${DOCKER_PYTHON_HOME}"]) {
                        sh "pytest -n 2 --reruns 1 ${CMD_PARAMS}"
                    }
                  }
               }
            }
          }
        }
    }

  }
}
