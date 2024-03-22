"""x = input("user input ")
stri = ""
for i in x:
    if i.isupper():
        stri += i.lower()
    elif i.islower():
        stri += i.upper()
print(stri)
x = input("Enter a string")
y = "AEIOUaeiou"
res = ""
for k in x:
    if k not in y:
        res += k
print(res)
x = int(input("Enter a number"))

seq = "ATGTACTC ATTCGTTTCG GAAGAGACAG GTACGTTAAT AGTTAATAGC GTACTTCTTT TTCTTGCTTCGTGGTATTC TTGCTAGTTA CACTAGCCAT CCTTACTGCG CTTCGATTGT GTGCGTACTG CTGCAATATT GTTAACGTGA GTCTTGTAAA ACCTTCTTTT TACGTTTACT CTCGTGTTAA AAATCTGAAT TCTTCTAGAG TTCCTGATCT TCTGGTCTAA"
count = 0
seq1 = ""
seq1 = seq[::-1]
for i in range(len(seq1)-4):
    if seq1[i:i+5] == "TTACT":
        count += 1"""
seq = "ATGTACTC ATTCGTTTCG GAAGAGACAG GTACGTTAAT AGTTAATAGC GTACTTCTTT TTCTTGCTTCGTGGTATTC TTGCTAGTTA CACTAGCCAT CCTTACTGCG CTTCGATTGT GTGCGTACTG CTGCAATATT GTTAACGTGA GTCTTGTAAA ACCTTCTTTT TACGTTTACT CTCGTGTTAA AAATCTGAAT TCTTCTAGAG TTCCTGATCT TCTGGTCTAA"
count = 0
seq = seq.replace(" ", "")
seq1 = seq[::-1]

for i in range(len(seq1)):  # Iterate through the entire reversed sequence
  if seq1[i:i+5] == "TTACT":
    count += 1

print("Number of occurrences of 'TTACT' in the reversed sequence:", count)

