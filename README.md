# MLog

A service that analyzes the log of the [Robot Shop](https://github.com/instana/robot-shop) and provides insights on how to increase sells.
This service is being built based on a microservices architecture.
This project will have the analysis of the **cart** and **shipping** services of the Robot Shop as its scope.

![alt text](https://github.com/lucas625/MLog/blob/master/media/diagram.png?raw=true)

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

- [Docker](https://www.docker.com/)

## Installation

### Robot Shop

```sh
sudo apt update

sudo apt install virtualbox

curl -Lo minikube https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64

chmod +x minikube

sudo mkdir -p /usr/local/bin/

sudo install minikube /usr/local/bin/

curl -LO "https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl"

chmod +x ./kubectl

sudo mv ./kubectl /usr/local/bin/kubectl

curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3

chmod 700 get_helm.sh

./get_helm.sh

git clone https://github.com/instana/robot-shop

kubectl create ns robot-shop

helm install robot-shop --namespace robot-shop robot-shop/K8s/helm
```

### Cart Log Analyzer

```sh
# Go to the cart_log_analyzer's folder.
cd cart_log_analyzer

# Build the cart_log_analyzer's image.
docker build -t cart_log_analyzer .

# Run the cart_log_analyzer's container.
# Remember to replace the values between [] by the actual values.
docker run --name cart_log_analyzer_container \
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
