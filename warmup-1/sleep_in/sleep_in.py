'''
the Warmup-1/sleep_in problem from Coding Bat
'''

def sleep_in(weekday: bool, vacation: bool):
  '''
  Takes two parameters that indicate if today is a weekday,
  and whether or not we are currently on vacation. Depending,
  on those values, it outputs True/False to let us know if
  we can/should sleep in today.
  '''
  return False if weekday and not vacation else True
