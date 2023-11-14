import nltk
from nltk import bigrams
from nltk.probability import FreqDist

nltk.download('punkt')

def load_text_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

# Зазначте шлях до вашого файлу
file_path = 'text.txt'

# Завантаження тексту із файлу
text = load_text_from_file(file_path)

# Токенізація тексту
words = nltk.word_tokenize(text)

# Визначення біграм
bi_grams = list(bigrams(words))

# Обчислення частот біграм
freq_bi_grams = FreqDist(bi_grams)

def generate_message(seed_word, num_words=6):
    message = [seed_word]
    current_word = seed_word

    for _ in range(num_words - 1):
        # Вибір біграм, що починається поточним словом
        next_words = [word[1] for word in freq_bi_grams if word[0] == current_word]
        
        if next_words:
            next_word = next_words[0]
            message.append(next_word)
            current_word = next_word
        else:
            break

    return ' '.join(message)

# Введене слово для генерації повідомлення
user_input = input("Введіть слово: ")
generated_message = generate_message(user_input)

print(f"Згенероване повідомлення: {generated_message}")
