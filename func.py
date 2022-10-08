import io
import json
import logging


import sys
# need to install elasticsearch to docker image
from elasticsearch import Elasticsearch


from fdk import response


def handler(ctx, data: io.BytesIO = None):
    try:
        logs = json.loads(data.getvalue())

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
            print ("the length of input is  " + str(len(logs)), file=sys.stderr)
            return response.Response(ctx, response_data=json.dumps(logs), headers={"Content-Type": "application/json"})


    except (Exception, ValueError) as ex:
        logging.getLogger().info('error parsing json payload: ' + str(ex))

    logging.getLogger().info("Inside Python Hello World function")
    return response.Response(ctx, response_data=json.dumps(logs), headers={"Content-Type": "application/json"})
