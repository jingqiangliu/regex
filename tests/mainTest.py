#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    phcat -- a php code analysis tool
    
    author:  wh1t3P1g <wh1t3P1g@gmail.com>
    description:
    
'''
from phcat import main
import os
from lib.core.data import options

if __name__=='__main__':
    options.extension=['c']
    options.language='c'
    options.threads=10
    options.target='/Users/wh1t3P1g/Documents/Fight/iie/alisoftsec/c2'
    main(debug=True)


