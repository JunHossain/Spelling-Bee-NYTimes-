import random
import string


def load_words():
    with open('words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())
    return valid_words


valid_words = load_words()
found_words = []


def generate_random_letters(n=7):
    excluded_letters = ['q', 'x', 'v', 'y', 'z']
    vowels = ['a', 'e', 'i', 'o', 'u']
    consonants = [
        letter for letter in string.ascii_lowercase if letter not in excluded_letters + vowels]
    letters = random.sample(vowels, k=random.choice([2, 3]))
    letters.extend(random.sample(consonants, k=7-len(letters)))
    return random.sample(letters, k=n)


def is_word_valid(word, random_letters, central_letter):
    if (len(word) < 4):
        return "Too Short"
    for letter in word:
        if letter not in random_letters:
            return "Bad Word"
    if word not in valid_words:
        return "Not in Word List"
    if central_letter not in word:
        return "Missing Center Letter"
    if word in found_words:
        return "Already Found"
    found_words.append(word)
    return "Good"


def check_stats():
    print(f"Your random letters are: {random_letters}")
    print(f"Your central letter is: {central_letter}")
    print(f"Your current points are: {points}")


random_letters = generate_random_letters()
random_letters = list(random_letters)
print('Your random letters are:', random_letters)

central_letter = random.choice(random_letters)
print('Your central letter is:\t', central_letter)

print("Your game starts now. Make sure to use lowercase letters only.\nType 'CHECK' to check the letters again.\nType 'EXIT' to end the game.\nType 'NEW' to start a new game.")

points = 0
fail_message = {
    "Too Short": "Too short",
    "Missing Center Letter": "Missing center letter",
    "Bad Word": "Bad word",
    "Not in Word List": "Not in word list",
    "Already Found": "Already found",
}

while True:
    current_word = str(input('Enter a word: '))

    if current_word == "EXIT":
        exit(0)
    if current_word == "CHECK":
        check_stats()
        continue
    if current_word == "NEW":
        points = 0
        print("Starting a new game.")
        random_letters = generate_random_letters()
        random_letters = list(random_letters)
        print('Your random letters are:', random_letters)

        central_letter = random.choice(random_letters)
        print('Your central letter is:\t', central_letter)
        continue

    result = is_word_valid(current_word, random_letters, central_letter)
    if result == "Good":
        if len(current_word) == 4:
            points += 1
            print("+1")
        elif (set(random_letters).issubset(set(current_word))):
            points += len(current_word) + 7
            print("You found a pangram! Bonus 7 points")
            print(f"+{len(current_word) + 7}")
        else:
            points += len(current_word)
            print(f"+{len(current_word)}")
    else:
        print(fail_message[result])
