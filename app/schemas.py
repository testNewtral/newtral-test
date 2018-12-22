import graphene

from app.models import Politician, Gender, PoliticalOffice, PoliticalParty, Region


class PoliticianSchema(graphene.ObjectType):
    anual = graphene.String()
    position = graphene.String()
    from_region = graphene.String()
    allowance = graphene.String()
    institution = graphene.String()
    monthly_income = graphene.String()
    name = graphene.String()
    kind = graphene.String()
    income = graphene.String()


class RegionSchema(graphene.ObjectType):
    name = graphene.String()


class GenderSchema(graphene.ObjectType):
    name = graphene.String()


class PoliticalOfficeSchema(graphene.ObjectType):
    name = graphene.String()


class PoliticalPartySchema(graphene.ObjectType):
    name = graphene.String()


class CreatePolitician(graphene.Mutation):
    class Arguments:
        anual = graphene.String()
        position = graphene.String()
        from_region = graphene.String()
        allowance = graphene.String()
        institution = graphene.String()
        monthly_income = graphene.String()
        name = graphene.String(required=True)
        kind = graphene.String()
        income = graphene.String()

    success = graphene.Boolean()
    politician = graphene.Field(lambda: PoliticianSchema)

    def mutate(self, info, **kwargs):
        politician = Politician(**kwargs)
        politician.save()

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


class Mutations(graphene.ObjectType):
    create_politician = CreatePolitician.Field()
    create_region = CreateRegion.Field()
    create_gender = CreateGender.Field()
    create_political_office = CreatePoliticalOffice.Field()
    create_political_party = CreatePoliticalParty.Field()


schema = graphene.Schema(mutation=Mutations, auto_camelcase=False)
