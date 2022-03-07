#!/bin/bash
docker rm -f rick
docker build -t rick . && \
docker run --name=rick --rm -p8080:80 -it rick 
