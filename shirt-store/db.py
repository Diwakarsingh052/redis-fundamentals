import redis

r = redis.Redis()

product = [
    {
        "color": "black",
        "price": 49.99,
        "style": "fitted",
        "quantity": 5,
        "nPurchased": 0,

    },

    {
        "color": "maroon",
        "price": 60,
        "style": "Office Shirt",
        "quantity": "6",
        "nPurchased": 0,
    },

    {
        "color": "Pink",
        "price": 79.99,
        "style": "Over Shirt",
        "quantity": "1",
        "nPurchased": 0,
    }

]

shirts = dict()
id = 1
for i in product:
    key = f"shirt:{id}"
    shirts[key] = i
    id += 1

print(shirts)

r.flushdb()  # For Development Environment only

pipe = r.pipeline()

for s_id, shirt in shirts.items():
    for field, value in shirt.items():
        pipe.hset(s_id, field, value)

pipe.execute()

r.close()
