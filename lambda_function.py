
from __future__ import print_function # Python 2/3 compatibility
import boto3
import json

def respond(err, response=None):
	return {
		'statusCode': '400' if err else '200',
		'body': err if err else json.dumps(response),
		'headers': {
			'Content-Type': 'application/json',
		},
	}
	
def add_item(event):
    try:
        requestBody = json.loads(event['body'])
        listName = requestBody['listName']
    except KeyError:
		return respond('Request is not properly formated.')

    # create dynamodb resource object
    client = boto3.resource('dynamodb')

    #  search for dynamoDB table 
    table = client.Table("Lists")
    print(table.table_status)

	#create a new db entry
    messageData = {
        'Name': str(listName)
	}

    table.put_item(Item=messageData)
    
    return respond(None, messageData)


def lambda_handler(event, context):
    # TODO implement
    
    # Because we're using a Cognito User Pools authorizer, all of the claims
    # included in the authentication token are provided in the request context.
    # This includes the username as well as other attributes.
    # username = event.requestContext.authorizer.claims['cognito:username'];
    
    return add_item(event)