import string

def interpret(cmd):
    SIZE = 100000
    data_arr = [0] * SIZE
    dp = 0
    ip = 0
    while ip < len(cmd):
        char = cmd[ip]
        if char == '>':
            if dp != SIZE - 1:
                dp = dp + 1
            else:
                raise IndexError
        elif char == '<':
            if dp != 0:
                dp = dp - 1
            else:
                raise IndexError
        elif char == '+':
            if data_arr[dp] != 255:
                data_arr[dp] = data_arr[dp] + 1
            else:
                raise OverflowError
        elif char == '-':
            if data_arr[dp] != 0:
                data_arr[dp] = data_arr[dp] - 1
            else:
                raise OverflowError
        elif char == '.':
            print chr(data_arr[dp])
        elif char == ',':
            data_arr[dp] = ord(sys.stdin.read(1))
        elif char == '[':
            if data_arr[dp] == 0:
                temp = string.find(cmd[ip:], ']')
                if temp != -1:
                    ip = temp
        elif char == ']':
            if data_arr[dp] != 0:
                temp = string.rfind(cmd[:ip], '[')
                if temp != -1:
                    ip = temp
        ip = ip + 1

def brainfpck():
    print "Type a filename here to execute it."
    print "Your file should be in the same directory as this program."
    print "Or if you want to go into interpret mode, just press Enter."
    filename = raw_input("Enter your choice: ")
    if filename == '':
        print 'Entering interpret mode...'
        # TODO: Implement interpret mode
    else:
        try:
            f = open(filename, 'r')
        except:
            print "Could not open file.  Exiting..."
            exit(1)
        cmd = f.read()
        interpret(cmd)
    
