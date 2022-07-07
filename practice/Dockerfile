FROM python:3.8

RUN mkdir /server
COPY /practice /server

RUN pip install -r /server/requirements.txt
EXPOSE 8000
WORKDIR /server
#CMD ["python", "-m", "django", "run", "--host=0.0.0.0"]
