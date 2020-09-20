from elasticsearch import Elasticsearch
import json

es = Elasticsearch(['http://localhost:9200'], http_auth=('elastic', 'changeme'))

search = {
  "query": {
    "query_string": {
      "query": "total",
      "default_field": "message"
    }
  }
}

res = es.search(index="logstash-*", body=search, size=500)

a = [json.loads(resultado['_source']['message'].split('INFO in payment: ')[1].replace('\'', '\"')) for resultado in res['hits']['hits']]
print(a)
