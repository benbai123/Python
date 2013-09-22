# ref:
# number concat string
# http://stackoverflow.com/questions/6981495/how-can-i-concatenate-a-string-and-a-number-in-python
#
# Complex Number
# http://en.wikipedia.org/wiki/Complex_number
#
# Python doc:
# http://docs.python.org/3/tutorial/introduction.html
# http://docs.python.org/3/library/stdtypes.html#typesnumeric
# 

# +, -, *, /
print()
print(" +, -, *, /")
print("    3+3 = " + str(3+3)) # 6
print("    3-3 = " + str(3-3)) # 0
print("    3*3 = " + str(3*3)) # 9
print("    3/3 = " + str(3/3)) # 1.0

# +, -, *, / with ()
print(" +, -, *, / with ()")
print("    (4+5)*3 = " + str((4+5)*3)) # = 9*3 = 27

# negated
print(" negated")
x = 5;
print("    x = 5, -x = " + str(-x)) # -5

# use equal sign to assign value
print(" use equal sign to assign value")
a = 2
b = 3
print("    a=2, b=3, a*b = " + str(a*b)) # 6

# absolute value
print(" absolute value")
print("    abs(5) = " + str(abs(5))) # 5
print("    abs(-5) = " + str(abs(-5))) # 5

# division always returns a floating point number automatically
print(" division always returns a floating point number automatically")
print("    8/5 = " + str(8/5)) # 1.6
print("    32/3 = " + str(32/3)) # 10.666666666666666

# floor division
print(" floor division")
print("    8//5 = " + str(8//5)) # 1
print("    32//3 = " + str(32//3)) # 10

# MOD (the remainder of the division)
print(" MOD (the remainder of the division)")
print("    32%3 = " + str(32%3)) # 2

# the pair (x // y, x % y)
print(" the pair (x // y, x % y)")
print("    divmod(32, 3) = " + str(divmod(32, 3))) # (10, 2)

# floor to specific digits with round()
print(" floor to specific digits with round()")
print("    round(8/3, 2) = " + str(round(8/3, 2))) # 2.67

# complex number with real part re, imaginary part im. im defaults to zero
print(" complex number with real part re, imaginary part im. im defaults to zero")
print("    complex(1, 2) = " + str(complex(1, 2))) # (1+2j)

# power
print(" power")
print("    2**5 = " + str(2**5)) # 32
print("    pow(2, 5) = " + str(pow(2, 5))) # 32

# converted to integer
print(" converted to integer")
print("    int(1.23) = " + str(int(1.23))) # 1

# converted to floating point
print(" converted to floating point")
print("    float(5) = " + str(float(5))) # 5.0
