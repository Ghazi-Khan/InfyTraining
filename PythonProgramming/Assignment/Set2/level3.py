#lex_auth_012693782475948032141

def calculate_bill_amount(food_type,quantity_ordered,distance_in_kms):
    
    bill_amount = 0
    ft = ['N','V']
    food_price = {'V':120,'N':150}
    
    if food_type not in ft or quantity_ordered < 1 or  distance_in_kms < 1:
        return -1;
    else :
        bill_amount += food_price[food_type] * quantity_ordered
        
        distance_in_kms -= 3
        
        if distance_in_kms >0 :
            if distance_in_kms - 3 > 0:
                bill_amount += 9
                distance_in_kms -= 3
                if distance_in_kms > 0 :
                    bill_amount += distance_in_kms* 6
            else :
                bill_amount += distance_in_kms*3
                
    return bill_amount

#Provide different values for food_type,quantity_ordered,distance_in_kms and test your program
bill_amount=calculate_bill_amount("N",2,7)
print(bill_amount)
