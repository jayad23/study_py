import subprocess
with open("texto.txt", "r") as fp:
    for i, line in enumerate(iter(fp.readline, '')):
        subprocess.run(["say", line])
