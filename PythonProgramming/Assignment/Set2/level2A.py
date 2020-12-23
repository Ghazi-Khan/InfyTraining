#lex_auth_012693810762121216155

def solve(heads,legs):
    error_msg="No solution"
    chicken_count=0
    rabbit_count=0

    if legs % 2 != 0 or legs <= heads:
        print("No Solution")
    else:
        rabbit_count = (legs//2) - heads
        chicken_count = heads - rabbit_count
        if (rabbit_count+chicken_count) != heads or (rabbit_count*4 + chicken_count*2) != legs :
            print("No Solution")
        else:
            print(chicken_count,rabbit_count)
    #Start writing your code here
    #Populate the variables: chicken_count and rabbit_count



    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work

   
    #print(error_msg)

#Provide different values for heads and legs and test your program
solve(150,440)
