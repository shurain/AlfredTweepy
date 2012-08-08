#!/usr/local/bin/python
import sys
import re
import unicodedata

import twitter_auth as ta

def tweetq(q):
    q = q.decode('utf-8')
    tweets = []

    #TODO handle a long string with only non-whitespace characters
    tweet = u''
    for word in q.split('\ '):
        tmp = tweet
        tmp = u' '.join((tmp, word))
        # tmp += u' ' + word
        if len(tmp) > 136:
            tweet += ' [' + str(len(tweets)) + ']'
            tweet = unicodedata.normalize('NFC', tweet)
            tweets.append(tweet)
            tweet = u''
        else:
            tweet = tmp
    tweet = unicodedata.normalize('NFC', tweet)
    tweets.append(tweet)

    for t in tweets:
        try:
            ta.api.update_status(t.encode('utf-8'))
            print 'Tweeted:', t.encode('utf-8')
        except:
            print 'Unabled to tweet:', sys.exc_info()[0]

if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit(2) # no argument provided

    query = sys.argv[1] # assume proper escapes
    tweetq(query)
