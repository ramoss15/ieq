from elasticsearch import Elasticsearch

from celeryclient import cc

client = Elasticsearch(hosts=['http://localhost:9200', 'http://localhost:9300'], verify_certs=False,
                       basic_auth=["my_admin", "yourpassword"], timeout=30)


def create_index(index_name):
    return client.indices.create(index=index_name)

@cc.task
def create_index_data(index_name: str, index_data: dict):
    index_data = dict(product_name=index_data.get('product_name'), product_id=index_data.get('id'))
    index_id = index_data.get('product_id')
    resp = client.index(index=index_name, document=index_data, id=str(index_id))
    return resp

def search_product(index_name, product_name):
    query = {"query": {"match": {"content": product_name}}}
    search_ids = list()
    try:
        resp = client.search(index=index_name, body=query)
    except Exception as e:
        print(e)
        return search_ids
    for hit in resp["hits"]["hits"]:
        _source = hit.get("_source")
        search_ids.append(int(hit.get("_id")))
    return search_ids

def delete_index_data(index_name, index_id):
    return client.delete(index=index_name, id=str(index_id))
