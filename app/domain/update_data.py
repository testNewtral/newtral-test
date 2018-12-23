from app.models import Politician, Gender, Region, PoliticalOffice, PoliticalParty

RELATION_DATA = {
    'region': (Region, 'CCAA'),
    'gender': (Gender, 'GENERO'),
    'political_office': (PoliticalOffice, 'CARGO'),
    'political_party': (PoliticalParty, 'PARTIDO'),
}


def update_politician(politician_id, data):
    politician = Politician().fetch_by_id(politician_id)

    for key, val in data.items():
        if hasattr(politician, key):
            setattr(politician, key, val)

        relation_data = RELATION_DATA.get(key.lower())

        if relation_data:
            relation_model, relation_name = relation_data
            politician.remove_relationship(relation_name)

            relation = relation_model().fetch(val)
            relation.politicians.add(politician)
            relation.save()

    politician.save()

    return politician
