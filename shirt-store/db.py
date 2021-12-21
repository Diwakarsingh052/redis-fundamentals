import redis

r = redis.Redis()

products = [
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

id = 1
pipe = r.pipeline()

for p in products:
    key = f"shirt:{id}"
    print(p)
    for field, value in p.items():
        pipe.hset(key, field, value)
    id += 1

pipe.execute()
r.close()
