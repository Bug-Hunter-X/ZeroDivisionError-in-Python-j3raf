def my_function(a, b):
    if b == 0:
        return "Division by zero is not allowed"
    else:
        return a / b

result = my_function(10, 0)
print(result) #Output: Division by zero is not allowed
result2 = my_function(10,2)
print(result2) # Output 5.0