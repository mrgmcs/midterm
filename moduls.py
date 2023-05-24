import random

user_data = "welcome to our world"
alphas = "abcdefghijklm01234 nopqrstuvwxyz56789/"
#         lxwd/f7kvus 54tpiny902q13mcrhjage6bzo8
shuffled = "".join(random.sample(alphas, len(alphas)))


#print(shuffled)
#shuffled= "".join(random.shuffle(user_data, len(user_data)))
#print(shuffled, user_data)
# sybmol = " !@#$%^&*()_+}{?><[] "
# number = "12345 67890"

def encryption2(data, shuffle):
    data_en = ""
    for item in range(len(data)):
        info = alphas.index(data[item])
        data_en += shuffle[info]

    return data_en
def decryption2(data, shuffle):
    data_de = ""
    for item in range(len(data)):
        info = shuffle.index(data[item])
        data_de += alphas[info]
    return data_de


