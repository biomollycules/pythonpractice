def FirstFactorial(num):  #define the function FirstFacorial() which takes the integer num as input

  for i in range (num - 1, 0, -1): #create a for loop that starts at num - 1, ends at 0, increments by -1 
    num = i * num 
  return num

print(FirstFactorial(input()))
