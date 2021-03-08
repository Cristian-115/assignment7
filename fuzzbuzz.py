
def fuzzbuzz(value):
    array = [value]
    for i in range(value):
        if i % 5 == 0:
            array.append("Buzz")
        
        else:
            array.append(i)
    array.pop(0)
    return array

