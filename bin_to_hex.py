"""
    This program converts user input (binary, decimal) numbers to other base equals
    octal, hexadecimal, or binary / decimal dependant on input 
    Authors: Esteban Madrigal, Edgard Jara, Jacob Bueno
"""
from cgi import MiniFieldStorage
import math

# used to set is binary variable to true or false
map = {'y': True, 'n': False}
binary_check = ('.', '0', '1')
decimal_check = ('.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9')

dictionary = {                      #Create a dictionary map to convert numbers >9 & <16 to letters
    10 : "A",
    11 : "B",
    12 : "C",
    13 : "D",
    14 : "E",
    15 : "F",
}

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
    if (len(new_bin) > 1):
        return octal_num + "." + bin_oct_helper(new_bin[1])
    else: 
        # binary has no decimal
        return octal_num

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
        Author: Edgard Jara
    """
    # first we need to create the decimal point variable
    deci_point = "."
  
    # if the binary number is a float, we need to split it into two parts 
    if (deci_point in binary):
        solid, partial = binary.split(deci_point)
        a = bin_whole_helper(solid)
        b = bin_fract_helper(partial)
        return a + b
    else:
        c = bin_whole_helper(binary)
    return c


def bin_fract_helper(fraction):
  #this function will take the fractional part of the binary number and convert it to a decimal
  
  # create a variable to store the decimal value
  fract = 0

  # we need to loop through the fractional part of the binary number and store the decimal value
  for place, number in enumerate(fraction):
    fract +=int(number)*2**(-(place+1))
  return fract
  
def bin_whole_helper(whole):
  # this function will take the whole part of the binary number and convert it to a decimal

  # create variables to store decimal value and a counter
  deci= 0
  count= 0

  # loop through the whole part of the binary number and store the decimal value
  for num in reversed(whole):
      deci += 2**count * int(num)
      count += 1
  return deci
 
def bin_to_hexa(binary):
  """
      returns hexadecimal equivalent
      Author: Edgard Jara
  """

  #first we need to create the decimal point variable
  hex_point = "." 
  # if the binary number is a float, we need to split it into two parts and add them together
  if (hex_point in binary):
    whole,fract = binary.split(hex_point)
    a = binwhole_to_hex_helper(whole)
    b = binfract_to_hex_helper(fract)
    return (a) +"."+ (b)
  else:
    c = binwhole_to_hex_helper(binary)
    return (c)

def binwhole_to_hex_helper(whole):
  """
      returns hexadecimal equivalent
      Author: Edgard Jara
  """
  ##This helper function will convert the whole part of the binary number to hex

  
  #create a variable to store the hex number
  deci_string =""
  
  #if length of whole is not divisible by 4, we need to add 0's to the start of the whole
  while (len(whole) % 4 != 0):
    whole = "0" + whole

  #loop through the whole and convert each 4 bit group   
  for min_i in range(0 , len(whole) - 1, 4):
    deci = 0
    count=0
    deci_string_loop = ""
    bin_group = whole[min_i:min_i + 4]

    #loop through the 4 bit group and convert it to a hexadecimal number
    for num in reversed(bin_group):
      deci += 2**count * int(num)
      count += 1
    if deci < 10:
      deci_string_loop=str(deci)
    else:
      deci_string_loop= dictionary.get(deci)

    #add the hexadecimal number to the string
    deci_string = deci_string + deci_string_loop
  return deci_string
        
  
def binfract_to_hex_helper(fraction):
  """
      returns hexadecimal equivalent
      Author: Edgard Jara
  """
  
  #this function will take the fractional part of the binary number and convert it to a hexadecimal number

  #create a variable to store the hexadecimal number
  fract_string = ""

  #if length of fraction is less than 4, we need to add 0's to the end of the fraction
  while (len(fraction) % 4 != 0):
    fraction += "0"

  #loop through the fraction and convert each 4 bit group to a hexadecimal number
  for min_i in range(0 , len(fraction) - 1, 4):
    count = 0
    fract = 0
    fract_string_loop = ""
    bin_group = fraction[min_i:min_i + 4]

    #loop through the 4 bit group and convert it to a decimal number
    for num in reversed(bin_group):
      fract += 2**count * int(num)
      count += 1
    if fract < 10:
      fract_string_loop = str(fract)
    else:
      fract_string_loop = dictionary.get(fract)

    #add the hexadecimal number to the string
    fract_string = fract_string +fract_string_loop
  return fract_string


def deci_to_hexa(num):
    """
        returns hexadecimal equivalent
        Author: Jacob Bueno
    """
    decimal = "."   #used later to seperate decimal numbers

    #if there is a decimal entered process decimal and integer seperatley else process integer    
    if (decimal in num):                       
        whole, fractal = num.split(decimal) 
        a = deci_to_hexa_whole(whole)
        b = deci_to_hexa_fractal(fractal)
        return a + "."+ b
    else:
        c = deci_to_hexa_whole(num)
        return c

def deci_to_hexa_whole(num):
    """
        returns hexadecimal equivalent
        Author: Jacob Bueno
    """
    numList = []    #Create a list to put our remainder values
    hexString = ''  #Create a string to hold our final converted number
    num = int(num)  #Convert input to integer

    #while there is a remainder, add remainder to list then change number to number / 16, repeat until there is no remainder
    while num%16 != num:                           
        if (num%16) > 9:                                
            numList.append(dictionary.get(num%16))              
        else:
            numList.append(num%16)                      
        num = int(num/16)                           

    #add the last remainder excluded from the while loop                          
    if (num%16) > 9:                                
        numList.append(dictionary.get(num%16))              
    else:
        numList.append(num%16) 

    numList.reverse()   #reverse the remainder list 

    #convert remander list to final string 
    for x in numList:                               
        hexString += str(x)

    return hexString    #return final conversion (string)              

def deci_to_hexa_fractal(num):
    """
        returns hexadecimal equivalent
        Author: Jacob Bueno
    """
    numList = []    #Create a list to put our values
    hexString = ''  #Create a string to hold our final converted number
    num = float(f"0.{num}")     #convert number to decimal
    
    #stop calculating after 5 tries (this stops the code from running infinitly in case a recuring number occurs)
    for x in range(5):

        #split the number into its integer and decimal values
        splitNum = str(num).split(".")
        whole = splitNum[0]
        decimal = float(f"0.{splitNum[1]}")

        #if decimal is 0 add corresponding integer value to our list
        if decimal == 0:
            if int(whole) > 9:
                numList.append(dictionary.get(int(whole)))
            else:
                numList.append(splitNum[0])
            break

        #else if decimal !=0, still add the integer value using tempNumber to seperate the integer and change number to number * 16 for next iteration
        else:
            tempNumber = str(decimal * 16).split(".")
            if int(tempNumber[0]) > 9:
                numList.append(dictionary.get(int(tempNumber[0])))
            else:
                numList.append(tempNumber[0])
            if int(tempNumber[1]) == 0:     #if tempNumber ever gets a decimal that is == 0 then we know we're done we can break
                break
            num = decimal * 16

    #convert remander list to final string
    for x in numList:                              
        hexString += str(x)

    return hexString    #return final conversion (string) 

def deci_to_octal(num):
    """
        returns hexadecimal equivalent
        Author: Jacob Bueno
    """
    decimal = "."   #used later to seperate decimal numbers

    #if there is a decimal entered process decimal and integer seperatley else process integer 
    if (decimal in num):
        whole, fractal = num.split(decimal)
        a = deci_to_oct_whole(whole)
        b = deci_to_oct_fractal(fractal)
        return a + "."+ b
    else:
        c = deci_to_oct_whole(num)
        return c

def deci_to_oct_whole(num):
    """
        returns octal equivalent
        Author: Jacob Bueno
    """
    numList = []    #Create a list to put our remainder values
    octString = ''  #Create a string to hold our final converted number
    num = int(num)  #Convert input to integer
    
    #while there is a remainder, add remainder to list then change number to number / 8, repeat until there is no remainder
    while num%8 != num:             
        numList.append(num%8)         
        num = int(num/8)                

    numList.append(num%8)   #add the last remainder excluded from the while loop 
    numList.reverse()   #reverse the remainder list   

    #convert remander list to final string 
    for x in numList:               
        octString += str(x)

    return octString    #return final conversion (string)                

def deci_to_oct_fractal(num):
    """
        returns hexadecimal equivalent
        Author: Jacob Bueno
    """
    numList = []    #Create a list to put our remainder values
    octString = ''  #Create a string to hold our final converted number
    num = float(f"0.{num}")     #convert number to decimal

    #stop calculating after 5 tries (this stops the code from running infinitly in case a recuring number occurs)
    for x in range(5):

        #split the number into its integer and decimal values
        splitNum = str(num).split(".")
        whole = splitNum[0]
        decimal = float(f"0.{splitNum[1]}")

        #if decimal is 0 add the integer value to our list
        if decimal == 0:
            numList.append(splitNum[0])
            break
        #else if decimal !=0, still add the integer value using tempNumber to seperate the integer and change number to number * 8 for next iteration
        else:
            tempNumber = str(decimal * 8).split(".")
            numList.append(tempNumber[0])
            if int(tempNumber[1]) == 0:     #if tempNumber ever gets a decimal that is == 0 then we know we're done we can break
                break
            num = decimal * 8

    #convert remander list to final string
    for x in numList:                               
        octString += str(x)

    return octString    #return final conversion (string)

def deci_to_bin(num):
    """
        returns hexadecimal equivalent
        Author: Jacob Bueno
    """
    decimal = "."   #used later to seperate decimal numbers
    
    #if there is a decimal entered process decimal and integer seperatley else process integer 
    if (decimal in num):
        whole, fractal = num.split(decimal)
        a = deci_to_bin_whole(whole)
        b = deci_to_bin_fractal(fractal)
        return a + "."+ b
    else:
        c = deci_to_oct_whole(num)
        return c

def deci_to_bin_whole(num):
    """
        returns octal equivalent
        Author: Jacob Bueno
    """
    numList = []    #Create a list to put our remainder values
    binString = ''  #Create a string to hold our final converted number
    num = int(num)  #Convert input to integer
    
    #while there is a remainder, add remainder to list then change number to number / 2, repeat until there is no remainder
    while num%2 != num:            
        numList.append(num%2)          
        num = int(num/2)                

    numList.append(num%2)   #add the last remainder excluded from the while loop
    numList.reverse()   #reverse the remainder list

    #convert remander list to final string
    for x in numList:               
        binString += str(x)

    return binString    #return final conversion (string)             

def deci_to_bin_fractal(num):
    """
        returns hexadecimal equivalent
        Author: Jacob Bueno
    """
    numList = []    #Create a list to put our remainder values
    binString = ''  #Create a string to hold our final converted number
    num = float(f"0.{num}")     #convert number to decimal

    #stop calculating after 5 tries (this stops the code from running infinitly in case a recuring number occurs)
    for x in range(5):

        #split the number into its integer and decimal values
        y = str(num).split(".")
        whole = y[0]
        decimal = float(f"0.{y[1]}")
        
        #if decimal is 0 add the integer value to our list
        if decimal == 0:
            numList.append(y[0])
            break
        #else if decimal !=0, still add the integer value using tempNumber to seperate the integer and change number to number * 2 for next iteration
        else:
            t = str(decimal * 2).split(".")
            numList.append(t[0])
            if int(t[1]) == 0:      #if tempNumber ever gets a decimal that is == 0 then we know we're done we can break
                break
            num = decimal * 2

    #convert remander list to final string
    for x in numList:                               
        binString += str(x)

    return binString    #return final conversion (string)                            


# code execution 
user_input = prompt_user()
num = user_input[0]




if (user_input[1]):
    # number is binary
    print(f"octal: {bin_to_octal(num)}")
    print(f"decimal: {bin_to_deci(num)}")
    print(f"hexadecimal: {bin_to_hexa(num)}")
else:
    # number is decimal
    print(f"Binary: {deci_to_bin(num)}")
    print(f"Octal: {deci_to_octal(num)}")
    print(f"Hexadecimal: {deci_to_hexa(num)}")
