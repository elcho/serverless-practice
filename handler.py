def hello(event, context):
    try:
        return dict(
            statusCode=200,
            body='HELLO FROM SERVERLESS FUNCTION!!'
        )
    except Exception as e:
        return dict(
            statusCode=500,
            body=str(e)
        )

