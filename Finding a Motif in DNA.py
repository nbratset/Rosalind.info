s=input("Sequence: ").upper()
t=input("Motif: ").upper()

results=[]

for i in range(0,len(s)):
    if s[i:i+len(t)] == t:
        results.append(i+1)
print(*results)