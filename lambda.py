import json
import math
from http import HTTPStatus
from time import gmtime, strftime

import boto3


dynamodb = boto3.resource("dynamodb", region="us-east-1")
table = dynamodb.Table("PowerOfMathDatabase")
now = strftime("%a, %d, %Y %H:%M:%s +0000", gmtime())


def lambda_handler(event, context):
    math_result = math.pow(int(event["base"]), int(event["exponent"]))
    response = None
    try:
        response = table.put_item(
            Item={
                "id": str(math_result),
                "latestGreetingTime": now
            }
        )
    except Exception as err:
        print(err)

    return {
        "statusCode": HTTPStatus.OK,
        "body": json.dumps(f"Your result is: {str(math_result)}"),
        "response": response
    }
