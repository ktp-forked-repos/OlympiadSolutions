#!/usr/bin/env python2.7
# -*- coding : utf-8 -*-
casos = int(raw_input())
for i in xrange(casos):
	print str(bin(int(raw_input()))).count("1")