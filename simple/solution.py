import string
from collections import Counter
from cipher_solver.simple import SimpleSolver

with open('flag.txt') as f:
#    ctext = f.read().strip().replace(' ', '')
    stext = f.read().strip()

# performing frequency analysis - not exactly needed, but can see trigrams are more
# confirms it's a substitution cipher

#def chunks(l, n):
#    n = max(1, n)
#    return [l[i:i+n] for i in range(0, len(l), n)]


# breaking chars into groups of different sizes and looking at the size of the set
#for i in range(1,10):
#    unique = len(set(chunks(ctext, i)))
#    print(f"{unique} unique groups when split into groups of length {i}")

# breaking into trigrams
#chunked = chunks(ctext, 3)
#freq = Counter(chunked).most_common()
#print(freq)


# solving the ciphertext divided into trigrams
#print("Decrypted cipher with trigrams") 
#s = SimpleSolver(ctext)
#s.solve()
#pstext = s.plaintext()
#print(pstext)

# since it doesn't make sense, continue with the normal text
# solving the given ciphertext directly 
s = SimpleSolver(stext)
s.solve()
pctext = s.plaintext()
print(pctext)

# after minor obvious changes in substitution, 
# the last line of the txt is: The flag is SctfEsubstitutionciphersE
# flag is: sctf{substitution_ciphers} 
