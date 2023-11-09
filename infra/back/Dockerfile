FROM python:3.8-slim-buster

ARG user
ARG uid

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

RUN useradd -G root -u $uid -d /app $user
RUN chown -R $user:$user /app

CMD [ "python3", "-m" , "flask", "run", "--debug", "--host=0.0.0.0", "--port=8089"]