
def myield(num):
    yield test(num, callback=myield)
    for p in [1,2,3,4]:
        yield test(p, callback=test2)

def test(num, callback):
    return 'test'

def test2():
    return 'test2'

for p in myield(6):
    print(p)
    

