# MLog

A service that analyzes the log of the [Robot Shop](https://github.com/instana/robot-shop) and provides insights on how to increase sells.
This service is being built based on a microservices architecture.
This project will have the analysis of the **cart** and **shipping** services of the Robot Shop as its scope.

![alt text](media/diagram.png?raw=true)

## Table OF Contents

- [MLog](#mlog)
  - [Table OF Contents](#table-of-contents)
  - [Team](#team)
  - [Backlog](#backlog)
  - [Requirements](#requirements)
  - [Installation](#installation)
    - [Robot Shop](#robot-shop)
    - [Cart Log Analyzer](#cart-log-analyzer)
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

### Cart Log Analyzer

```sh
# Go to the cart_log_analyzer's folder.
cd cart_log_analyzer

# Build the cart_log_analyzer's image.
docker build -t mlog_cart_log_analyzer .

# Run the cart_log_analyzer's container.
# Remember to replace the values between [] by the actual values.
docker run --name mlog_cart_log_analyzer_container \
    -e SECRET_KEY=[SECRET_KEY] \
    -e DEBUG=[DEBUG] \
    -e PORT=[PORT] \
    -p [PORT]:[PORT] \
    -v "$(pwd):/cart_log_analyzer_volume" \
    cart_log_analyzer
```

## Testing

## Production

## Guides

- [Docker](https://docs.docker.com/get-started/)
- Django Rest Framework
  - [Docs](https://www.django-rest-framework.org/)
  - [Overview](http://www.cdrf.co/)
