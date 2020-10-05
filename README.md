# MLog

A service that analyzes the log of the [Robot Shop](https://github.com/instana/robot-shop) and provides insights on how to increase sells.
This service is being built based on a microservices architecture.
This project will have the analysis of the **Payment** service of the Robot Shop as its scope.

![alt text](media/diagram.png?raw=true)

## Table OF Contents

- [MLog](#mlog)
  - [Table OF Contents](#table-of-contents)
  - [Team](#team)
  - [Backlog](#backlog)
  - [Requirements](#requirements)
  - [Installation](#installation)
    - [Robot Shop](#robot-shop)
    - [Elastic Search](#elastic-search)
    - [Mlog](#mlog-1)
  - [Testing](#testing)
  - [Production](#production)
  - [Guides](#guides)

## Team

- [Lucas Aurelio](https://github.com/lucas625)
- [Lucas Thierry](https://github.com/lucasthierry)
- [Marcus Rafael](https://github.com/marcusrafael)

## Backlog

- [Board](https://trello.com/invite/b/gBPAZXzy/567892ba668b70a6f3a84c1ad4a84c62/projeto-microservice)

## Requirements

- [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [Docker](https://www.docker.com/)
- [Docker-Compose](https://docs.docker.com/compose/install/)

## Installation

### Robot Shop

```sh
# Go to robot shop's folder
cd robot_shop

# Give permission to script.
chmod +x robot_shop.sh

# Run the script.
# The front-end of the robot shop will be available at: http://127.0.0.1:8080/
./robot_shop.sh
```

### Elastic Search

- Installing

```sh
# Go to elastic search's folder
cd elastic_search

# Give permission to script.
chmod +x elastic_search.sh

# Run the script.
# The front-end of the elastic search will be available at: http://127.0.0.1:5601/
./elastic_search.sh
```

- Setup

You will have to login into the elastic search interface. Use the following credentials:

```txt
user: elastic
password: changeme
```

Then you need to:

1. Go to **Discover**.
2. Create an index pattern with patthen: `logstash-*`.
3. Go to the next page and set `@timestamp`.
4. Go to **Discover** again, now you should be able to see the logs, once you upload then.

### Mlog

In order to work, mlog needs a few IPs, you must provide them on the setup_env.sh. Remember not to use localhost or 127.0.0.1, you must use your real IP.
Remember to change the secret key value and whenever you change the setup_env.sh you must run the commands bellow.

```sh
# Allow setup_env.sh
chmod +x ./setup_env.sh

# Set the env variables
source ./setup_env.sh

# Build and Run the containers.
# Mlog will be available at http://127.0.0.1:8084/
docker-compose up --build
```

## Testing

## Production

## Guides

- [Docker](https://docs.docker.com/get-started/)
- Django Rest Framework
  - [Docs](https://www.django-rest-framework.org/)
  - [Overview](http://www.cdrf.co/)
- Vue
  - [Docs](https://vuejs.org/)
  - [Vuetify](https://vuetifyjs.com/en/)
  - [Vue Router](https://router.vuejs.org/)
- [Elastic Search](https://github.com/deviantony/docker-elk)
  - [Elastic Search Py](https://github.com/elastic/elasticsearch-py)
