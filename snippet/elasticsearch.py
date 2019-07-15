# !pip install elasticsearch
import elasticsearch
from elasticsearch.helpers import bulk

# bulk indexing
# dataframe 형식의 데이터를 elasticsearch에 indexing
IP = ''
PORT = ''
ELASTIC_INDEX_NAME = ''
df = pd.read_csv('file_path')

bulk(elasticsearch.Elasticsearch(IP + ':' + PORT),
     df.to_dict(orient='records'),
     index=ELASTIC_INDEX_NAME,
     doc_type='doc',
     raise_on_error=True
     )


# suggest query
QUERY = ''

json = {
          "suggest": {
            "keyword": {
              "prefix": QUERY,
              "completion": {
                "field": "keyword.completion",
                "fuzzy": {
                  "fuzziness": 2
                }
              }
            }
          }
        }

headers = {'Content-Type': 'application/json; charset=utf-8'}
res = requests.post(IP  + ':' + PORT + '/ ' + ELASTIC_INDEX_NAME + '/_search', headers=headers, json=json)
res.json()


def main():
    pass
