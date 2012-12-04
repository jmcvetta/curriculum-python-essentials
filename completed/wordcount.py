#!/usr/bin/env python
#
# This is Free Software, released under the terms of the X11 License.
# See http://directory.fsf.org/wiki/License:X11 for details.

'''
Lab - Book Stats

* Download the book text from:  http://tinyurl.com/sbtrain-2-cities.  You can
  download it manually; no need to make the program do that.
* Report the number of words in the book.
* Report the top ten most used words in the book.
'''

import re
from collections import Counter

def main():
    wordcounter = Counter()
    wordfinder = re.compile(r'[\w-]+')
    with open('pg98.txt', 'r') as book:
        for line in book:
            words = wordfinder.findall(line)
            for word in words:
                wordcounter[word.lower()] += 1
    #print wordcounter
    total_words = sum(wordcounter.values())
    sortedwords = sorted(wordcounter.items(),
        key=lambda x: x[1], reverse=True)
    print 'Total words: %s' % total_words
    print 'Top 10 Words:'
    for item in sortedwords[:10]:
        print '\t %-10s (%s)' % item


if __name__ == '__main__':
    main()
