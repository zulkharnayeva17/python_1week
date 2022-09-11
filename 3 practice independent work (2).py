#task 1
def is_alive(health):
    if health <= 0:
        return False
    else:
        return True
    # checking
print(is_alive(5))
print(is_alive(-4))

 #task 2
months = {
    1: 'january',
    2: 'february',
    3: 'march',
    4: 'april',
    5:  'may',
    6: 'june',
    7: 'july',
    8: 'august',
    9: 'september',
    10: 'october',
    11: 'november',
    12: 'december'}
def season(number_of_month):
   if not isinstance(number_of_month, int) and 1 <= number_of_month <= 12:
        print('You need to enter the real number of the month')
  
   if number_of_month in range(3, 6):
    print(f'You were born in {months[number_of_month]}. Birds sang beautiful songs')
   elif number_of_month in range(6, 9):
           print(f'You were born in  {months[number_of_month]}. The sun shone brighter than ever')
   elif number_of_month in range(9, 12):
     print(f'you were born in {months[number_of_month]}. the harvest was incredible')
   else:
        print(f'you were born in  {months[number_of_month]}. white snow fell outside the window')
season (1)
season(4)
season(7)
season(10)

#task 3
import string
def check_pass(pswd):
 error = {
        'length': 'The password length is not equal to 8 characters',
        'upper': 'Upper letters are missing',
        'lower': 'There are no lowercase letters in the password',
        'digits': 'There are no numbers in the password',
        'spec': 'There are no special characters in the password',
        'unintended_symbols': 'The password uses unintended characters'
    }

 if len(pswd) == 8:
     error.pop('length')

 pswd_reduced = [symbol for symbol in pswd]

 for symbol in pswd:
        if symbol in string.ascii_uppercase:
            pswd_reduced.remove(symbol)
            error.pop('upper', None)
        elif symbol in string.ascii_lowercase:
            pswd_reduced.remove(symbol)
            error.pop('lower', None)
        elif symbol in string.digits:
            pswd_reduced.remove(symbol)
            error.pop('digits', None)
        elif symbol in '*-#':
            pswd_reduced.remove(symbol)
            error.pop('spec', None)

 if len(pswd_reduced) == 0:
        error.pop('unintended_symbols')

 if len(error) == 0:
        print('this password is perfect')
 else:
        print(*error.values(), sep='; ')


# checking
check_pass('98Tt#*Yf')
check_pass('@#@khb')
check_pass('6#2@@')
check_pass('qwerty')
check_pass('dfghj')
