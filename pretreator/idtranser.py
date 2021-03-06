'''
Created on Jan 3, 2013

@author: chunwei
'''
from sets import Set
import common
import os

class IDTranser:
    '''
    parse all trainingset and find all userid in a set
    then sort the set and output to a file
    '''
    def __init__(self, dir='/home/chunwei/NetFlixData/training_set/', outpath='/home/chunwei/NetFlixData/userids.red'):
        self.set = Set()
        self._dir = dir
        self._outpath = outpath
        self._list = None
    
    def load(self):
        files = os.listdir(self._dir)
        for f in files:
            path = os.path.join(self._dir, f)
            f = open(path)
            content = f.read()
            yield content
            f.close()
    
    def parse(self):
        for i,c in enumerate(self.load()):
            lines = c.split('\n')
            for l in lines:
                if len(l.split(',')) < 3: continue
                if common.canfind(l, ':'): continue
                # the line contains userid
                words = l.split(',')
                userid = int(words[0])
                if userid > 2650000:
                    print '.. Error: get userid', userid
                    break
                self.set.add(userid)
            if i % 100 == 0:
                print '.. has parsed %d files' % i
        print '.. begin sort ids'
        print '.. get list'
        self._list = list(self.set)
        print '.. list sort'
        self._list.sort()
        print '.. end parse.'
    
    def tofile(self):
        #write the file
        f = open(self._outpath, 'w')
        #f.writelines([str(s) for s in self._list])
        strr = ''
        for l in [str(s) for s in self._list]:
            strr += l + '\n'
        f.write(strr)
        f.close()
        print '.. succeed output to file : <%s>' % self._outpath
            
if __name__ == '__main__':
    import time
    start = time.time()
    idname =  IDTranser()
    idname.parse()
    idname.tofile()
    end = time.time()
    print '.. spent time: ', end - start
     
