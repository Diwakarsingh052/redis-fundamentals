import redis

r = redis.Redis()
r.set("fname","Diwakar")
name_bytes = r.get("fname")

name = name_bytes.decode('utf-8')
msg = f"My name is {name}"

# print(type(name))
print(msg)