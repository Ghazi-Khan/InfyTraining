#lex_auth_012693813706604544157

def digSum(n) :
    sum = 0
    
    for i in str(n) :
        sum += int(i)
    return sum

def find_max(num1, num2):
    
    max_num = -1
    l = []
    
    if num1 >= num2 :
        return -1;
    
    for i in range(num1, num2+1):
        if len(str(i)) == 2 and i % 5 == 0 and digSum(i) % 3 == 0 :
            l.append(i)
     # Write your logic here
    l.sort(reverse = True)
    
    if len(l) >0 :
        max_num = l[0]
    return max_num

#Provide different values for num1 and num2 and test your program.
max_num=find_max(10,15)
print(max_num)
