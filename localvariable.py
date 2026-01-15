local_result = 0
def calculate():
    global local_result
    local_result = 50 #local_variable
    print(local_result)
     
def another_function():
    #Error! NameError: name 'local_result' is not defined
    print(local_result)

calculate()
another_function()