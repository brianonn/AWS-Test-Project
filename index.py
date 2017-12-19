import json
import datetime


def handler(event, context):
    data = {
        'output': 'Hello JASON',
        'timestamp': datetime.datetime.utcnow().isoformat()
    }
    html = """
        <html>
            <head>AWS-Test Project</head>
            <body>
                <div class="jason-test-div">
                    Hello Jason/Brian.
                </div>
            </body>
        </html>
    """
    return {'statusCode': 200,
            'body': html,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'OPTIONS, HEAD, GET, POST'
            }
        }
