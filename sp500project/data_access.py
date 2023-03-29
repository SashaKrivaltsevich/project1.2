import csv


class RecordAlreadyExists(Exception):
    ...


def get_all_records():
    with open("sp500.csv") as db_file:
        data = csv.DictReader(db_file)
        return list(csv.DictReader(db_file))


def record_exist(company_name):
    with open("sp500.csv") as db_file:
        for row in csv.DictReader(db_file):
            if company_name == row["Name"]:
                raise RecordAlreadyExists("Company already exists.")


def write_to_csv_db(fields, data, mode):
    with open('sp500.csv', newline='', mode='w') as \
            write_file:
        names = fields
        file_writer = csv.DictWriter(write_file, names)
        file_writer.writeheader()
        file_writer.writerows(data)


