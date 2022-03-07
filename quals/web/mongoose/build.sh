#!/bin/bash
docker rm -f mongoose
docker build -t mongoose . && \
docker run --name=mongoose --rm -p80:8080 -it mongoose
