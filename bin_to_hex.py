"""
    This program converts user input (binary, decimal) numbers to other base equals
    octal, hexadecimal, or binary / decimal dependant on input 
    Authors: Esteban Madrigal, Edgard Perez, Jacob Bueno
"""
from cgi import MiniFieldStorage
import math

# used to set is binary variable to true or false
map = {'y': True, 'n': False}
binary_check = ('.', '0', '1')
decimal_check = ('.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9')

def prompt_user() -> tuple:
    """ 
        prompts user for number and type
        return input as tuple(number: int, is_binary: boolean)
        Author: Esteban Madrigal
    """
    num = input("\nEnter a number (binary or decimal): ")
    is_binary = map.get(input("Is your number binary? (Y or N): ").lower())

    return prompt_helper(num, is_binary)

def prompt_helper(num, is_binary) -> tuple:
    """
        helper for prompt_user()
        returns tuple of binary/decimal and is_binary
        Author: Esteban Madrigal
    """
    # prompt user for input until no exceptions occur
    while True:
        try:
            # checking the validity of user input
            if is_binary is None:
                # character other than 'y' or 'n' was entered, prompt the user again
                raise KeyError("Only enter Y or N when prompted")
            elif is_binary:
                # run validity check for binary numbers
                for elem in num:
                    if elem not in binary_check:
                        raise ValueError("Binary can only contain 1 and 0")
            elif not is_binary:
                # run validity check for decimal
                for elem in num:
                    if elem not in decimal_check:
                        raise ValueError("Decimal can only contain characters [0-9]")

        except Exception as e:
            print(f"ERROR: {e}")
            # prompt user again for input
            num = input("\nEnter a number (binary or decimal): ")
            is_binary = map.get(input("Is your number binary? (Y or N): ").lower())

        else:
            # no exception occurred, break out of the loop and return the result
            return num, is_binary


def bin_to_octal(binary: str) -> str:
    """
        returns octal equivalent
        reference (https://www.youtube.com/watch?v=JxmarqiqUdM&t=192s)
        Author: Esteban Madrigal
    """
    new_bin = binary.split(".")
    octal_num = "" # stores the calculated octal digits
    binary_group = [] # 3 bit group for octal conversion

    # adding zeroes to end of bits (1) turns to (001)
    while (len(new_bin[0]) % 3 != 0):
        new_bin[0] = "0" + new_bin[0]
    
    # working in groups of 3 bits
    for min_i in range(0 , len(new_bin[0]) - 1, 3):
        # computation for normal integer
        deci_val = 0
        binary_group = new_bin[0][min_i: min_i + 3]

        # binary to decimal conversion
        # reversed(str) memory efficient compared to str[::-1]
        for i, bit in enumerate(reversed(binary_group)):
            deci_val += int(bit) * (2 ** i)

        octal_num += str(deci_val)

    # return computed octal
    return octal_num + "." + bin_oct_helper(new_bin[1])

def bin_oct_helper(bin_fraction) -> str:
    octal_fract = ""
    # adding zeroes to bits (1 turns to 100)
    while (len(bin_fraction) % 3 != 0):
        bin_fraction += "0"

    # working in groups of 3 bits
    for min_i in range(0 , len(bin_fraction) - 1, 3):
        # computation for fractional integer
        deci_val = 0
        bin_group = bin_fraction[min_i: min_i + 3]

        # bin to deci conversion
        for i, bit in enumerate(reversed(bin_group)):
            deci_val += int(bit) * (2 ** i)
        octal_fract += str(deci_val)

    return octal_fract


def bin_to_deci(binary):
    """
        returns decimal equivalent
        Author: 
    """


def bin_to_hexa(binary):
    """
        returns hexadecimal equivalent
        Author: 
    """




def deci_to_bin(num):
    """
        returns binary equivalent
        Author: Jacob Bueno
    """
    numList = []                    #Create a list to put our remainder values
    binString = 'Binary: '          #Create a string to hold our final converted number
    num = int(num)                  #Convert input to integer

    while num/2 >= 0.01:            #While loop set to repeat as long as the number/2 is greater than or equal to 0.01, if the value is > or = to 0.01 this means we can divide further 
        numList.append(num%2)           #Divide our number by 2 and put the remainder in our remainder list
        num = int(num/2)                #Replaced our number with the integer value of number/2 to update it for the next iteration of the while loop
    numList.reverse()               #Reverse the remainder list since our number is currently backwards
    for x in numList:               #Add each element of the remainder list to our final string
        binString += str(x)

    return binString                #Return final string

def deci_to_octal(num):
    """
        returns octal equivalent
        Author: Jacob Bueno
    """
    numList = []                    #Create a list to put our remainder values
    octString = 'Octal: '           #Create a string to hold our final converted number
    num = int(num)                  #Convert input to integer

    while num/8 >= 0.01:            #While loop set to repeat as long as the number/8 is greater than or equal to 0.01, if the value is > or = to 0.01 this means we can divide further 
        numList.append(num%8)           #Divide our number by 8 and put the remainder in our remainder list
        num = int(num/8)                #Replaced our number with the integer value of number/8 to update it for the next iteration of the while loop
    numList.reverse()               #Reverse the remainder list since our number is currently backwards
    for x in numList:               #Add each element of the remainder list to our final string
        octString += str(x)

    return octString                #Return final string


dictionary = {                      #Create a dictionary map to convert numbers >9 & <16 to letters
    10 : "A",
    11 : "B",
    12 : "C",
    13 : "D",
    14 : "E",
    15 : "F",
}

def deci_to_hexa(num):
    """
        returns hexadecimal equivalent
        Author: Jacob Bueno
    """
    numList = []                                    #Create a list to put our remainder values
    hexString = 'Hexadecimal: '                     #Create a string to hold our final converted number
    num = int(num)                                  #Convert input to integer

    while num/16 >= 0.01:                           #While loop set to repeat as long as the number/16 is greater than or equal to 0.01, if the value is > or = to 0.01 this means we can divide further 
        if (num%16) > 9:                                #Divide our number by 16 and check if the remainder is greater than 9
            numList.append(dictionary.get(num%16))      #If true add the corresponding letter based on our dictionary map         
        else:
            numList.append(num%16)                      #If false we divide our number by 16 and put the remainder in our remainder list 
        num = int(num/16)                           #Replaced our number with the integer value of number/8 to update it for the next iteration of the while loop
    numList.reverse()                               #Reverse the remainder list since our number is currently backwards
    for x in numList:                               #Add each element of the remainder list to our final string
        hexString += str(x)

    return hexString                                #Return final string


# code execution 