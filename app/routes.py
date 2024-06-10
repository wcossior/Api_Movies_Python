def register_routes(app):
    @app.route('/')
    def holamundo():
        return "Hello, World! Natalia"