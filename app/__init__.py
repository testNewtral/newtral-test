from flask import Flask, jsonify

from app.views import import_file


def create_app():
    app = Flask(__name__)

    app.register_blueprint(import_file)

    @app.errorhandler(404)
    def page_not_found(e):
        return jsonify({'message': 'The requested URL was not found on the server.'}), 404

    return app
