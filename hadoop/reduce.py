#!/usr/bin/python
import sys

current_word = None
current_count = 0
word = None
dict = {'20160701':0, '20160702':0, '20160703':0, '20160704':0, '20160705':0, '20160706':0, '20160707':0}

for line in sys.stdin:
    line = line.strip()
    words = line.split()
    word = words[0]
    count = words[1]
    data = words[2]

    try:
        count = int(count)
    except ValueError:
        continue

    if current_word == word:
        current_count += count
        dict[data] += count

    else:
        if current_word and current_count>100000:
            s = str(current_count) + '\t' + str(current_word) + '\t'
            for i in dict:
                s += str(i) + ':' + str(dict[i]) + '\t'
            print(s)
        current_count = count
        current_word = word
        dict = {'20160701':0, '20160702':0, '20160703':0, '20160704':0, '20160705':0, '20160706':0, '20160707':0}
        dict[data] = count

if current_word == word and current_count>100000:
    s = str(current_count) + '\t' + str(current_word) + '\t'
    dict[data] += count
    for i in dict:
        s += str(i) + ':' + str(dict[i]) + '\t'
    print(s)