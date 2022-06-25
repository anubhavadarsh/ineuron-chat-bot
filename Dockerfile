FROM python:latest
Add . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD flask run