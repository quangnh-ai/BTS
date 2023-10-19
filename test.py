import redis

r = redis.Redis(
    host='100.78.237.90',
    port=30000,
    password='123456',
    db='0'
)

r.set('foo', 'bar')
print(r.get('foo'))