def count_words(text):
    """Count words in a given text"""
    words = text.lower().split()
    
    word_count = {}
    
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    return word_count

def main():
    print("Enter some text to count words:")
    text = input()
    
    result = count_words(text)
    
    print(f"\nTotal words: {sum(result.values())}")
    print(f"Unique words: {len(result)}")
    print("\nWord frequencies:")
    
    for word, count in result.items():
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()