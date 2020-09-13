from datetime import datetime
from elasticsearch import Elasticsearch

es = Elasticsearch(['http://localhost:9200'], http_auth=('elastic', 'changeme'))
# resp = es.search(index="logstash-*")

res = es.search(index="logstash-*", body={"query": {"match_all": {}}})
print(res)
