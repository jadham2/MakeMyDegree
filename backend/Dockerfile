FROM ubuntu:20.04
RUN apt-get update \
&& apt-get install -y python3-pip python3-dev libpq-dev \
&& apt-get install -y vim
WORKDIR /src/backend
COPY requirements.txt /src/backend
RUN python3 -m pip install -r requirements.txt
COPY . /src/backend
EXPOSE 8000
ENTRYPOINT ["sh", "entrypoint.sh"]