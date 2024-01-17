#! /bin/sh

TAGNAME="auto-generate-novelai"
ENV_FILE=".env"
if [ ! -f $ENV_FILE ]; then
    echo "plase write .env"
    exit 1
fi

. ./$ENV_FILE

CMD_DOCKER=$(which docker)
if [ ! -f $CMD_DOCKER ]; then
    echo "please install docker or other container apps."
    exit 1
fi

$CMD_DOCKER build -t auto-generate-novelai .
ret=$?
echo "ret:$ret"
if [ $ret -ne 0 ]; then
    echo "failed docker build"
    exit 1
fi
# echo "$CMD_DOCKER container run -d --name $TAGNAME --env-file $ENV_FILE -p 8051:8501 --mount type=bind,src=$(pwd)$STORAGE_PATH,target=$STORAGE_PATH $TAGNAME"
$CMD_DOCKER container run -d --name $TAGNAME --env-file $ENV_FILE -p 8051:8501 --mount type=bind,src="$(pwd)$STORAGE_PATH",target=$STORAGE_PATH $TAGNAME