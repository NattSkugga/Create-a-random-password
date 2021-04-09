import random 

def GetPassword(data):
    Max_of_digits = 6                              # here yor can change the length of passwords
    password = ""
    while len(password) != Max_of_digits:
        value = random.choice(data)
        password += value
    return password

data = '@£%1234567890qwertyuiopasdfghjklmnbvcxz'
for i in range(2):                                 # here yor can change the number of passwords
    print(GetPassword(data))
