
pass_items = {
    'a': "bsfh", 'b': "ai33", 'c': "alw", 'd': "na", 'e': "aiw",
    'f': "gs", 'h': "aioue", 'i': "al", 'j': "4ht", 'k': "ief",
    'l': "jfd", 'm': "fh", 'n': "ddy", 'o': "ghj", 'p': "hl",
    'q': "fy", 'r': "gi", 's': "gyy", 't': "fh", 'u': "v",
    'v': "gjh", 'w': "drgg", 'x': "dfgerg", 'y': "dh", 'z': "kshg",
    '1': "haf", '2': "aljfd", '3': "485h", '4': "jkdf", '5': "kdfh",
    '6': "lakf", '7': "akjdf", '8': "skjfh", '9': "ajdf", '0': "sdjh"
}
if __name__ == "__main__":
    print("Select an option: ")
    print("1. Encrypt a message/password")
    print("2. Decrypt a message/password")
    

    try:
        a = int(input("Enter your choice (1 or 2): "))
    except ValueError:
        print("opps!didn't found that one. Please enter 1 or 2.")
        exit()


    if a == 1:
        message = input("Enter the word to make a secret: ")
        encrypted_message = ""
        
        for char in message:
    
            if char in pass_items:
                encrypted_message += pass_items[char] 
            else:
                encrypted_message += char  

        print("Encrypted message:", encrypted_message)
    elif a == 2:
        print("Decryption yet to be implemented")
    else:
        print("its not there. Please select 1 or 2.")
