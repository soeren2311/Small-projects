import random

# Initialisiere die Punktzahlen und die Rundennummer
player1_score = 0
player2_score = 0
round_number = 1

# Schleife, die solange läuft, bis ein Spieler 10 Punkte erreicht hat
while player1_score < 15 and player2_score < 15:
  # Warte auf Eingabetaste
  input("Drücke Enter, um Runde {} zu starten".format(round_number))

  # Würfel eine Zufallszahl für beide Spieler
  player1_roll = random.randint(1, 6)
  player2_roll = random.randint(1, 6)

  # Füge den gewürfelten Wert dem aktuellen Spieler hinzu, falls der Wurf nicht 0 ist
  ## Addiere plus 3 bei einer 6 und plus 3 bei einer 1
  if player1_roll == 6:
    player1_roll += 3
  player1_score += player1_roll
  if player2_roll == 1:
    player2_roll += 3
  player2_score += player2_roll

  # Erhöhe die Rundennummer
  round_number += 1

  # Ausgabe der aktuellen Punktzahlen und der gewürfelten Werte
  print("Gewürfelter Wert von Spieler 1:", player1_roll)
  print("Gewürfelter Wert von Spieler 2:", player2_roll)
  print(f"Spieler 1 hat: {player1_score} Punkte")
  print(f"Spieler 2 hat: {player2_score} Punkte")


# Ermittle den Gewinner
if player1_score >= 15 and player1_score > player2_score and player2_score < 15:
  print("Spieler 1 hat gewonnen!")
if player2_score >= 15 and player2_score > player1_score and player1_score < 15:
  print("Spieler 2 hat gewonnen!")
