#lex_auth_012693825794351104168

def find_common_characters(msg1,msg2):
    s = ''
    
    for i in msg1 :
        if i != ' ' and i in msg2 and i not in s :
            s += i
    if len(s) > 0:
        return s
    
    return -1


#Provide different values for msg1,msg2 and test your program
msg1="moto"
msg2="moto"
common_characters=find_common_characters(msg1,msg2)
print(common_characters)
