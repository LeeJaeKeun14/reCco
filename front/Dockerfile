# Dockerfile-Dev는 docker-compose를 통해서가아닌
# Docker run을 통하여 따로 실행시킬때 사용합니다.

# build
# docker build -t <태그이름> -f ./Dockerfile.dev . 

#run
#docker run -it -d -p 3000:3000 image-id
# -d -> demon으로 실행한다는 의미입니다 써주지 않아도 됩니다
# -p 전달포트:목표포트 입니다 전달포트의 경우 외부에서 접속하는 포트이며 목표포트는 실제 client가 Docker 내에서 사용하는 포트입니다.

FROM node:16-alpine3.14

WORKDIR /srv/client

COPY . /srv/client

RUN apk update && apk add bash

ENTRYPOINT ["sh", "entrypoint.sh"]

#만약 필요한 ENV(환경변수)가 있다면
# ENV key=value 로 선언주면됩니다.
