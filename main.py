import string 
#This program is the starter code for the Cipher Usability Project. 
# This code is inspired by Cracking Codes with Python: An Introduction to Building and Breaking Ciphers by Al Sweigart https://www.nostarch.com/crackingcodes (BSD Licensed)

# Global variables
initialPosition = 0
shiftedPosition = 0
shiftedMessage = ""

letterslower = string.ascii_lowercase
lettersupper = string.ascii_uppercase
numbers = string.digits
symbols = string.punctuation

possibleCharacters = letterslower + lettersupper + numbers + symbols


def wraparound(position): #wrap around func 
  return position % len(possibleCharacters)

def encryptOrdecrypt(initialMessage,key,mode): #encrypt/decrypt func
  global shiftedMessage
  shiftedMessage = ""
  
  
  for character in initialMessage:
    if character in possibleCharacters:
      initialPosition = possibleCharacters.find(character)

      if mode.lower() == "e":
        shiftedPosition = initialPosition + key
      elif mode.lower() == "d":
        shiftedPosition = initialPosition - key

      shiftedPosition = wraparound(shiftedPosition)
      shiftedMessage += possibleCharacters[shiftedPosition]

    else:
      shiftedMessage += character

  return shiftedMessage

# Introduction
def start():
  print("Welcome! This program will encrypt or decrypt your secret message using the Caesar cipher. \n\nWhen creating your message, you may only choose from the following characters: " + possibleCharacters + "\n\nLet's get started!\n")

# Receive user input
  initialMessage = input("Please enter your message: ").upper()
  key = int(input("Please enter your key: "))
  mode = input("Would you like to encrypt or decrypt your message? Use 'e' for encrypt or 'd' for decrypt: ").lower()
  while mode != "e" and mode != "d":
    mode = input("Please enter a valid answer: ").lower()
  if mode.lower() == "e":
    result = encryptOrdecrypt(initialMessage,key,mode)
    print("Your encrypted message is: " + result)
  else:
    result = encryptOrdecrypt(initialMessage,key,mode)
    print("Your encrypted message is: " + result)
start()