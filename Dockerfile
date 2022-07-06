FROM python:

WORKDIR /home/oem/practice_test1/pracrice
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .