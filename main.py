class Solution:
    def text_analyzer(self,text ):
        text = text.lower()
        words = text.split()
        counts = {}


        if not words:
                return 0, 0, None


        for word in words:
                counts[word] = counts.get(word,0)+1

        total_words = len(words)
        unique_words = len(counts)
        most_frequent_words = max(counts,key = counts.get)

        return total_words,unique_words,most_frequent_words

text = input("Enter a text: ")
s = Solution()
total, unique, frequent =s.text_analyzer(text)

print ('Total words: ',total)
print ('Unique words: ',unique)
print("Most frequent word: ",frequent)


# ==============================
# Text Analyzer - Version 2
# Improvements:
# - Ignore stopwords
# - Show top 5 frequent words
# - Export results to file
# ==============================

# Step 1: input text
text = input("Enter text: ").lower()

# Step 2: stopwords list
stopwords = {"a", "the", "is", "and", "to", "of", "in", "on"}

# Step 3: remove punctuation
clean_text = ""
for ch in text:
    if ch.isalpha() or ch == " ":
        clean_text += ch

# Step 4: split into words
words = clean_text.split()

# Step 5: count frequency (ignoring stopwords)
freq = {}

for word in words:
    if word not in stopwords:
        freq[word] = freq.get(word, 0) + 1

# Step 6: sort by frequency (descending)
sorted_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)

# Step 7: top 5 words
top_5 = sorted_words[:5]

# Step 8: print result
print("Top 5 words:")
for word, count in top_5:
    print(word, count)

# Step 9: export to file
with open("output.txt", "w") as f:
    for word, count in top_5:
        f.write(f"{word} : {count}\n")

print("Result saved to output.txt")}\n")

