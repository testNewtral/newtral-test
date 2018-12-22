from app.schemas import schema


# def create_politician(anual,
#                       position,
#                       from_region,
#                       allowance,
#                       institution,
#                       monthly_income,
#                       name,
#                       kind,
#                       income):
# 
#     res = schema.execute('''
#         mutation {
#             create_politician(name:"Peter", kind:"JUAS") {
#                 politician {
#                     {},
#                     {},
#                     {},
#                     {},
#                     {},
#                     {},
#                     {},
#                     {},
#                     {},
#                 },
#                 success
#             }
#         }
#     '''.format(
#         anual,
#         position,
#         from_region,
#         allowance,
#         institution,
#         monthly_income,
#         name,
#         kind,
#         income,
#     ))
# 
#     if res.data and res.data.get('success'):
#         return res.data.get('politician')


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


def create_political_office(name):
    res = schema.execute('''
        mutation {{
            create_political_office(name:"{}") {{
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
        return res.data.get('political_office')


def create_political_party(name):
    res = schema.execute('''
        mutation {{
            create_political_party(name:"{}") {{
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
        return res.data.get('political_party')
