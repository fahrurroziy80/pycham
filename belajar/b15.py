#membuat list (Iterators)

list = [1,2,3,4,5,6]
it = list.__iter__()
el = it.__next__()
while el:
    print(el,end="")
    try:
        el = it.__next__()
    except StopIteration as e:
        print("")
        break





















