def get_min_and_max_words(sentense):
    words = sentense.split(" ") # type: ignore
    min_word = min(words, key=len)
    max_word = max(words, key=len)
    
    return (min_word, max_word)

def get_min_and_max_words_sorted(sentense):
    words = sentense.split(" ")
    min_word, max_word = get_min_and_max_words(sentense)
    
    all_min_words = [w for w in words if len(w) == len(min_word)]
    all_max_words = [w for w in words if len(w) == len(max_word)]
    
    all_min_words.sort()
    all_max_words.sort()
    
    return all_min_words[0], all_max_words[0]

s = "Un qq sachant chasser sait chasser sans son chien"

min_word, max_word = get_min_and_max_words_sorted(s)

print("Mot le plus petit:", min_word)
print("Mot le plus long:", max_word)