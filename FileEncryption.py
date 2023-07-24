# Define dictionary

codes = {
    'A': '%', 'B': '@', 'C': '#', 'D': '!', 'E': '1',
    'F': '2', 'G': '3', 'H': '4', 'I': '5', 'J': '6',
    'K': '7', 'L': '8', 'M': '9', 'N': '0', 'O': '$',
    'P': '^', 'Q': '&', 'R': '*', 'S': '(', 'T': ')',
    'U': '-', 'V': '+', 'W': '=', 'X': '/', 'Y': '\\',
    'Z': '|', 'a': 'q', 'b': 'w', 'c': 'e', 'd': 'r',
    'e': 't', 'f': 'y', 'g': 'u', 'h': 'i', 'i': 'o',
    'j': 'p', 'k': 'a', 'l': 's', 'm': 'd', 'n': 'f',
    'o': 'g', 'p': 'h', 'q': 'j', 'r': 'k', 's': 'l',
    't': 'z', 'u': 'x', 'v': 'c', 'w': 'v', 'x': 'b',
    'y': 'n', 'z': 'm'
}

# Get input from the user

encrypted_str=""
f1 = open('info_security-1.txt', "r")
f2 = open('encrypted.txt','w')

for char in f1:
    if char in codes:
        encrypted_str += codes[char]
    else:
        encrypted_str += char

# Display the encrypted string to the user
f2.write(encrypted_str)
f2.close()

#open and read the file after the overwriting:
f2 = open('encrypted.txt','r')
