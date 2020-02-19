with open('my_input_file.txt','r+') as f:  #r+: open a file, reading+writing
    for line in f: #print line by line
        print(line)
    f.write("This is the last line i just added.\n")