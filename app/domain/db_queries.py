from app.schemas import schema


def create_politician(data):

    res = schema.execute('''
        mutation {{
            create_politician(
                name:"{}",
                institution:"{}",
                anual_income:{},
                monthly_income:{},
                income:{},
                allowance:{},
                extra_income:{},
                notes:"{}",
                gender:"{}",
                region:"{}",
                political_office:"{}",
                political_party:"{}",
            ) {{
                politician {{
                    name,
                    institution,
                    anual_income,
                    monthly_income,
                    income,
                    allowance,
                    extra_income,
                    notes,
                }},
                success
            }}
        }}
    '''.format(
        data.get('TITULAR').replace('"', '\''),
        data.get('INSTITUCION'),
        data.get('RETRIBUCIONANUAL', '').replace(',', '.') or 0,
        data.get('RETRIBUCIONMENSUAL', '').replace(',', '.') or 0,
        data.get('SUELDOBASE_SUELDO', '').replace(',', '.') or 0,
        data.get('OTRASDIETASEINDEMNIZACIONES_SUELDO', '').replace(',', '.') or 0,
        data.get('PAGASEXTRA_SUELDO', '').replace(',', '.') or 0,
        data.get('OBSERVACIONES'),
        data.get('GENERO'),
        data.get('CCAA'),
        data.get('CARGO_PARA_FILTRO'),
        data.get('PARTIDO_PARA_FILTRO'),

        # data.get('TRIENIOS_SUELDO'),
        # data.get('COMPLEMENTOS_SUELDO'),

    ))

    if res.data and res.data.get('success'):
        return res.data.get('politician')

    return res.errors


def create_region(name):
    res = schema.execute('''
        mutation {{
            create_region(name:"{}") {{
                region {{
                    name
                }},
                success
            }}
        }}
    '''.format(
        name
    ))

    if res.data and res.data.get('success'):
        return res.data.get('region')

    return res.errors


def create_gender(name):
    res = schema.execute('''
        mutation {{
            create_gender(name:"{}") {{
                gender {{
                    name
                }},
                success
            }}
        }}
    '''.format(
        name
    ))

    if res.data and res.data.get('success'):
        return res.data.get('gender')

    return res.errors


def create_political_office(name):
    res = schema.execute('''
        mutation {{
            create_political_office(name:"{}") {{
                political_office {{
                    name
                }},
                success
            }}
        }}
    '''.format(
        name
    ))

    if res.data and res.data.get('success'):
        return res.data.get('political_office')

    return res.errors


def create_political_party(name):
    res = schema.execute('''
        mutation {{
            create_political_party(name:"{}") {{
                political_party {{
                    name
                }},
                success
            }}
        }}
    '''.format(
        name
    ))

    if res.data and res.data.get('success'):
        return res.data.get('political_party')

    return res.errors
