# Task 1
def count_word_frequencies(text):

    text = text.lower()
    text = text.replace('.', '').replace(',', '').replace('!', '').replace('?', '')

    words = text.split()

    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count

text = "Hello world! Hello everyone. Welcome to the world of Python."
print(count_word_frequencies(text))

# Task 2

def translate():
    translations = {'hello': 'привіт', 'goodbye': 'до побачення', 'cat': 'кіт', 'dog': 'собака'}
    print(f"The translation of '{(word:=input('Enter a word to translate: ').lower())}' /n "
          f"is '{translations.get(word, f'Sorry, the word \'{word}\' is not in the dictionary.')}'.")

if __name__ == "__main__":
    translate()


# Task 4

exchange_rates = {"USD": 1.0, "EUR": 0.85, "UAH": 42.0}

def currency_converter(amount, from_currency, to_currency):
    if from_currency not in exchange_rates or to_currency not in exchange_rates:
        return "Невідома валюта."
    return round((amount / exchange_rates[from_currency]) * exchange_rates[to_currency], 2)

print(currency_converter(100, "USD", "EUR"))
print(currency_converter(50, "EUR", "USD"))
print(currency_converter(1000, "UAH", "USD"))


