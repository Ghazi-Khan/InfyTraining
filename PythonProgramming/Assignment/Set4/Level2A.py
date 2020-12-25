#lex_auth_01269444890062848087

def find_correct(word_dict):
    res  = [0,0,0]
    
    for i, j in word_dict.items() :
        mismatch = 0
        
        if len(i) != len(j) :
            mismatch = 3
        else: 
            count = 0
            
            while count < len(i):
                if i[count] != j[count] :
                    mismatch +=1
                if mismatch > 2:
                    break;
                count += 1
                
        if mismatch == 0:
            res[0] += 1
        elif mismatch > 0 and mismatch <=2 :
            res[1] += 1
        else :
            res[2] += 1
    return res
        
    
    

word_dict={"THEIR": "THEIR","BUSINESS":"BISINESS","WINDOWS":"WINDMILL","WERE":"WEAR","SAMPLE":"SAMPLE"}
print(find_correct(word_dict))
