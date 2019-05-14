def stuff(event, context):
    try:
        return dict(
            statusCode=200,
            body='VERY COOL!!'
        )
    except Exception as e:
        return dict(
            statusCode=500,
            body=str(e)
        )

