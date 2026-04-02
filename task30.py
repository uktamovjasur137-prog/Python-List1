words = ["alla", "olma", "kiyik", "ona", "lola"]

palindrom = []

for word in words:
    if word[::-1] == word:
        palindrom.append(word)

print(palindrom)