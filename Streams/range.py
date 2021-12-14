import redis

r = redis.Redis()

key = 'numbers'

last_id = '0-1'
n_sum = 0


def increment_id(msg_id_bytes):
    t, s = msg_id_bytes.decode("utf-8").split('-')
    t = int(t)
    s = int(s)

    s += 1
    return f'{t}-{s}'


while True:
    msgs = r.xrange(key, min=last_id, max='+', count=5)

    if not msgs:
        break

    for msg in msgs:
        last_id = msg[0]
        n_sum += int(msg[1][b'n'])  # n_sum = n_sum +int(msg[1][b'n'])

    last_id = increment_id(last_id)

print('sum', n_sum)
