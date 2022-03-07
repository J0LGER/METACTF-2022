#!/bin/bash
docker rm -f space_travel
docker build -t space_travel . && \
docker run --name=space_travel --rm -p4443:80 -it space_travel 
