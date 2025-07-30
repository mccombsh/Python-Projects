plaintext = input("Plaintext: ").upper().replace(" ", "")
keyword = input("Keyword: ").upper()
resulttext = ""
char = ''

for i, char in enumerate(plaintext):
    resulttext += chr((ord(char) - 65 + ord(keyword[i % len(keyword)]) - 65) % 26 +65)

print(resulttext)