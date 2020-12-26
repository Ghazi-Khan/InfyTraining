#lex_auth_01269444961482342489

def sms_encoding(data):
    res = ''
    vow = 'aeiouAEIOU'
    l = data.split()
    
    for i in l :
        if len(i) > 1 :
            for s in i :
                if s not in vow :
                    res += s
        else :
            res += i
        res += ' '
    return res.rstrip();
                

data="I love Python"
print(sms_encoding(data))
