def decrypt(text):
    if len(user) <= 3:
        return text[::-1]
    prefix_and_suffix_remover = text[3:-3]
    shift_reverse = prefix_and_suffix_remover[-1] + prefix_and_suffix_remover[:-1]
    return shift_reverse
                


user = input("Enter Your text here : ")
decrypted = decrypt(user)
print("decrypted : ",decrypted)