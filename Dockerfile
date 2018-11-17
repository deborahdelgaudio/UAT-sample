# @see https://github.com/joyzoursky/docker-python-chromedriver

FROM joyzoursky/python-chromedriver:2.7-selenium
WORKDIR /var/www/test-search-functionality
ADD . .
RUN pip install requests html-testRunner
CMD ["sh", "-c", "python test_run.py"]