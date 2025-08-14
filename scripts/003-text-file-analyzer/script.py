def analyze_file(filename):
    lines = 0
    words = 0
    characters = 0

    with open(filename, 'r', encoding='utf-8') as f: 
        for line in f:
            lines += 1
            words += len(line.split())
            characters += len(line)

    return lines, words, characters

# Example

file_path = './samples/canine_breeds.txt'
lines, words, characters = analyze_file(file_path)
print(f"Lines: {lines}")
print(f"Words: {words}")
print(f"Characters: {characters}")