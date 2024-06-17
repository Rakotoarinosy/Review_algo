import subprocess
import os

while True:
    cmd = input(f"{os.getcwd()} > ")
    if cmd == "exit":
        break
    
    commande_split = cmd.split(" ")
    if len(commande_split) == 2 and commande_split[0] == "cd":
        try:
            os.chdir(commande_split[1])
        except FileNotFoundError:
            print("ERREUR : Dir not found")
    else:
        resultat = subprocess.run(cmd,capture_output=True,universal_newlines=True,shell=True)
        print(resultat.stdout)
        print(resultat.stderr)
