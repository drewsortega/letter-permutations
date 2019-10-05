import sys
import os

# determine whether or not each input is nummeric
def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

# recursive permute function which uses N to track how many characters remaining to permute
def permute(N, L):
    # enpty array to store results
    result = []
    if N == 1:
        # if N = 1, L is our base case so return L instead of result.
        return L.copy()

    # loop over values in L
    for i, l in enumerate(L):

        # get all permutations from lower levels
        subperm = permute(N-1, L)

        #loop over values in subperm
        for j in range(0,len(subperm)):

            # append the current letter to the beginning of the subperm
            subperm[j] = l + subperm[j]

        #add the subperm list to the result list
        result += subperm

    # return overall result
    return result


if len(sys.argv) != 3 or not is_int(sys.argv[1]) or not os.path.exists(sys.argv[2]):
    print("Error: format: permutations.py [WORD LENGTH] [INPUT_CHARACTERS.txt]")
    exit(1)
input_letters_filepath = sys.argv[2]
word_length = int(sys.argv[1])

input_letters = []

if word_length < 1:
    print("Error: word length must be >= 1.")
    exit(1)

print("input file:\t{}".format(input_letters_filepath))
print("word length:\t{}".format(word_length))

with open(input_letters_filepath) as input_letters_file:
    print("\nreading from file...")

    input_letters = list(map(lambda s: s.strip(), input_letters_file.readlines()))

    print("read letters:", end="\t")
    print(*input_letters)

    for letter in input_letters:
        if len(letter) != 1 or not letter.isalpha():
            print("Error: input file must contain lines with single letters only")
            exit(1)

    output_file = open("permutations.csv", "w")

    for word in permute(word_length, input_letters):
        output_file.write(word + ",\n")

print()
print("done! \noutput:\t\tpermutations.csv") 
