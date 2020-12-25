#lex_auth_01269444195664691284

def encrypt_sentence(sentence):
    l = sentence.split()
    res = ''
    for i in range(0, len(l)):
        if (i+1)%2 == 1:
          #  print(l[i][::-1])
            res += l[i][::-1]+' '
        else :
            const = []
            vow = []            
            
            t1 = 'aeiouAEIOU'
            for s in l[i] :
                if s not in t1:
                    const.append(s)
                else :
                    vow.append(s)
            
            res += ''.join(const)+''.join(vow)+' '
 
    return res.rstrip()


sentence="The sun rises in the east"
encrypted_sentence=encrypt_sentence(sentence)
print(encrypted_sentence)
