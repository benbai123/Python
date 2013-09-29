# display message and wait for input
# input is always a string
# ref http://stackoverflow.com/questions/5424716/python-how-to-check-if-input-is-a-number-given-that-input-always-returns-stri
x = input("Please enter an integer, or q to stop: ")
sum = 0
# while input is not 'q'
while x != 'q':
  try: # try to convert x to integer
    x = int(x)
    if x < 0:
      x = 0
      print('Negative changed to zero')
    elif x == 0: # keyword 'elif' is short for 'else if'
      print('Zero')
    else:
      print('positive')
    sum += x
    print('sum = ' + str(sum))
    x = input() # wait for next input
  except ValueError: # error happened when convert x to integer
    x = input("Please enter an integer, or q to stop: ")