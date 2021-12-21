import redis

r = redis.Redis(password="hello")
r.flushdb()

i = 1
pipe = r.pipeline()
while i <= 14:
    name = f"check:{i}"
    data = f"hello:{i}"
    pipe.set(name, data)
    i += 1

pipe.execute()
i = 0
while True:
    i, val = r.scan(i, match="check*")
    print("cursor=", i, val)
    if i == 0:
        break

r.close()
