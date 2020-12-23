#lex_auth_012693780491968512136

def make_amount(rupees_to_make,no_of_five,no_of_one):
    five_needed=0
    one_needed=0
    
    if (rupees_to_make > ((no_of_five * 5) + no_of_one)) or (no_of_one < (rupees_to_make % 5)) :
        print(-1)
    else :
        five_needed = (rupees_to_make // 5)
        
        
        if five_needed > no_of_five :
            five_needed = no_of_five
            rupees_to_make = rupees_to_make - (no_of_five * 5)
        else :
            rupees_to_make = rupees_to_make - (five_needed * 5)
        
        one_needed = no_of_one - (no_of_one - rupees_to_make)
        
        print("No. of Five needed :", five_needed)
        print("No. of One needed  :", one_needed)
    #print(-1)


#Provide different values for rupees_to_make,no_of_five,no_of_one and test your program
make_amount(110,21,8)
