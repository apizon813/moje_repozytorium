alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def deciphre(str):
    list = str.split()
    output = []
    print(list)
    for word in list:
        string = ''
        for char in word:
            if char in alphabet:
                string += alphabet[(alphabet.index(char) + 2)%26]
            else:
                string += char
        output.append(string)
    output = " ".join(output)
    return output

text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

print(deciphre(text))
print(deciphre("map"))

