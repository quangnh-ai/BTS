import redis

r = redis.Redis(
    host='100.73.211.25',
    port=30000,
    password='123456',
    db='0'
)

r.set('aaaa', '123')
print(r.get('aaaa'))