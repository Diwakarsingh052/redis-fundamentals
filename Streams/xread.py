import redis

r = redis.Redis()

key = 'numbers'

last_id = '0-1'
n_sum = 0

streamDict = {}

while True:

    streamDict[key] = last_id
    msgs = r.xread(streamDict, count=1)

    # print(msgs)

    if not msgs:
        break

    for msg in msgs[0][1]:
        last_id = msg[0]
        n_sum += int(msg[1][b'n'])  # n_sum = n_sum +int(msg[1][b'n'])

print('sum', n_sum)
