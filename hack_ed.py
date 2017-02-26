#READ ME:
#Submitted by: Ashish Adhikari
#			   Howard University
#			   B.Sc. Computer Science, Expected Concentration: cybersecurity
#
#	This program consists of three functions:
#		1.rot13(s):  Parameter => single string 
#				     Return    => String right shifted by 13 preserving upper/lower case
#							note* does not change non alphabtic characters
#
#		2.base64(s): Parameter => single string 
#					 Return    => processed string based on base64 encryption algorithm
#
#		3.binaryConverter(s)  Parameter => Single string
#							  Return    => Returns binary encoded value of the string 
#								base64(s) actually consists a part where similar step is involved
#	    
########################################################################################################
def rot13(INPUT):
  encrypt_text =""
  char_ord = 0
  overVal = 0
  
  for char in INPUT:
    #get int value of ASCII
    char_ord = ord(char)
    #if Capital letter
    if 65 <= char_ord <=90:
      char_ord += 13
      #if the sum exceeds 90
      if char_ord > 90:
        overVal = char_ord - 91
        char_ord = 65 + overVal
    #if small letter
    elif 97<= char_ord <=122:
      char_ord += 13
      if char_ord > 122:
        overVal = char_ord - 123
        char_ord = 97 + overVal
    
    #take the value of ord and add it to encrypt_text  
    encrypt_text += chr(char_ord)
    
  return encrypt_text 

###########################################################################################################
def base64(INPUT):
  #get the binary equivalent of the string
  binaryInput = ''                            #used to store the binary values of INPUT 
  for char in INPUT:
    binaryInput += format(ord(char),'08b')
  
  #if the number of bytes in INPUT is not a multiple of 3, calculate number of missing bytes
  if len(INPUT) % 3 != 0:
     lenToFix = 3 - (len(INPUT)%3)           #number of 00000000 bits to be added in the binaryInput
      
     #add missing bytes  
     for i in range (lenToFix):
       binaryInput += '00000000'
  
  
  ######PART TWO####### 
  #take 6 bits in each iteration and process to modify encrypt_text 
  b64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
  front = 0
  back = 6
  bitLength = len(binaryInput)             #length of standardised input binary string 
  encrypt_text = ''                        # to store block of 6 bits for every iteation
  block = ''
  for i in range (bitLength/6):           #since six binary strings are processed in every itereation
    block = binaryInput [front:back]	  #slice the binary string into blocks of 6 bits
    front +=6
    back +=6
    encrypt_text+= b64[int(block,2)]
  
  return encrypt_text
###################################################################################################################
#take a string and return its bit pattern based on ASCII interpretation    
def binaryConverter(INPUT):
	binaryInput = ''
	for char in INPUT:
		binaryInput += format(ord(char),'08b') 

####################################################################################################################


##sample test:
print binaryConverter((base64(rot13('HackEd'))))



