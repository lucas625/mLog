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
# Give permission to script.
chmod +x robot_shop.sh

# Run the script.
# The front-end of the robot shop will be available at: http://127.0.0.1:8080/
./robot_shop.sh
```

### Elastic Search

- Installing

```sh
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

Before running you **MUST** create a file called **.env** on each of the specified folders and pass the required environment variables.

- payment_log_analyzer:
  - SECRET_KEY

- csv_service
  - SECRET_KEY

- search_service
  - SECRET_KEY

```sh
# Set ports.
# Remember to change the values between [] for the actual ports.
export CSV_SERVICE_PORT=[PORT]
export PAYMENT_LOG_ANALYZER_PORT=[PORT]
export SEARCH_SERVICE_PORT=[PORT]

# Build images
docker-compose build

# Build and Run the containers.
docker-compose up
```

## Testing

## Production

## Guides

- [Docker](https://docs.docker.com/get-started/)
- Django Rest Framework
  - [Docs](https://www.django-rest-framework.org/)
  - [Overview](http://www.cdrf.co/)
- [Elastic Search](https://github.com/deviantony/docker-elk)
  - [Elastic Search Py](https://github.com/elastic/elasticsearch-py)
