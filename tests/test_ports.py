#!/usr/bin/env python3

from os import popen

def test():
    output = popen('tports -c').readlines()
    
    assert output[0].replace('\n','').split(' ')[0] == 'target-ports'