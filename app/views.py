from io import StringIO

from flask import Blueprint, jsonify, request

from app.domain.load_data import load_data
from app.domain.retrieve_data import get_politicians


import_file = Blueprint('import_file', __name__)
index = Blueprint('get_politicians', __name__)


@import_file.route('/import', methods=['POST'])
def import_file_view():
    data_file = request.files.get('file')

    if not data_file:
        return jsonify({'error': 'request has not "file" attribute'}), 400

    stream = StringIO(data_file.stream.read().decode('utf-8-sig'), newline=None)
    errors = load_data(stream)

    if errors:
        return jsonify({'import': errors}), 400

    return jsonify({'import': 'ok'})


@index.route('/index', methods=['GET'])
def get_politicians_view():
    politicians = get_politicians(50)
    return jsonify(politicians)
