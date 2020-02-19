with open('my_input_file.txt') as f:
    contents=f.read()
    print(contents.rstrip())


with open('my_input_file.txt') as f:
    contents=f.read(10)  #read only first 10 objects in the file
    print(contents.rstrip())



with open('my_input_file.txt') as f:
    contents=f.read(10)
    contents2 = f.read(10)
    print(f.tell())  #tell me where my position is on the file after 10+10

#operation ends

print(contents)
print(contents2)


#method one
with open('my_input_file.txt') as f:
    for line in f: #print line by line
        print(line.rstrip())

#method two, doing it from memory, faster way
with open('my_input_file.txt') as f:
    lines=f.readlines()
for l in lines:
    print(l.rstrip()) #rstrip: strip the non-printing lines

print(lines)

print(len(lines))