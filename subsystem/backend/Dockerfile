FROM python:3.8-buster AS base

# Directorio de trabajo
WORKDIR /usr/local/app/

# Dependencias
RUN apt-get clean \
    && apt-get -y update \
    && apt-get -y install python3-dev \
    && apt-get -y install build-essential \
    && apt-get -y install libpcre3 libpcre3-dev

# instalar redis
RUN apt-get install -y redis-server

# instalar mongoDB
RUN apt-get -y install apt-utils
RUN wget -qO - https://www.mongodb.org/static/pgp/server-4.4.asc | apt-key add -
RUN echo "deb http://repo.mongodb.org/apt/debian buster/mongodb-org/4.4 main" | tee /etc/apt/sources.list.d/mongodb-org-4.4.list
RUN apt-get update \
    && apt-get -y install mongodb-org


# instalar python requirements
COPY requirements.txt .
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt


# copy config and application files
COPY ./open-api ./open-api
COPY ./src ./src
COPY ./setup.py ./setup.py
RUN pip install -e .

# expose port used by uwsgi
EXPOSE 3000

ENTRYPOINT [ "/bin/bash", "/usr/local/app/src/startup.sh" ] 