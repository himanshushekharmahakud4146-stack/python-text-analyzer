"""
Text Analyzer Project

Version 1:
Basic text analyzer that counts total words, unique words, 
and the most frequent word.

Version 2:
Improved version with stopword filtering, text cleaning,
top frequent words, and export to file.

This project is part of my Python learning journey.
"""

# ============================================
# TEXT ANALYZER PROJECT
# Version 1 – Basic Text Analyzer
# ============================================

# Features:
# 1. Count total number of words
# 2. Count number of unique words
# 3. Find most frequent word

class Solution:
    def text_analyzer(self, text):

        # convert text to lowercase for uniform comparison
        text = text.lower()

        # split text into words
        words = text.split()

        counts = {}

        # if input text is empty
        if not words:
            return 0, 0, None

        # count frequency of each word
        for word in words:
            counts[word] = counts.get(word, 0) + 1

        # calculate statistics
        total_words = len(words)
        unique_words = len(counts)
        most_frequent_words = max(counts, key=counts.get)

        return total_words, unique_words, most_frequent_words


# ===== Run Version 1 =====

text = input("Enter a text: ")

s = Solution()
total, unique, frequent = s.text_analyzer(text)

print("Total words:", total)
print("Unique words:", unique)
print("Most frequent word:", frequent)

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

