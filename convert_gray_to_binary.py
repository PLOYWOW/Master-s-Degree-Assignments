def to_list(gray_code): #Convert String to List
    n = len(gray_code)
    gray_list = [0]*n
    for i in range(n):
        gray_list[i] = gray[i]
    return gray_list

def print_list(list): #Print List
    n = len(list)
    for i in range(n):
        print(list[i],end='')
    print("")

def convert(gray_list): #Convert Gray Code to Binary Code
    n = len(gray_list)
    bin_list = [0]*n
    bin_list[0] = gray_list[0]
    for i in range(1,n): #XOR
        if gray_list[i] == bin_list[i-1]:
            bin_list[i] = "0"
        else: 
            bin_list[i] = "1"
    return bin_list

gray = "1000000000" #Input
gray_list = to_list(gray) #Convert String to List
print("Input, Gray Code: ",end='') 
print_list(gray_list) #Print Gray List
print("Output, Binary Code: ",end='')
print_list(convert(gray_list)) #Convert Gray Code to Binary Code and Print Out



