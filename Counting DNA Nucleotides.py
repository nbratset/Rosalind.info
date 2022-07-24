'''
Problem:
    A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; the length of a string is the number of symbols that it contains.
    An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."
    Given: A DNA string s of length at most 1000 nt.
    Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.
'''

keyMap={'A':0,'C':0,'G':0,'T':0}
inputSeq=input("Paste DNA Sequence Here: ")

for base in inputSeq.upper(): #I make everything capital here just in case there are lowercase bases in the sequence
    if base in keyMap:
        keyMap[base]+=1

print(keyMap['A'], keyMap['C'],keyMap['G'],keyMap['T'])