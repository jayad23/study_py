import random

options = {"piedra": 0, "papel": 1, "tijera": 2}
values = ["piedra", "papel", "tijera"]
machine_wins = 0;
user_wins = 0;

def getMachineSelection():
  x = random.randint(0, 2)
  selection = options[values[x]]
  return selection

def getUserSelection(value):
  selection = options[value];
  return selection;

def reStartTheGame():
  want_to = input("¿Jugar otra vez? ").lower();
  if(want_to == "yes" or want_to == "si" or want_to == "y"):
    Game();
  else:
    print("Fue una buena ronda!");
  return;


def Game():
  global machine_wins;
  global user_wins;
  
  machine_selection = getMachineSelection()
  input_val = input("Piedra, Papel, ó Tijera... Choose: ").lower()
  if input_val in values:
    user_selection = getUserSelection(input_val);
    if user_selection > machine_selection:
      user_wins = user_wins + 1;
      print(
        f"Ganas porque {values[user_selection]} vence a {values[machine_selection]}; Máquina {machine_wins} - Usuario: {user_wins}"
      )
    elif user_selection == machine_selection:
      print(
        f"Empate. Ambos han seleccionado {values[machine_selection]} y {values[user_selection]}; Máquina {machine_wins} - Usuario: {user_wins}"
      )
    else:
      machine_wins = machine_wins + 1;
      print(
        f"Gana la máquina porque {values[machine_selection]} vence a {values[user_selection]}; Máquina {machine_wins} - Usuario: {user_wins}"
      )
  else:
    print("El valor no existe!")

  reStartTheGame();
  return;
Game()
