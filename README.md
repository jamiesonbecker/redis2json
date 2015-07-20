# redis2json

This is a quick and dirty script that dumps redis into RAM and prints out 
corresponding JSON.

## Uses

you can pipe the output through gzip and send it to a file for a quick
non-redis data backup or export/migrate to another system.

For example:

    ./redis_to_json.py | gzip > redis_backup.json.gz

It's also nice for apps that you're putting on ice but don't want to lose the
data for, since the Redis RDB files aren't as convenient.


## Caveats and Notes

*   Unicode support in u() is designed for Python 2.x only. Pulls appreciated!

*   redis().keys() is really bad to use in anything other than a development DB!
    For production, use repeated scans instead.

*   Although you could get a bit more speed by parallelizing, you can't write JSON
    in parallel.
    
*   JSON cannot iterate, so this is entirely in RAM, so plan on using temporarily
    at least 2x size of Redis dataset. (actually, you /could/ iterate by faking
    the outer JSON wrapper of keynames and then using json.dumps() or dump() on
    the values.)
    
*   That is, don't attempt a 1GB Redis dump on less than a 4GB box.  also, it
    will take a while. ;)
    
*   It'd be interesting to do this as JSON dicts for each record in redis,
    iterated over a csv (or sqlite). You can do this easily for whatever you're
    trying to do.
    
*   The "get" method below is incomplete and does not support even a majority of
    Redis data types - it's just a demo to get you started. Feel free to add more.
    
*   The values returned here are guaranteed to be atomic, thanks to Redis'
    awesome design.
    
*   Binary detection is nonexistent. That'd be a cool feature. But why are you
    storing binaries in Redis :)
    
*   Another cool feature would be import to Redis from JSON.
