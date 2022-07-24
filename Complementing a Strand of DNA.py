basePairs={'A':'T','T':'A','C':'G','G':'C'}
dna=input('Paste DNA sequence here: ')
revComp=''
for base in reversed(dna.upper()):
    if base in basePairs:
        revComp+=basePairs[base]
print(revComp)