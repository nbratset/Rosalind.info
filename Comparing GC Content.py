import numpy as np

filename=input('Input FASTA filename here:')
bigdict={}
lastheader=''
resultsDict={}

#Super Basic Fasta reader
for line in open(filename):
    if '>' in line:
        rows=line.rstrip().split('>')
        if rows[1] not in bigdict:
            bigdict[rows[1]]=''
            lastheader=rows[1]

        elif rows[1] in bigdict:
            lastheader-rows[1]
            pass
    else: 
        seq=line.rstrip().upper()
        bigdict[lastheader]+=seq

for key in bigdict:
    basecount={'A':0,'C':0,'T':0,'G':0,'U':0}
    length=len(bigdict[key])

    for i in np.arange(0,length):
        if bigdict[key][i] in basecount:
            basecount[bigdict[key][i]]+=1

    GCs=basecount['G']+basecount['C']
    GCcontent=float(GCs)/float(length)
    resultsDict[GCcontent]=key

highestGC=max(resultsDict)

print(resultsDict[highestGC])
print(format(highestGC*100,".6f"))