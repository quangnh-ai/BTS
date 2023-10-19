import redis

r = redis.Redis(
    host='100.78.237.90',
    port=30000,
    password='123456',
    db='0'
)

r.set('quang', '123')
print(r.get('quang'))