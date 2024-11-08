import random

#Parametros public: numero primo e base
p = 23
g = 5 

def generate_keys():
    private_key = random.randint(1, p -1)
    public_key = (g ** private_key) % p

    return private_key, public_key

def calculate_shared_key(ther_public, my_private):
    shared_key = (ther_public ** my_private) % p
    return shared_key
