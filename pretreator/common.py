'''
Created on Jan 3, 2013

@author: chunwei
'''
def canfind(strr, s):
    try:
        strr.index(s)
        return True
    except:
        return False