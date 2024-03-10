import time

# Grade Calculator

print('BTEC EXTENDED CERTIFICATE GRADE CALCULATOR')

name = input("What's your name: ")

print("Alrighty " + name + '!' + " Let's Begin")

time.sleep(2)

menu = print('\nFill in your grades:')

grade = ''
points = 0
total_points = 0

no_unit = [1, 2, 3, 12, 9, 10, 11, 13]

unit_name = ['Online World', 'Technology Systems', 'Digital Portfolio', 'Software Development', 'Spreadsheet Development',
             'Databse Development', 'Computer Netw0rks', 'Website Development']

while True:
    for no, units in zip(no_unit, unit_name):  # Iterate
        time.sleep(1.5)  # delay

        unit = 'Unit',no,units
        print(unit)

        time.sleep(1.5)  # delay

        grade = input(
            '\nThe letters represent your grade \n Distinction = D  \n Merit = M \n Pass = P \n Level 1 Pass = L1P \n Undefined = U \n : ')
        if grade.upper() == 'D':
            points = 24
            total_points += 24
        elif grade.upper() == 'M':
            points = 18
            total_points += 18
        elif grade.upper() == 'P':
            points = 12
            total_points += 12
        elif grade.upper() == 'L1P':
            points = 6
            total_points += 6
        elif grade.upper() == 'U':
            points = 0
            total_points += 0
        else:
            print('Invalid Option')

        time.sleep(1.5)  # delay

        print('\nYour points for', unit, 'is', points,'\n')
        time.sleep(1.5)

    user_q = input("COMPLETED, Select 'Y' to see your total points : ")
    if user_q.upper() == 'Y':
        total_points += points
        print('\nYour total points is', total_points)

        if total_points >= 144:
            print('\nCongratulations, You Passed')
        else:
            print("\nI'm sorry, you failed")

        back = input('\nGo back to the main menu? (y/n) ')

        if back.lower() == 'y':
            continue
        else:
            break
    else:
        print('Invalid Input')
    break

