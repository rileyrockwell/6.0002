import random

random.seed(9001)
for i in range(random.randint(1, 10)):
	print(random.randint(1, 10))

print("###")

random.seed(9001)
d = random.randint(1, 10)
for i in range(random.randint(1, 10)):
    print(d)

print("###")

random.seed(9001)
d = random.randint(1, 10)
for i in range(random.randint(1, 10)):
    if random.randint(1, 10) < 7:
        print(d)
    else:
        random.seed(9001)
        d = random.randint(1, 10)
        print(random.randint(1, 10))


# supposedly:
# 3
# 1, 1, 1
# 1, 1, 3