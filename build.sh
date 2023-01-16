#!/usr/bin/env sh

docker build -t trapinit-hello-world-trap .
docker save trapinit-hello-world-trap > ./images.tar

zip hello-world-trap.zip docker-compose.yml images.tar trapdef.json bait-template.txt
