'''The basic idea is that if one initialises a variable as 0 and applies the XOR operator to the variable
with each element of an array of numbers, at the end the variable will store the number which has been
repeated odd number of times. This is simply because an even frequency will nullify the value stored
in the variable. The process will be clearer with the aid of the pseudocode and hand simulation.'''

array = [1, 2, 3, 2, 3, 1, 3]
result = 0
for element in array:
    result = result ^ element
print(result)

