import io
import json
import logging
import urllib3


import sys
import random
# need to install elasticsearch to docker image
from elasticsearch import Elasticsearch


from fdk import response


def handler(ctx, data: io.BytesIO = None):
    try:
        doc_body = {"@timestamp":"2022-10-09T14:48:26.959Z","log.level":"info","message":"Elvis has left the oven on.","ecs":{"version":"1.6.0"},"http":{"request":{"body":{"content":"Elvis has left the oven on."}}},"log":{"logger":"app","origin":{"file":{"line":38,"name":"elvis.py"},"function":"<module>"},"original":"Elvis has left the oven on."},"process":{"name":"MainProcess","pid":15552,"thread":{"id":140203898001216,"name":"MainThread"}}}
        logs = json.loads(data.getvalue())
        dk = random.randint(1, 10000000000)
        client = Elasticsearch(
                ["https://03ac5b74f7fc483cba750cf5770d3966.us-central1.gcp.cloud.es.io:443"],
                http_auth=('elastic', 'Kau6ktrDkf8pKMmUJxYNFNkN'),
#               api_key=('3381795227', 'aXd2OWlZTUJGN1U3SFo4eFJ5aGk6RjVwTDdqOXZUTmV6T3JZR2pJR09jdw=='),
                request_timeout=120,
                verify_certs=True,
                ca_certs='./srch.crt',
                # Add your cluster configuration here!
        )
        y = json.dumps(logs)
        print (y, file=sys.stderr)
        client.index(index = 'oci_logs_22', id = dk, document = logs) 
        return response.Response(ctx, response_data=json.dumps({"this":"is good"}), headers={"Content-Type": "application/json"})


    except (Exception, ValueError) as ex:
        logging.getLogger().info('error parsing json payload: ' + str(ex))

    logging.getLogger().info("Inside Python Hello World function")
    return response.Response(ctx, response_data=json.dumps(logs), headers={"Content-Type": "application/json"})
