'''
Date:01-10-2020
Purpose: Practice problem
'''

'''
This code will give the nect plaindrome only if the number in the list is  mgreater than 10'''

def next_palindrome(n):
    n = n+1
    while not is_palindrome(n):
        n += 1
    return n



def is_palindrome(n):
    return str(n) == str(n)[::-1]


if __name__ == "__main__":


    try:
        n=int(input("Enter the sixe of the list"))
    except ValueError:
        print("You should enter only the interger value \n")

    numbers = []
    for i in range(n):
        try:

            num=int(input("Enter the numbers \n"))
            numbers.append(num)
        except ValueError:
            print("Values shud be intergers")
            exit()
        
    # print(numbers) Just to check the numbers are printing in a list or not

    #to print only if the nmber in the list is greather thna 10
    nums = []
    for i in range(n):
        if numbers[i]>10:

            #append next palindrome of the number to the list, if the number is greater than 10

            nums.append(next_palindrome(numbers[i]))
        else: 
            #otherwise append the same number to the list
            nums.append(numbers[i])

    print(f"Your output list is {nums}")

    # the bellow code is using the list comphrension, the above logic of finding the number is greater than 10 
    #can be written in a singl line
    
    print(f"Output list: {[numbers[i] if numbers[i]<10 else next_palindrome(numbers[i]) for i in range(n)]}")

