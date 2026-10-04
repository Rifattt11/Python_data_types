text = input("Введите текст: ").lower().split()
words = [w.strip('.,!?;:"()-') for w in text]
words = [w for w in words if w]

word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

sorted_words = sorted(word_count.items(), key=lambda item: item[1], reverse=True)

for word, count in sorted_words[:5]:
    print(word, count)