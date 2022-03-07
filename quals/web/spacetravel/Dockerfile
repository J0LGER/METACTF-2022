FROM ubuntu:latest 

ENV TZ=Europe/Minsk
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezon
ENV DEBIAN_FRONTEND noninteractive 
ENV TERM xterm

RUN apt update -y   
USER root

#Install application packages
RUN apt install -y supervisor nginx  gnupg systemctl
RUN apt update -y 
 
COPY config/supervisord.conf /etc/supervisord.conf
COPY challenge /var/www/html



CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]
EXPOSE 80