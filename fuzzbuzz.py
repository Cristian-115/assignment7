
def fuzzbuzz(value):
    array = [value]
    for i in range(value):
        if i % 5 == 0:
            array.append("Buzz")
        elif i % 3 == 0:
            array.append("Fizz")
        elif i % 5 == 0 and i % 3 == 0:
             array.append("FizzBuzz")
        else:
            array.append(i)
    array.pop(0)
    return array

