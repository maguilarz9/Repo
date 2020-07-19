#Testing Commit

whateverList= ['a',5,'b',8,'c',2]

while whatever_iterator:
    try:
        value = next(whatever_iterator)
        print(value)
    except StopIteration:
        print("End of iterator")
        break
