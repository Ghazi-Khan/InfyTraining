#lex_auth_012693819159732224162

def check_palindrome(word):
    s = list(word)
    i =0
    j = len(s)-1
    
    while i<j :
        if s[i] != s[j] :
            return False
        i += 1
        j -= 1
    return True
    
    #Remove pass and write your logic here

status=check_palindrome("malayalam")
if(status):
    print("word is palindrome")
else:
    print("word is not palindrome")
