# Problem Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".

string_bits('Hello') → 'Hlo'
string_bits('Hi') → 'H'
string_bits('Heeololeo') → 'Hello'


def string_bits(str):
  result = ""
  # Within the string. 
  # grabing the even value characters
  #Loop that increments by 2 each time
  
  for i in range(len(str)):
    if i % 2 == 0:
      result = result + str[i]
      
      # You only want an even result so an odd number would not work. Therefore this is why we do the i % 2 ==0.
      
  return result
