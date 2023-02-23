from business_logic import find_info_by_name
from validators import validate_user_choice
from errors import IncorrectUserInputError
from business_logic import average_price
from business_logic import top_ten


while True:
    user_choice = input('1 - Find info by name\n'
                        '2 - Get all companies by sector\n'
                        '3 - Calculate average price\n'
                        '4 - Get top 10 companies\n'
                        '5 - Exit\nYour choice: ')

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







