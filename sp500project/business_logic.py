from data_access import get_all_records
from data_access import write_to_csv_db
from time import time

cache_storage = {}


def cache(cache_time=5):
    def inner(func):
        def wrapper(*args, **kwargs):
            value, expiration_time = cache_storage.get(args, (None, None))
            if value and time() <= expiration_time:
                return value

            res = func(*args, **kwargs)
            expiration_time = time() + cache_time
            cache_storage[args] = (res, expiration_time)
            return res

        return wrapper

    return inner


@cache(cache_time=10)
def find_info_by_name(company_name):
    data = get_all_records()
    result = []
    for row in data:
        if company_name.lower() in row.get("Name").lower():
            result.append({
                "Symbol": row.get("Symbol"),
                "Name": row.get("Name"),
                "Sector": row.get("Sector"),
                "Stock Price": row.get("Price")
            }
            )
    return result


def list_of_companies(sector):
    data = get_all_records()
    result = []
    for row in data:
        if sector in row['Sector']:
            result.append(row['Name'])
    return result


def average_price():
    counter_of_companies = 0
    total_price = 0
    data = get_all_records()
    for row in data:
        counter_of_companies += 1
        total_price += float(row.get('Price'))
    av_price = round((total_price / counter_of_companies), 2)
    return av_price


def top_ten():
    companies = []
    price = []
    data = get_all_records()
    fin_pr = [(row['Name'], row['Price']) for row in data]
    fin = sorted(fin_pr, key=lambda x: (x[1]), reverse=True)
    return fin[1:11]


def check_in_data(symbol_name='', company_name='', sector=''):
    data = get_all_records()
    flag = False
    for row in data:
        if symbol_name == row.get('Symbol'):
            flag = True
            break
        if company_name.lower() == row.get('Name').lower():
            flag = True
            break
        if sector.lower() == row.get('Sector').lower():
            flag = True
            break
    return flag


def truncate_all_data() -> None:
    data = get_all_records()
    fields = []
    data = []
    mode = 'w'


def add_new_company(symbol, name, sector, price):
    fieldnames = ["Symbol", "Name", "Sector", "Price"]
    values = [symbol, name, sector, price]
    new_company = [{fieldnames[i]: values[i] for i in range(len(fieldnames))}]
    get_all_records()


def update_company_name(company_symbol, company_name):
    data = get_all_records()
    new_data = []
    fields = []
    for row in data:
        if row.get("Symbol") == company_symbol.upper():
            row["Name"] = company_name
        new_data.append(row)

    for keys in new_data[0].keys():
        fields.append(keys)

    write_to_csv_db(fields, new_data, 'w')



