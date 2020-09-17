import random
import pickle
import datetime





today = datetime.date.today()
print (today)
alpa="abcdefghijklmnopqrstuvwxyz"

rotor_one= list(alpa)
rotor_one_str= ""
random.shuffle(rotor_one)
for letter in rotor_one:
    rotor_one_str= rotor_one_str + letter

rotor_two= list(alpa)
rotor_two_str= ""
random.shuffle(rotor_two)
for letter in rotor_two:
    rotor_two_str= rotor_two_str + letter

rotor_three= list(alpa)
rotor_three_str= ""
random.shuffle(rotor_three)
for letter in rotor_three:
    rotor_three_str= rotor_three_str + letter

with open("./{}-config.enig".format(today),"wb") as file:
    pickle.dump((rotor_one_str,rotor_two_str,rotor_three_str),file)
print(rotor_two_str)
print(rotor_three_str)


