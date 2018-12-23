from io import StringIO

from flask import Blueprint, jsonify, request

from app.domain.load_data import load_data
from app.domain.retrieve_data import get_politicians
from app.domain.create_data import create_politician
from app.domain.update_data import update_politician

import_file = Blueprint('import_file', __name__)
politician = Blueprint('politician', __name__)


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


@politician.route('/index', methods=['GET'])
def get_politicians_view():
    politicians = get_politicians(50)
    return jsonify(politicians)


@politician.route('/create', methods=['POST'])
def create_politician_view():
    try:
        politician = create_politician(request.form.to_dict())
        return jsonify(politician.as_dict())
    except Exception:
        return jsonify({'error': 'Error in input data'}), 400


@politician.route('/update/<politician_id>', methods=['PUT'])
def update_politician_view(politician_id):
    try:
        politician = update_politician(politician_id, request.form.to_dict())
        return jsonify(politician.as_dict())
    except Exception as e:
        return jsonify({'error': 'Error in input data'}), 400
