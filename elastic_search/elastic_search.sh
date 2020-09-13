git clone https://github.com/deviantony/docker-elk.git
cp logstash.conf docker-elk/logstash/pipeline/
cd docker-elk/
docker-compose up -d
