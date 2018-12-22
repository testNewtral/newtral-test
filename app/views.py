from io import StringIO

from flask import Blueprint, jsonify, request

from app.domain.load_data import load_data


import_file = Blueprint('import_filehome', __name__)


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

    # res = schema.execute('''
    #     mutation {
    #         create_politician(name:"Peter", kind:"JUAS") {
    #             politician {
    #                 anual,
    #                 position,
    #                 from_region,
    #                 allowance,
    #                 institution,
    #                 monthly_income,
    #                 name,
    #                 kind,
    #                 income,
    #             },
    #             success
    #         }
    #     }
    # ''')
