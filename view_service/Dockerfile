FROM alpine:3.12.0

RUN apk add yarn

COPY . /view_service
WORKDIR /view_service

RUN yarn install

ENV VIEW_SERVICE_PORT ""
ENV VUE_APP_ANALYZER_URL ""

ENTRYPOINT yarn serve --port $VIEW_SERVICE_PORT
