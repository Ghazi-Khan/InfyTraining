#lex_auth_012693711503400960120
'''
Author  : Ghazi Khan
Problem : https://lex.infosysapps.com/en/viewer/hands-on/lex_auth_012693711503400960120?collectionId=lex_auth_0125409616243425281061&collectionType=Course
'''
def find_product(num1,num2,num3):
    #product=0
    #write your logic here
    if num3 == 7 :
        return -1
    elif num2 == 7 :
        return num3
    elif num1 == 7 :
        return num3* num2
    return num1*num2*num3

#Provide different values for num1, num2, num3 and test your program
product=find_product(7,6,2)
print(product)
