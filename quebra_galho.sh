#!/usr/bin/env bash
# coding: utf-8
'''
@author: Memória de Cálculo <memoriadcalculo@gmail.com>
'''
lynx -source "http://www.verbix.com/webverbix/go.php?T1=${1}&D1=22&H1=122" > ${1}.html
lynx -dump ${1}.html

