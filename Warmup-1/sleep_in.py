'''
The Warump-1/sleep_in problem from Coding Bat
'''

'''
Takes two parameters that indicate if today is a weekday,
and whether or not we are currently on vacation. Depending,
on these values, it outputs True/False to let us know if we 
can/shoudl sleep in today
'''

def sleep_in(weekday:bool, vacation: bool):
   if weekday and not vacation:
      return False
   else:
      return True

def sleep_in(weekday, vacation):
# first check whether or not it's a weekday
   if weekday = True:
   # yes, are we on vacation
      if vacation = True:
         return True # sleep in
      else: 
         return False # work day
   else:
   # no, are we on vacation
      if vacation == True:
       return True
   else:
   # if we are not 
    return False:
