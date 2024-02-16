login = input('Login: ')
pswrd = input('Password: ')
print('\nYour login: ', login, '\nYour password: ', pswrd)
pswrd_new = input('\nEnter a New Password: ')

if pswrd_new != pswrd: print('\nUser', login, 'has changed the password to', pswrd_new)
else: print('\nThe password has not changed.')