import random
import string

def Generate_Random(n = 6): 
    return ''.join(random.choice(string.ascii_letters) for _ in range(n))

def encrypt(Text): 
    if len(Text) <= 3:
        return Text[::-1]
    
    shift = Text[1:] + Text[0]
    prefix = Generate_Random(6)
    sufix = Generate_Random(6)

    encription = prefix + shift + sufix
    return encription
def encrypt_sentence(sentence): 
    words = sentence.split()
    encrypted_words = [encrypt(word) for word in words]
    return ' '.join(encrypted_words)

user = input("Enter Your Text here : ")
secure = encrypt_sentence(user)
print("Encrypted Text : ", secure)






