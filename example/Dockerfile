FROM selenium/standalone-chrome:85.0-chromedriver-85.0-20200907
USER root

RUN apt-get update && \
  apt-get install -y python3-distutils && \
  curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && \
  python3 get-pip.py

WORKDIR /code
COPY requirements.txt .
RUN python3 -m pip install -r requirements.txt
COPY . .
CMD python3 run.py
