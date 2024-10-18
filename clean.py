
def clean_text(input_file, output_file):
    cleaned_words = []
    with open(input_file, 'r', encoding='utf-8') as file:
        #To read a file line by line  used a for loop to iterate over the file object.
        for line in file:
            #Python String split() method splits a string into a list of strings after breaking the given string by the specified separator.
            words = line.split()
            if words:
                dzongkha_word = words[0]
                cleaned_words.append(dzongkha_word)
    with open (output_file ,'w', encoding="utf-8") as file:
        for words in cleaned_words:
            file.write(words + "\n")
        print(f"cleaned words saved to {output_file}")
input_file = "dzo.txt"
output_file = "clean.txt"
clean_text(input_file, output_file)           