from app.models import Politician, Gender, Region, PoliticalOffice, PoliticalParty


def create_politician(data):
    politician = Politician(**data)
    politician.save()

    gender = Gender().fetch(data.get('gender'))
    region = Region().fetch(data.get('region'))
    political_office = PoliticalOffice().fetch(data.get('political_office'))
    political_party = PoliticalParty().fetch(data.get('political_party'))

    if gender:
        gender.politicians.add(politician)
        gender.save()

    if region:
        region.politicians.add(politician)
        region.save()

    if political_office:
        political_office.politicians.add(politician)
        political_office.save()

    if political_party:
        political_party.politicians.add(politician)
        political_party.save()

    return politician
