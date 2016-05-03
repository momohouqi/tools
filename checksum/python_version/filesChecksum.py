#! /usr/bin/env python

import os
import sys
import binascii
import io
import hashlib

class checkvalue:
    def getchecksum(self, filename):
        md5value = 0
        if os.path.exists(filename):
            fp = io.FileIO(filename, 'rb')
            if fp is not None:
                allbytes = fp.readall()
                fp.close()
                m = hashlib.md5()
                m.update(allbytes)
                md5value = m.hexdigest()
        else:
            print('file {0} does not exist'.format(filename))
        return int(md5value, 16)

    def getcrc(self, filename):
        if os.path.exists(filename):
            fp = open(filename, 'rb')
            crc = 0
            if fp is not None:
                content = fp.read()
                crc = binascii.crc32(content, crc)
                fp.close()
            else:
                print('open file fail!')
        else:
            print('file {0} does not exist'.format(filename))
        return crc

def main(argv = None):
    if argv is None:
        argv = sys.argv
    print('list input dir:{0}'.format(os.listdir(argv[1])))
    ob = checkvalue()
    for filename in os.listdir(argv[1]):
        mypath = os.path.join(argv[1], filename)
        if os.path.isfile(mypath):
            #ob.getchecksum(mypath)
            print('file: %s, length: %d, crc: 0x%X, sum: 0x%X' %(mypath,
                os.path.getsize(mypath), ob.getcrc(mypath),
                ob.getchecksum(mypath)))

if __name__== '__main__':
    sys.exit(main())
