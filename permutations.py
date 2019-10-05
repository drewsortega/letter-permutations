import sys
import os
import os.path
def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
def permute(N, L):
    result = []
    if N == 1:
        return L
    for i, l in enumerate(L):
        subperm = permute(N-1, L.copy())
        for j in range(0,len(subperm)):
            subperm[j] = l + subperm[j]
        result += subperm
    return result

if len(sys.argv) != 3 or not is_int(sys.argv[1]) or not os.path.exists(sys.argv[2]):
    print("Error: format: permutations.py [WORD LENGTH] [INPUT_CHARACTERS.txt]")
    exit()
input_letters_filepath = sys.argv[2]
print("input file:", input_letters_filepath, end="\t\n")
input_letters = []
word_length = int(sys.argv[1])
print("word length:", word_length, end="\t\n")
with open(input_letters_filepath) as input_letters_file:
    print("\nreading from file...")
    input_letters = list(map(lambda s: s.strip(), input_letters_file.readlines()))
    print("read letters:", end="\t")
    print(*input_letters)
    for letter in input_letters:
        if len(letter) != 1 or not letter.isalpha():
            print("Error: input file must contain lines with single letters only")
            exit()
    output_file = open("permutations.csv", "w")
    for word in permute(word_length, input_letters):
        output_file.write(word + ",\n")
print("done! output: permutations.csv") 
