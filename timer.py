import time

current_time = time.time()


with open ('time.txt', 'r') as file:
    last_time = float(file.read())

print(current_time)
print(last_time)

if last_time - current