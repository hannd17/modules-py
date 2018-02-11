def convert(word):
    codes = [".-", "-...", "-.-.",
             "-..", ".", "..-.",
             "--.", "....", "..",
             ".---", "-.-", ".-..",
             "--", "-.", "---",
             ".--.", "--.-", ".-.",
             "...", "-", "..-",
             "...-", ".--", "-..-",
             "-.--", "--..", " "]
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    output = []
    for x in word:
        output.append(codes[alphabet.index(x)])
    print(output)

convert(input("Enter a phrase to convert: "))
