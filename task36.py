words = ["nok", "olma", "qovun", "mandarin", "xurmo"]

max_len = ""

for word in words:
    if len(word) > len(max_len):
        max_len = word

print(max_len)