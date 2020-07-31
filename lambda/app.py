import json
import boto3
from boto3.dynamodb.conditions import Key
from boto3 import client as boto3_client

def lambda_handler(event, context):
    lambda_client = boto3_client('lambda')
    dynamodb = boto3.resource('dynamodb', region_name="eu-west-3")
    table = dynamodb.Table("sam_table")
    items = table.get_item(Key={"ID": "1"})
    response = table.query(
        KeyConditionExpression=Key('ID').eq("1")
    )
    
    for key,value in response['Items'][0].items():
        if key == 'Visit':
            Visits = int(value)
            
    Hit = Visits + 1
    response = table.update_item(
        Key={
            'ID': "1",
        },
        UpdateExpression="set Visit = :r",
        ExpressionAttributeValues={
            ':r': Hit
        },
        ReturnValues="UPDATED_NEW"
    )
            
    #msg = {"key":"new_invocation", "at": "square"}
    #invoke_response = lambda_client.invoke(FunctionName="dynamoGet",
    #                                       InvocationType='RequestResponse',
    #                                       Payload=json.dumps(msg))
    #print(invoke_response)
    
    #return {"statusCode": 200,"body": Hit}

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        'body':Hit
    }

def get_visits(event):
    for key,value in event['Items'][0].items():
        if key == 'Visit':
            Visits = int(value)
            
    Hit = Visits + 1
