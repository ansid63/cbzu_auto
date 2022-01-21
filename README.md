##Project for experiments with environment

>Autotests launching in separated Selenoid Chrome browsers based on Docker image in Jenkins environment.

>Dockerfile create image for tests launching, Jenkinsfile create environment for launching tests.

>Additional modules xdist and rerunfailures launch tests in 4 threads with 1 rerun on failure. 

> Allure create reports for running tests

> Added Selenoid UI to pipeline, now you can look at your tests in browser 

Selenoid useful for launching browsers independently, full information you could find in [documentation](https://aerokube.com/selenoid/latest/)