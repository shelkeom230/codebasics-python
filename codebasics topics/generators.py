"""
benefits of generators over iterators

1. no need to write iter() and next() methods
2. no need to raise stopIteratoin exception
"""
def remote_control_next():
    yield "cnn"
    yield "sony"
    yield "zee"

itr=remote_control_next()

'''
print(next(itr))
print(next(itr))
print(next(itr))
'''

while True:
    try:
        print(next(itr))
    except StopIteration as e:
        break 

for c in remote_control_next():
    print(c,end=" ")