from fileinput import filename


file_name = "Files And Exceptions/alice.txt"
try:
    with open(file_name) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + file_name + " does not exist"
    print(msg)
else:
    # Count the approximate number of words in the file
    words = contents.split()
    num_words = len(words)
    print("Word's count: " + str(num_words))