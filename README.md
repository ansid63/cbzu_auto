**cbzu_auto**

Autotests for launching in Selenoid Chrome browser based on Docker image in Jenkins environment.

Dockerfile create image for tests launching, Jenkinsfile create environment for launching tests.
Additional modules xdist and rerunfailures launch tests in 4 threads with 1 rerun on failure. 
