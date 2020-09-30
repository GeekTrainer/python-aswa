import logging, json

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    tasks = ['Clean up GitHub repos', 'Check out cool stuff on Azure Functions']

    return func.HttpResponse(
        body=json.dumps({'tasks': tasks}),
        mimetype='application/json'
    )
