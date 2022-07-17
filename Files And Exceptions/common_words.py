file_path = "Files And Exceptions/book_sample.txt"

with open(file_path) as f_obj:
    line = f_obj.read()
    print(line.count("men"))
