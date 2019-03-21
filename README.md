# UAT
> User's happy path performed automatically ! 

## Description

This is a test suite written in python, it tests the search functionality of autohero.com's search page, as a sample of UAT.
This application uses: 

- **Unittest**,  a python framework useful to organize the test's code 
- **Selenium webdriver** with python bindings that provides an instance of the Chrome browser and some useful methods to interact with it 
- Some external python's libraries

The application use a docker compose to connect to Remote WebDrivers (Chrome and Firefox).

## How to run test suite

Clone the repository and install the requirements using pip:

```
$ pip3 install -r requirements.txt
```

You need to up docker compose's services, through this:

```
$ docker-compose -f docker-compose.yaml up 
```
replace `down` with `up` if you want to remove the containers.

At this point you can run test's application performing this command inside the app's directory:

```
$ python3 main.py 
```


Some parameters are available to run the test, type `--help` for more details, here is a short list of parameters: 
- browser
- viewport
- test file
- html report


A docker image is available to run test into a container without installing packages, (a local option has to be implemented).
First build the image:
```
$ docker build . -t ${container_name}
```
Then run the container:
```
$ docker run -v $(pwd):/var/www/uat -ti ${container_name} /bin/bash
```
Now you are ready to run tests as described above.


### Requirments
- python 3.7
- pip
- Docker 

### Sources

- [Python's unittest](https://docs.python.org/2/library/unittest.html)
- [Selenium webdriver](https://www.seleniumhq.org/docs/03_webdriver.jsp) 
- [Selenium with Python bindings](https://selenium-python.readthedocs.io/)
- [Docker CE](https://docs.docker.com/install/)