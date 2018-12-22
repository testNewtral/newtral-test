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
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    @property
    def all(self):
        return self.select(graph)

    def save(self):
        graph.push(self)


class Region(BaseModel):
    name = Property()

    political_parties = RelatedTo('PoliticalParty', 'CCAA')  # BELONGS

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
    anual = Property()
    position = Property()
    from_region = Property()
    allowance = Property()
    institution = Property()
    monthly_income = Property()
    name = Property()
    kind = Property()
    income = Property()

    # anual: 250,00
    # cargo: Alcalde
    # cargo_filtro: Alcalde
    # ccaa: Canarias
    # dietas: 250,00
    # institucion: Ayuntamiento de LAS PALMAS DE GRAN CANARIA
    # mensual: 4297,95
    # nombre: Augusto Hidalgo Macario
    # observa: Dedicación Exclusiva
    # partido: PSOE
    # partido_filtro: PSOE
    # sueldo_base: 60171,30
