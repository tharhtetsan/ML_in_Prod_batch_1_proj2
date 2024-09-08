FROM python:3.10.14

EXPOSE 8080


WORKDIR /app
COPY . .

RUN apt-get update


RUN pip install pipenv
RUN pipenv install --system --deploy

CMD [ "python3","main.py" ]