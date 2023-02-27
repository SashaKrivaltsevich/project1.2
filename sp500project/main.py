from validators import (validate_user_choice,
                        symbol_name_in_data,
                        validate_symbol_name,
                        validate_company_name,
                        validate_sector_name,
                        validate_company_price)
from errors import (IncorrectUserInputError,
                    IncorrectNewCompanyNameError,
                    IncorrectSymbolError,
                    IncorrectSectorNameError,
                    IncorrectCompanyPriceError)
from business_logic import (average_price,
                            top_ten,
                            find_info_by_name,
                            truncate_all_data,
                            add_new_company,
                            update_company_name)


while True:
    user_choice = input('1 - Find info by name\n'
                        '2 - Get all companies by sector\n'
                        '3 - Calculate average price\n'
                        '4 - Get top 10 companies\n'
                        "6 - Add new company\n"
                        "7 - Update company name\n"
                        "8 - Delete company\n"
                        "9 - Truncate all \n"
                        "10 - Populate file with random data\n"
                        '5 - Exit\nYour choice: \n')

    try:
        validate_user_choice(user_choice=user_choice)
    except IncorrectUserInputError as err:
        print(err)
        continue

    if user_choice == "5":
        print("GOODBYE!")
        break

    elif user_choice == "1":
        company_name = input("Enter search string: ")
        result = find_info_by_name(company_name)
        print(result)

    elif user_choice == '2':
        sector = input('Write the sector: ')
        list_of_companies = find_info_by_name(sector)
        print(list_of_companies)

    elif user_choice == '3':
        result = average_price()
        print(f'Average price: {result}')

    elif user_choice == '4':
        result = top_ten()
        print(f'Top ten companies: {result}')

    elif user_choice == "6":
        company_symbol = input('Enter Symbol of the company to be added: ')
        try:
            validate_symbol_name(company_symbol)
        except IncorrectSymbolError as err:
            print(err)
            continue
        company_name = input('Enter Name of the company to be added: ')
        try:
            validate_company_name(company_name)
        except IncorrectNewCompanyNameError as err:
            print(err)
            continue
        sector_name = input('Enter name of the Sector: ')
        try:
            validate_sector_name(sector_name)
        except IncorrectSectorNameError as err:
            print(err)
            continue
        company_price = input('Enter Price of the company: ')
        try:
            validate_company_price(company_price)
        except IncorrectCompanyPriceError as err:
            print(err)
            continue
        add_new_company(company_symbol, company_name,
                        sector_name, company_price)
        print(f'You added the {company_name} company to the list.')

    elif user_choice == "7":
        company_symbol = input('Enter the symbol of the company whose name '
                               'is to be changed: ').upper()
        try:
            symbol_name_in_data(symbol_name=company_symbol)
        except IncorrectSymbolError as err:
            print(err)
            continue
        company_name = input('Enter new name of the company: ')
        try:
            validate_company_name(company_name)
        except IncorrectNewCompanyNameError as err:
            print(err)
            continue
        update_company_name(company_symbol, company_name)
        print(f"New name of company with {company_symbol} Symbol:"
              f" {company_name}.")

    elif user_choice == '8':
        company_symbol = input('Enter the symbol of the company that will '
                               'be deleted: ')
        try:
            symbol_name_in_data(symbol_name=company_symbol)
        except IncorrectSymbolError as err:
            print(err)
            continue

    elif user_choice == "9":
        answer = input('Enter "YES" if you seriously want to delete all data.')
        if answer.upper() == 'YES':
            truncate_all_data()
            print('Complete. All data has been deleted.')
        else:
            print('The data has NOT been deleted.')
        continue








