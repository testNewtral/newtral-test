from py2neo import Graph
from py2neo.ogm import GraphObject, Property, RelatedTo

from app import settings


graph = Graph(
    host=settings.NEO4J_HOST,
    port=settings.NEO4J_PORT,
    user=settings.NEO4J_USER,
    password=settings.NEO4J_PASSWORD,
)


class BaseModel(GraphObject):
    __primarykey__ = "name"

    def __init__(self, **kwargs):

        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    @property
    def all(self, limit=None):
        return self.match(graph)

    def save(self):
        graph.push(self)

    def fetch(self, name):
        return self.match(graph, name).first()

    def fetch_by_id(self, obj_id):
        return self.match(graph).where('ID(_) = {}'.format(obj_id)).first()

    @staticmethod
    def delete_all():
        graph.delete_all()


class Region(BaseModel):
    name = Property()

    politicians = RelatedTo('Politician', 'CCAA')  # BELONGS

    def as_dict(self):
        return {
            'name': self.name,
        }


class Gender(BaseModel):
    name = Property()

    politicians = RelatedTo('Politician', 'GENERO')  # GENDER

    def as_dict(self):
        return {
            'name': self.name,
        }


class PoliticalOffice(BaseModel):
    name = Property()

    politicians = RelatedTo('Politician', 'CARGO')  # POLITICAL_OFFICE

    def as_dict(self):
        return {
            'name': self.name,
        }


class PoliticalParty(BaseModel):
    name = Property()

    politicians = RelatedTo('Politician', 'PARTIDO')  # MILITATE

    def as_dict(self):
        return {
            'name': self.name,
        }


class Politician(BaseModel):
    FK_ATTRS = ['region', 'gender', 'political_office', 'political_party']

    name = Property()
    institution = Property()

    anual_income = Property()
    monthly_income = Property()
    income = Property()
    allowance = Property()
    extra_income = Property()

    notes = Property()

    region = Property()
    gender = Property()
    political_office = Property()
    political_party = Property()

    def as_dict(self):
        return {
            'name': self.name,
            'institution': self.institution,
            'anual_income': self.anual_income,
            'monthly_income': self.monthly_income,
            'income': self.income,
            'allowance': self.allowance,
            'extra_income': self.extra_income,
            'notes': self.notes,
            'region': self.region,
            'gender': self.gender,
            'political_party': self.political_party,
            'political_office': self.political_office,
        }

    def remove_relationship(self, relationship):
        possible_relationships = ['CCAA', 'GENERO', 'PARTIDO', 'CARGO']

        if relationship not in possible_relationships:
            return

        query = '''
            MATCH (n{{name:"{}"}})-[r:GENERO]-()
            DELETE r
        '''.format(self.name)

        return graph.run(query).data()
