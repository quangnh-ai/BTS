import redis

r = redis.Redis(
    host='192.168.1.9',
    port=31850,
    db='0'
)

r.set('foo', 'bar')
r.get('foo')