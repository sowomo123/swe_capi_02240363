import re

def extract_words(text):
    
    words = re.findall(r'[\u0F00-\u0FFF]+', text)
    return set(words)  

with open("363.txt", encoding="utf-8") as file:
    content1 = file.read()
    word1 = extract_words(content1)

with open("clean.txt", encoding="utf-8") as file:
    content2 = file.read()
    word2 =extract_words(content2)

unique_to_file1 = word1.difference(word2)  

for word in unique_to_file1:
    print(f"The word '{word}' from this sentence is incorrect.")

#(some of the code used from chat gpt)