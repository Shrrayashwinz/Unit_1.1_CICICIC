number_variable = 5

greeting = 'Hello'

try:
    value = number_variable + greeting

except TypeError as e:
    print(f'Execption thrown is: {e}')
    #consume the exeception so wont cause further problems
    #Writing code that can fix the mistake


else:
    print(value)

finally:
    #run code regardless of exception
    print("Run at the close")


print("I'm still here, losers!")