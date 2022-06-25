def encryption(text, distanceValue):
  print("\nYour plaintext is:", text)
  plainText = text
  distance = int(distanceValue)
  code = ""
  for ch in plainText:
    ordvalue = ord(ch)
    cipherValue = ordvalue + distance
    if cipherValue > ord('~'):
      cipherValue = ord('!') + distance - (ord('~') - ordvalue + 1)
    code += chr(cipherValue)
  print("The encrypted text is:", code)
  return code

text = input("Please input plaintext: ")
distanceValue = input("Please input a distance value: ")
while True:
  code = encryption(text, distanceValue)
  option = input("\nIs this the desired result? (y/n) ")
  if option == "y":
    break
  elif option == "n":
    code = input("\nPlease re-input plaintext: ")
    distanceValue = input("Please input a new distance value: ")
  else:
    print("\nInvalid response.  Reprinting results.")
print("\nYour coded text is", code)