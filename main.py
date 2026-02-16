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

        

