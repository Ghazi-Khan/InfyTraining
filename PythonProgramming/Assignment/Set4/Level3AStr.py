#lex_auth_0127382283825971201450

def max_frequency_word_counter(data):
    word=""
    frequency=0
    
    l = data.split();
    resData = {}    #word, freq, len
    
    for i in l :
        resData[i.lower()] = resData.get(i.lower(), [0,0])[0] + 1, len(i)
        
  #  resData = sorted(resData.items(), key = lambda it : (it[1][1], it[1][0]), reverse = True);
    
    finRes = ['',0,0]    # name, frq, len
    
    for i in sorted(resData.items(), key = lambda it : (it[1][0], it[1][1]), reverse = True) :
        #print(i[0])
        
        if finRes[1] < i[1][0] :
            finRes[0] = i[0]
            finRes[1] = i[1][0]
            finRes[2] = i[1][1]
        elif finRes[1] == i[1][0] :
            if finRes[2] < i[1][1] :
                finRes[0] = i[0]
                finRes[1] = i[1][0]
                finRes[2] = i[1][1]
        else :
            break
                
     

    #print(finRes)
    print(finRes[0]+' '+ str(finRes[1]))
    return finRes[0]+' '+ str(finRes[1])
   # print(sorted(resData.values(), key = lambda it : (it[1], it[0]), reverse = True))
    
   # print(resData)
#    for i in resData.values() :
 #       print(i[1])
    #print(resData)
    

    #start writing your code here
    #Populate the variables: word and frequency


    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work
    #print(word,frequency)


#Provide different values for data and test your program.
data="Hands to clap and eyes to see"
max_frequency_word_counter(data)
