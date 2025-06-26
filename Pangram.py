def is_pangram(sentence):
    count = {key:0 for key in "qwertyuiopasdfghjklzxcvbnm"}
    for letter in sentence:
        lowered = letter.lower()
        if lowered in "qwertyuiopasdfghjklzxcvbnm":
            count[lowered] += 1
    print(count)
    return not (0 in count.values())

print(is_pangram("The quick brown fox jumps over the lazy dog."))
        
