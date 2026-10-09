"""
Write a python function to check whether three given numbers can form the sides of a triangle. 
Hint: Three numbers can be the sides of a triangle if none of the numbers are greater than or equal to the sum of the other two numbers."""


#lex_auth_012693802383794176153

def form_triangle(num1,num2,num3):
    #Do not change the messages provided below
    if num1>0 and num2>0 and num3>0 and num3+num2>num1 and num1+num3>num2 and num1+num2>num3:
        success="Triangle can be formed"
        return success
    else:

        failure="Triangle can't be formed"
        return failure

#Provide different values for the variables, num1, num2, num3 and test your program
num1=3
num2=3
num3=5
print(form_triangle(num1, num2, num3))