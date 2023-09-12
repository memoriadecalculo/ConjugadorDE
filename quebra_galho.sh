#!/usr/bin/env bash
# coding: utf-8
'''
@project: ConjugadorDE <http://github.com/memoriadecalculo/ConjugadorDE>
@copyright: Memória de Cálculo (c) 2023 <memoriadcalculo@gmail.com>
'''
lynx -source "http://www.verbix.com/webverbix/go.php?T1=${1}&D1=22&H1=122" > ${1}.html
lynx -dump ${1}.html

