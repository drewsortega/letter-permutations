# letter-permutations
Small project for WAW
Gets all permutations of a set of letters based on input and length.

## Installing

### Option 1:

```bash
git clone https://github.com/drewsortega/letter-permutations.git
```

### Option 2:

Download permutations.py directly:
```bash
wget https://github.com/drewsortega/letter-permutations/blob/master/permutations.py
```

### Option 3:

Download permutations.py directly in a zip file:
https://github.com/drewsortega/letter-permutations/archive/master.zip

## Usage

1. Create a .txt file with individual letters on each line for characters to permutate over.
2. run permutations.py in any terminal where python3 is accessible.
```bash
$ python3 permutations.py <WORD_LENGTH> <INPUT_FILE.txt>
```

### Examples

input.txt:
```
a
b
c
d
e
```
terminal:
```bash
$ python3 permutations.py 3 input.txt    

input file: input.txt	
word length: 3	

reading from file...
read letters:	a b c d e
done! output: permutations.csv
```

;)
