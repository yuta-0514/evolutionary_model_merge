~#!/bin/bash

CONTAINER_NAME=llm
IMAGES=yuta-0514/llm
TAGS=1.0
PORT=8888

docker run --rm -it --gpus all --ipc host -v $PWD:$PWD -p ${PORT}:${PORT} --name ${CONTAINER_NAME} ${IMAGES}:${TAGS}

#run "umask 000" after this script
#docker makes file or dir by root, therefore make permission 777