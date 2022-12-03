# Quiz game for a partyevening

questions = ("Frage 1: Wie viele Zeitzonen gibt es in Russland?: ",
             "Frage 2: Was ist die nationale Blume Japans?: ",
             "Frage 3: Wann begann der 30jährige Krieg?: ",
             "Frage 4: Welches Land hat die meisten Inseln der Welt?: ",
             "Frage 5: Der wie vielte Präsdient der vereinigten Staaten von Amerika war George W. Bush?: ",
             "Frage 6: Welcher Planet liegt am nächsten zur Sonne?: ",
             "Frage 7: Wann wurde die Londoner U-Bahn eröffnet?: ",
             "Frage 8: Welchen Spitznamen trug der in Mönchengladbach geborene Fußballer Horst-Dieter Höttges?: ",
             "Frage 9: Wie lange braucht das Licht in etwa von der Sonne bis zur Erde?: ",
             "Frage 10: Wie nennt man die Wissenschaft und Lehre von der Führung eines Schiffes?: ")

options = (("A. 6", "B. 7", "C. 9", "D. 11"),
           ("A. Tulpe", "B. Rose", "C. Kirschblüte", "D. Orchideen"),
           ("A. 1618", "B. 1718", "C. 1848", "D. 1900"),
           ("A. Finnland", "B. Indonesien", "C. Griechenland", "D. Schweden"),
           ("A. 39", "B. 41 ", "C. 43", "D. 44"),
           ("A. Mars", "B. Merkur ", "C. Venus", "D. Erde"),
           ("A. 1817", "B. 1846 ", "C. 1863", "D. 1896"),
           ("A. Titan", "B. Eisenfuß ", "C. Turbo", "D. Windhund"),
           ("A. 8 Sekunden", "B. 8 Minuten ", "C. 8 Stunden", "D. 8 Tage"),
           ("A. Keltik", "B. Statik ", "C. Kinetik", "D. Nautik"))

answers = ("D", "C", "A", "D", "C", "B", "C", "B", "B", "D")
guesses = []
score = 0
quest_num = 0

for question in questions:
    print("........................................")
    print(question)
    for option in options[quest_num]:
        print(option)

    guess = input("Enter A, B, C, D: ").upper()
    guesses.append(guess)
    if guess == answers[quest_num]:
        score += 1
        print("Richtig!")
    else:
        print("Falsch!")
        print(f"{answers[quest_num]} ist die richtige Antwort")

    quest_num += 1


print("...........................")
print("   Dein ERGEBNIS lautet    ")
print("...........................")

print("Korrekte Antworten: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("   Deine Antworten: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

# add something new to the script

score = int(score / len(questions) * 100)
if score < 30:
    print("Du bist wirklich extrem ungebildet. Schäm dich!!!")
elif score>=30 and score<50:
    print("Gut ist anders! In der Schule nicht aufgepasst, was?")
elif score>=50 and score<70:
    print("Das war ganz okay. Aber immer noch bei weitem nicht gut")
elif score>=70 and score<100:
    print("Gut. Bilde Dir aber bloß nichts drauf ein!!")
else:
    print("Weltklasse. Einfach nur Weltklasse!!!")
print(f"{score} % Richtige Antworten")

