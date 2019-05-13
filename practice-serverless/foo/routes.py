def init_routes(app):

    @app.route('/hello-flask', methods=['GET'])
    def get_hello():
        return 'HELLO FROMM FLASK!!'

    @app.route('/', methods=['GET'])
    def get_root():
        return 'HI FROM FLASK!!'
