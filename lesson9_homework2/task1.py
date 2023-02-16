import csv
from functools import reduce


def find_info():
    with open('sp500.csv') as file:
        data = csv.DictReader(file)
        while True:
            user_choice = input('1 - Find info by name\n'
                                '2 - Get all companies by sector\n'
                                '3 - Calculate average price\n'
                                '4 - Get top 10 companies\n'
                                '5 - Exit\nYour choice: ')
            if user_choice == "5":
                print("By")
                break
            if user_choice == '1':
                name_of_company = input('Write the company name: ')
                companies = []
                for row in data:
                    if name_of_company.lower() in row.get("Name").lower():
                        companies.append({
                            "Symbol": row.get("Symbol"),
                            "Name": row.get("Name"),
                            "Sector": row.get("Sector"),
                            "Stock Price": row.get("Price")
                        }
                        )
                for row in data:
                    if name_of_company in row['Name']:
                        companies.append(row)
                return companies

            elif user_choice == '2':
                sector = input('Write the sector: ')
                list_of_companies = []
                for row in data:
                    if sector in row['Sector']:
                        list_of_companies.append(row['Name'])
                return list_of_companies

            elif user_choice == '3':
                price = []
                for row in data:
                    price.append(float(row['Price']))
                av_pr = (reduce(lambda x, y: x + y, price) / len(price))
                return round(av_pr, 4)

            else :
                companies = []
                price = []
                for row in data:
                    companies.append(row['Name'])
                    price.append(row['Price'])
                fin_pr = list(zip(companies, price))
                fin = sorted(fin_pr, key=lambda x: (x[1]), reverse=True)
                return fin[1:11]



print(find_info())