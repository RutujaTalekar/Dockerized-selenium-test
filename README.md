# Dockerized-Selenium-Test
A simple test in selenium python that can run inside a dockerized container

1. Search for selenium-chrome-standalone image on docker hub, and use the official one to pull the image. 
    docker pull selenium/standalone-chrome
2. Once the image is built, use official git seleniumHQ readme to find the command to run docker container with standalone chrome
    docker run -d -p 4444:4444 --shm-size="2g" selenium/standalone-chrome:4.8.0-20230210
    or
    docker run -d -p 4444:4444 --shm-size="2g" selenium/standalone-chrome:latest
3. You can access the standalone chrome on - http://localhost:4444/
4. Create a simple selenium test, run it on command prompt, and check the status on the above link
