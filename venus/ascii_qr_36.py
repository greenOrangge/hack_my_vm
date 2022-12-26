# Opening the file we saved which has the qr code, we use r to denote we are opening the file to read
with open('[path_of_the_file]', 'r') as qr:
    lines = qr.readlines()
# we are reading line by line and replacing all the '#' symbols with a block google what (0x2588) is
for l in lines:
    print(l.replace('#', chr(0x2588)), end='')
