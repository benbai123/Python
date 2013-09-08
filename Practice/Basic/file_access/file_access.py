import os

# get path of the folder contains this script
pathToCurrentFolder = os.path.dirname(os.path.abspath(__file__))
# open test.txt in read mode
f = open(pathToCurrentFolder + '/test_files/test.txt', 'r')
# create output.txt (write mode)
o = open(pathToCurrentFolder + '/test_files/output.txt', 'w')
# create output2.txt (write mode)
o2 = open(pathToCurrentFolder + '/test_files/output2.txt', 'w')

idx = 1

print('current folder: ' + pathToCurrentFolder)

# get all content of test.txt
content = f.read()

print('write all content to test_files/output.txt')
# write content to output.txt
o.write("content from test.txt: " + content)

# go to head of test.txt
f.seek(0)

print('write each line with line number to test_files/output2.txt')
# for each line in test.txt
# write line with line number into output2.txt
for line in f:
    o2.write(str(idx) + '\t' + line)
    idx += 1
# or call o2.write(f.readline()) three times