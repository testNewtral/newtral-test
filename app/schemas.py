import graphene

from app.models import Politician, Gender, PoliticalOffice, PoliticalParty, Region
from app.domain.create_data import create_politician


class PoliticianSchema(graphene.ObjectType):
    name = graphene.String()
    institution = graphene.String()
    anual_income = graphene.Float()
    monthly_income = graphene.Float()
    income = graphene.Float()
    allowance = graphene.Float()
    extra_income = graphene.Float()
    notes = graphene.String()
    region = graphene.String()
    gender = graphene.String()
    political_party = graphene.String()
    political_office = graphene.String()


class GenderSchema(graphene.ObjectType):
    name = graphene.String()

    politicians = graphene.List(PoliticianSchema)


class PoliticalOfficeSchema(graphene.ObjectType):
    name = graphene.String()

    politicians = graphene.List(PoliticianSchema)


class PoliticalPartySchema(graphene.ObjectType):
    name = graphene.String()

    politicians = graphene.List(PoliticianSchema)


class RegionSchema(graphene.ObjectType):
    name = graphene.String()

    political_parties = graphene.List(PoliticalPartySchema)


class CreatePolitician(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        institution = graphene.String()
        anual_income = graphene.Float()
        monthly_income = graphene.Float()
        income = graphene.Float()
        allowance = graphene.Float()
        extra_income = graphene.Float()
        notes = graphene.String()
        gender = graphene.String()
        region = graphene.String()
        political_office = graphene.String()
        political_party = graphene.String()

    success = graphene.Boolean()
    politician = graphene.Field(lambda: PoliticianSchema)

    def mutate(self, info, **kwargs):
        politician = create_politician(kwargs)
        return CreatePolitician(politician=politician, success=True)


class CreateRegion(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)

    success = graphene.Boolean()
    region = graphene.Field(lambda: RegionSchema)

    def mutate(self, info, **kwargs):
        region = Region(**kwargs)
        region.save()

        return CreateRegion(region=region, success=True)


class CreateGender(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)

    success = graphene.Boolean()
    gender = graphene.Field(lambda: GenderSchema)

    def mutate(self, info, **kwargs):
        gender = Gender(**kwargs)
        gender.save()

        return CreateGender(gender=gender, success=True)


class CreatePoliticalOffice(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)

    success = graphene.Boolean()
    political_office = graphene.Field(lambda: PoliticalOfficeSchema)

    def mutate(self, info, **kwargs):
        political_office = PoliticalOffice(**kwargs)
        political_office.save()

        return CreatePoliticalOffice(political_office=political_office, success=True)


class CreatePoliticalParty(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)

    success = graphene.Boolean()
    political_party = graphene.Field(lambda: PoliticalPartySchema)

    def mutate(self, info, **kwargs):
        political_party = PoliticalParty(**kwargs)
        political_party.save()

        return CreatePoliticalParty(political_party=political_party, success=True)


class DeleteDB(graphene.Mutation):
    success = graphene.Boolean()

    def mutate(self, info, **kwargs):
        Politician.delete_all()
        Gender.delete_all()
        Region.delete_all()
        PoliticalOffice.delete_all()
        PoliticalParty.delete_all()

        return DeleteDB(success=True)


class Mutations(graphene.ObjectType):
    create_politician = CreatePolitician.Field()
    create_region = CreateRegion.Field()
    create_gender = CreateGender.Field()
    create_political_office = CreatePoliticalOffice.Field()
    create_political_party = CreatePoliticalParty.Field()
    delete_db = DeleteDB.Field()


schema = graphene.Schema(mutation=Mutations, auto_camelcase=False)
