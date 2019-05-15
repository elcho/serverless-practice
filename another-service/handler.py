from weather import forecaster
from auth import authenticator
import json

# for local:
# from .weather import forecaster


def weather(event, context):
    try:
        forecast = forecaster.get_forecast()
        return {
            'statusCode': 200,
            'body': json.dumps(forecast)
        }
    except Exception as e:
        return dict(
            statusCode=500,
            body=str(e)
        )


def jwt(event, context):
    try:
        encoded = authenticator.generate_jwt()
        return {
            'statusCode': 200,
            'body': encoded.decode('utf-8')
        }
    except Exception as e:
        return dict(
            statusCode=500,
            body=str(e)
        )
