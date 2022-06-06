#Define a hexadecimal value
hex_value = input("Enter HEX value input: ")

#Convert to Integer
int_value = int(hex_value, base=16)

#Convert integer to binary value
bin_value = str(bin(int_value))[2:].zfill(len(hex_value*4))

#Count no. of 1
count_1 = 0
for i in range(len(bin_value)):
    if bin_value[i] == "1":
        count_1 += 1

#Check no. of 1 is even or odd number + print input + print output (OK or Error)
print("Input: ",hex_value)
#This is even parity protocol 
#If no. of 1 is even -> OK : No error detected -> There is no error during data transmission
#If no. of 1 is odd -> Error : Error detected -> There is error during data transmission
#No. of 1 is Even
if (count_1 % 2) == 0:
    print("Output: OK")
#No. of 1 is Odd
else:
    print("Output: Error")


