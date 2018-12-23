import csv

from app.domain.db_queries import (
    create_politician,
    create_region,
    create_gender,
    create_political_office,
    create_political_party,
)


def add_errors(import_errors, errors):
    for error in errors:
        import_errors.append(error.message)

    return import_errors


def load_data(data_file):

    dialect = csv.Sniffer().sniff(data_file.readline())
    data_file.seek(0)
    reader = csv.DictReader(data_file, dialect=dialect, skipinitialspace=True)

    politicians = []
    regions = set()
    genders = set()
    political_offices = set()
    political_parties = set()

    import_errors = []

    for row in reader:
        politicians.append(row)
        regions.add(row.get('CCAA'))
        genders.add(row.get('GENERO'))
        political_offices.add(row.get('CARGO_PARA_FILTRO'))
        political_parties.add(row.get('PARTIDO_PARA_FILTRO'))

    for region in regions:
        errors = create_region(region)
        if errors:
            import_errors = add_errors(import_errors, errors)

    for gender in genders:
        errors = create_gender(gender)
        if errors:
            import_errors = add_errors(import_errors, errors)

    for political_office in political_offices:
        errors = create_political_office(political_office)
        if errors:
            import_errors = add_errors(import_errors, errors)

    for political_party in political_parties:
        errors = create_political_party(political_party)
        if errors:
            import_errors = add_errors(import_errors, errors)

    for politician in politicians:
        errors = create_politician(politician)
        if errors:
            import_errors = add_errors(import_errors, errors)

    return import_errors


# row.get('TITULAR'),
# row.get('PARTIDO'),
# row.get('PARTIDO_PARA_FILTRO'),
# row.get('CARGO_PARA_FILTRO'),
# row.get('CARGO'),
# row.get('INSTITUCION'),
# row.get('SUELDOBASE_SUELDO'),
# row.get('COMPLEMENTOS_SUELDO'),
# row.get('PAGASEXTRA_SUELDO'),
# row.get('OTRASDIETASEINDEMNIZACIONES_SUELDO'),
# row.get('TRIENIOS_SUELDO'),
# row.get('RETRIBUCIONMENSUAL'),
# row.get('RETRIBUCIONANUAL'),
# row.get('OBSERVACIONES')
