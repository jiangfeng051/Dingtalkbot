#!/usr/bin/python
# -*- coding: UTF-8 -*-
#date:2019/4/4
#Author:jiangfeng

import os
import sys

BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASEDIR)

from src import service

if __name__ == '__main__':
    service.main()