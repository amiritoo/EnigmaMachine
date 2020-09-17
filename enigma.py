import pickle
import os.path


alpha="abcdefghijklmnopqrstuvwxyz"

def read_config(date):
    with open("./{}-config.enig".format(date),"rb") as file:
        rotor_one,rotor_two,rotor_three = pickle.load(file)
    return rotor_one  , rotor_two , rotor_three

def code_decode_enigma(each):


    out_rotor_one= rotor_one[alpha.find(each)]
    out_rotor_two= rotor_two[alpha.find(out_rotor_one)]
    out_rotor_three= rotor_three[alpha.find(out_rotor_two)]

    out_reflector = refl(alpha , out_rotor_three)

    back_out_three= alpha[rotor_three.find(out_reflector)]
    back_out_two= alpha[rotor_two.find(back_out_three)]
    back_out_one= alpha[rotor_one.find(back_out_two)]

    return back_out_one


def refl(alpha, out_rotor_three):
    for letter in alpha:
        if letter == out_rotor_three:
            out_reflector= (alpha[(alpha.find(letter) +1) * -1])
    return out_reflector

def rotor_shift(state_rotor):

    global rotor_one , rotor_two , rotor_three

    rotor_one = rotor_one[-1] + rotor_one[:-1]
    if state_rotor == 26:
        rotor_two = rotor_two[-1] + rotor_two[:-1]
    if state_rotor == 26*26:
        rotor_three = rotor_three[-1] + rotor_three[:-1]

def primary_state(primary_rotors_state):
    global rotor_one , rotor_two , rotor_three
    state_rotor_one = primary_rotors_state.split()[0]
    state_rotor_two = primary_rotors_state.split()[1]
    state_rotor_three = primary_rotors_state.split()[2]

    while rotor_one[0]!=state_rotor_one:
        rotor_one = rotor_one[-1] + rotor_one[:-1]

    while rotor_two[0]!=state_rotor_two:
        rotor_two = rotor_two[-1] + rotor_two[:-1]

    while rotor_three[0]!=state_rotor_three:
        rotor_three = rotor_three[-1] + rotor_three[:-1]



if __name__ == "__main__":

    state_rotor = 0

    while True:
        date = input("Enter ur date same as YYYY-MM-DD: ")
        if os.path.isfile("./{}-config.enig".format(date)):
                
            primary_rotors_state = input("Enter three primary rotors states: ")



            rotor_one , rotor_two , rotor_three = read_config(date)
            while True:
                text = input('Enter message: ')
                coded = ''
                primary_state(primary_rotors_state)
                for each in text:
                    
                    coded += code_decode_enigma(each)
                    rotor_shift(state_rotor)
                    state_rotor = state_rotor + 1

                print(coded)
        else :
            print('Enter correct enigma machine config file.')