#lex_auth_012693816331657216161

def encode(message):
    i = 0
    j = 0
    count = 1
    res = ''
    while i < len(message) :
        j = i+1
        while j < len(message) :
            if message[i] == message[j] :
                count += 1
                j += 1
                i += 1
            else :
                break
        
        res += str(count) + message[i]
        count = 1
        i = j
        #    i += 1
    return res
        
        
        
#Provide different values for message and test your program
encoded_message=encode("AAABBCA")
print(encoded_message)
