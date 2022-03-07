FROM ubuntu:latest 

ENV TZ=Europe/Minsk
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezon
ENV DEBIAN_FRONTEND noninteractive 
ENV TERM xterm

RUN apt update -y   
USER root

#Install application packages
RUN apt install -y supervisor nginx wget gnupg systemctl python3-pip 
RUN wget -qO - https://www.mongodb.org/static/pgp/server-4.4.asc | apt-key add - && \ 
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/4.4 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-4.4.list
RUN apt update -y && \
apt install -y mongodb-org  
RUN pip install flask pymongo flask-jwt-extended

COPY config/nginx.conf /etc/nginx/nginx.conf 
COPY config/supervisord.conf /etc/supervisord.conf
COPY challenge /www 



CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]
EXPOSE 80