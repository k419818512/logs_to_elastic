import io
import json
import logging
import urllib3


import sys
import random
from datetime import datetime
# need to install elasticsearch to docker image
from elasticsearch import Elasticsearch


from fdk import response

def isJson(jsonData):
    try:
        json.loads(jsonData)
    except ValueError as err:
        return 1 
    return 0



def handler(ctx, data: io.BytesIO = None):
    try:
        logs=''
        logs = json.loads(data.getvalue())
        #logs = logs[0]
        #logs = json.dumps(logs)
        #timestamp = int(round(datetime.now().timestamp()))
        client = Elasticsearch(
                ["https://03ac5b74f7fc483cba750cf5770d3966.us-central1.gcp.cloud.es.io:443"],
                http_auth=('elastic', 'Kau6ktrDkf8pKMmUJxYNFNkN'),
#               api_key=('3381795227', 'aXd2OWlZTUJGN1U3SFo4eFJ5aGk6RjVwTDdqOXZUTmV6T3JZR2pJR09jdw=='),
                request_timeout=120,
                verify_certs=True,
                ca_certs='./srch.crt',
                # Add your cluster configuration here!
        )
        for item in logs: 
            timestamp = int(round(datetime.now().timestamp()))
            y = json.dumps(item)
            print (y, file=sys.stderr)
            client.index(index = 'oci_logs_2', id = timestamp, document = y ) 



    except (Exception, ValueError) as ex:
        logging.getLogger().info('error parsing json payload: ' + str(ex))

    logging.getLogger().info("Inside Python Hello World function")
    return response.Response(ctx, response_data=logs, headers={"Content-Type": "application/json"})
