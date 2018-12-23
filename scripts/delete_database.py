from app.schemas import schema


def delete_database():
    schema.execute('''
        mutation {{
            delete_db {{
                success
            }}
        }}
    '''.format())
