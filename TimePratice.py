import time




import time

time_list = []

start = time.time()

end = time.time()

counting = end - start
while True:
    if sum(time_list) < 5:
        time_list.append(counting)
        print('pants')

    elif sum(time_list) >= 5:
        print('ass')
