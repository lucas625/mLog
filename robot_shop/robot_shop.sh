git clone https://github.com/instana/robot-shop
cd robot-shop/
docker-compose build
docker-compose -f docker-compose.yaml -f docker-compose-load.yaml up
