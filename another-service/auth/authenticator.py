import jwt


def generate_jwt():
    return jwt.encode({'something': 'payload'}, 'secret', algorithm='HS256')