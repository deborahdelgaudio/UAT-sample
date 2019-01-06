# Test search functionality
> A super test suite for autohero.com search page

## Description

This is a test suite written in python, that tests the search functionality of autohero.com.
This application uses: 

- **Unittest**,  a python framework useful to organize the test's code 
- **Selenium webdriver** with python bindings that provides an instance of the Chrome browser and some useful methods to interact with it 
- Some external python's libraries like _HtmlTestRunner_ and _requests_ 

The application runs in a Docker container. 

## How to run test suite

You have to clone the repository and build the Docker image by typing this command on the terminal:

```
$ docker build -t ${container_name}
```

where _${container_name}_ is the name that you have to choose for the container.

Now you are ready to test the autohero's search functionality by running the container, through this:

```
$ docker run ${container_name}
```

Test will automatically run and the results are can be seen as a terminal's output.  

If you want to access the HTMLTestRunner report run the container with the following command:

```
$ docker run -v $(pwd)/reports:/var/www/test-search-functionality/reports ${container_name}
```

### Requirments

If you want to run the suite locally, without the Docker's container, you need:

- python 3.7
- pip

Run the following command:

```
$ pip3 install -r requirements.txt
```

Pip will install all packages needed.
By running TestSuite locally you can change some parameters, type:
```
$ python3 main.py --help
```
to see which parameteres you can change.

Using the docker's container, only Docker is required.

### Sources

- [Python's unittest](https://docs.python.org/2/library/unittest.html)
- [Selenium webdriver](https://www.seleniumhq.org/docs/03_webdriver.jsp) 
- [Selenium with Python bindings](https://selenium-python.readthedocs.io/)
- [Docker CE](https://docs.docker.com/install/)
- [Docker's container with selenium and python](https://github.com/joyzoursky/docker-python-chromedriver)
