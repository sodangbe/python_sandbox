# A function is a block of code which only runs when it is called. In Python, we do not use curly brackets, we use indentation with tabs or spaces

import json ,operator
# Create function
def sayHello(name='Sam'):
    return (f'Hello {name}')


# Return values
def getSum(num1, num2):
    total = num1 + num2
    return total


# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

getSum = lambda num1, num2: num1 + num2

print(getSum(10, 3))
print(sayHello('romeo'))
print(sayHello())



def sort_by_price_ascending(json_string):
    
    json_parse =json.loads(json_string)
    sorting_json = json.dumps(json_parse,sort_keys=True)
    #json_parse.sort(key=operator.itemgetter('price'))
    #sorted = json.dump(json_parse, indent=2)
    return  sorting_json

print(sort_by_price_ascending('[{"name":"eggs","price":1},{"name":"coffee","price":9.99},{"name":"rice","price":4.04}]'))