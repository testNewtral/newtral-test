from app.models import Politician


def get_politicians(limit):
    politicians = []
    politicians_match = Politician().all

    for politician in politicians_match.limit(limit):
        politicians.append(politician.as_dict())

    return politicians
