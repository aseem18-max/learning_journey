def my_generator():
    for i in range(500):
        yield i

gen = mygen()
for j in gen:
    print(next(gen))