def swapFile():
    file1 = input("Enter First File: ")
    file2 = input("Enter Second File: ")
    with open(file1, 'r') as a:
        data_a = a.read()
    with open(file2, 'r') as b:
        data_b = b.read()
    with open(file1, 'w') as c:
        c.write(data_b)
    with open(file2, 'w') as d:
        d.write(data_a)
swapFile()


