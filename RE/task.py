#!/usr/bin/env python3

def encode(msg):
    output = ''

    for i in range(len(msg)):
        temp = ord(msg[i]) * 0x40
        temp = temp >> 4
        if 0xc0 <= temp < 0xe8:
            output = str(int(msg[i]) * 0x1234) + output
        else:
            output = chr(ord(msg[i]) * 0x10) + output

    return output


# TODO implement the decode function
def decode(msg):
    output = ''
    tmp_num = ''

    for i in range(len(msg)):
        temp = ord(msg[i])
        
        if 0x30 <= temp < 0x39:
            tmp_num  = tmp_num + msg[i]
        else:
            if tmp_num != '':
                output = str(int(tmp_num)//0x1234) + output
                tmp_num = ''
            output = str(chr(ord(msg[i])//0x10)) + output
    
    return output



def shift(msg):
    j = len(msg) - 1
    output = ''

    for i in range(len(msg)//2):
        output += msg[i] + msg[j]
        j -= 1

    return output


# TODO implement the unshift function
def unshift(msg):
    j = len(msg) - 1
    output = ''

    for i in range(0, len(msg), 2):
        output += msg[i]
    for i in range(len(msg)-1, 0, -2):
        output +=msg[i]

    return output

if __name__ == '__main__':
    #shifted = shift('<REDACTED>')
    #print(shifted)
    #hashed = encode(shifted)
    #print (hashed)
    # print (unshift('<>RDEEDTAC'))
    hashed = '4660۠ܰ4660ڀ٠װװސ23300۰ސݐ18640ܠݰװۀڠ18640۰ްؠѠȐՀȐа4660ѠȐѠߐА'
    # CODE HERE
    print(decode(hashed))
    print(unshift(decode(hashed)))
    
# AFFCTF{4lw4y5_f1n1sh_your_job!!1!}