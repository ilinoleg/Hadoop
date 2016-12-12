#!/usr/bin/python

import sys
import os
import re

filterStart = ('Media:', 'Special:', 'Talk:',
               'User:', 'User_talk:',
               'Project:', 'Project_talk:',
               'File:', 'File_talk:',
               'MediaWiki:', 'MediaWiki_talk:',
               'Template:', 'Template_talk:',
               'Help:', 'Help_talk:',
               'Category:', 'Category_talk:',
               'Portal:',
               'Wikipedia:', 'Wikipedia_talk:')

filterEnd = ('.jpg', '.gif', '.png', '.JPG', '.GIF', '.PNG', '.txt', '.ico')

filterT = ('404_error/', 'Main_Page', 'Hypertext_Transfer_Protocol', 'Search')


def cond1 (word):
    for w in filterStart:
        if word.startswith(w):
            return False
    return True


def cond2 (word):
    for w in filterEnd:
        if word.endswith(w):
            return False
    return True


def cond3 (word):
    for w in filterT:
        if word == w:
            return False
    return True


d = os.environ["mapreduce_map_input_file"]
#d = "pagecounts-20160701-000000"
reg = re.compile("pagecounts-(\d{8})")
date = reg.findall(d)[-1]
for line in sys.stdin:
    line = line.strip()
    words = line.split()
    if line.startswith('en') and cond1(words[1]) and words[1][0].isupper():
        if cond2(words[1]):
            if cond3(words[1]):
            	if len(words) == 4:
                	print '%s\t%s\t%s' %  (words[1], words[2], date)