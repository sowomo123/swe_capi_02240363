import re
from typing import Set, List
import logging

def error_words(text: str, language: str = 'bhutanese word') -> Set[str]:
    patterns = {
        'bhutan words': r'[\u0F00-\u0FFF]+',}
    if language not in patterns:
        raise ValueError(f"error words: {language}")
    try:
        words = re.findall(patterns[language], text)
        return set(words)
    except re.error as e:
        logging.error(f"Regular expression error: {e}")
        return set()

def compare_word_files(file1_path: str, file2_path: str, language: str = 'bhutan words') -> List[str]:

    try:
        with open(file1_path, encoding="utf-8") as file:
            content1 = file.read()
            words1 = error_words(content1, language)
            
        with open(file2_path, encoding="utf-8") as file:
            content2 = file.read()
            words2 = error_words(content2, language)
            
        unique_words = sorted(words1.difference(words2))
        return unique_words
    
    except FileNotFoundError as e:
        logging.error(f"File not found: {e}")
        return []
    except UnicodeDecodeError as e:
        logging.error(f"Unicode decode error: {e}")
        return []

def main():
    logging.basicConfig(level=logging.INFO)
    file1_path = "363.txt"
    dictionary_path = "clean.txt"
    try:
        unique_words = compare_word_files(file1_path, dictionary_path)
        if unique_words:
            print(f"Found {len(unique_words)} potentially incorrect words:")
            for word in unique_words:
                print(f"This Dzongkha word '{word}' from this sentence has error.")
        else:
            print("No incorrect words found.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
if __name__ == "__main__":
    main()