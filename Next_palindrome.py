def next_palindrome(n):
    n = n+1
    while not is_palindrome(n):
        n += 1
    return n



def is_palindrome(n):
    return str(n) == str(n)[::-1]


if __name__ == "__main__":


    try:
        n=int(input("Enter the number of test cases you want to try"))
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

    for i in range(n):
        print(f'Next plaindrome of {numbers[i]} is {next_palindrome(numbers[i])}')



    

