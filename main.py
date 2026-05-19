import random


def play_game():
    secret_number = random.randint(1, 100)
    attempts = 0

    print("Välkommen till gissa talet!")
    print("Jag tänker på ett tal mellan 1 och 100.")

    while True:
        try:
            guess = int(input("Skriv din gissning: "))
            attempts += 1

            if guess < secret_number:
                print("För lågt!")
            elif guess > secret_number:
                print("För högt!")
            else:
                print("Rätt!")
                print(f"Du klarade det på {attempts} försök.")
                break

        except ValueError:
            print("Du måste skriva ett heltal.")


play_game()
