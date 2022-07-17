import json
numbers = [1, 2, 41123 , 43, 32, 5,123]

filename = "Files And Exceptions/numbers.json"
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)

