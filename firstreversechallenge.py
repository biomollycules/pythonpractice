def FirstReverse(strParam): #define the function FirstReverse() that takes the string strParam as input
  return strParam[::-1]  #return the strParam [] is a slice, [start, stop, step], :: makes system auto start/stop so begins at beginning of string & ends at end, -1 increments backwards

print(FirstReverse(input()))
