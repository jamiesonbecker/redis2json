#! /usr/bin/env python

from redis import StrictRedis as Redis 
import json

def u(s):
    # python 2.x only. see README
    if not isinstance(s, basestring):
        # never fail
        s = str(s)
    if type(s) is unicode:
        return s
    return unicode(s, "utf-8", errors="ignore")

def get(r, k):
    if r.type(k) == 'string':
        return u(r.get(k))
    elif r.type(k) == 'set':
        return [u(v) for v in r.smembers(k)]
    elif r.type(k) == 'list':
        return [u(v) for v in r.lrange(k, 0, -1)]
    elif r.type(k) == 'hash':
        return dict(((u(hk),u(v)) for hk,v in r.hgetall(k).items()))
    else: # this is not complete
        raise Exception, "Please add support for %s" % r.type(k)

if __name__ == "__main__":
    r = Redis()
    results = dict([(k, get(r, k)) for k in  r.keys()])
    print json.dumps(results, sort_keys=True, indent=4, separators=(',', ': '))
