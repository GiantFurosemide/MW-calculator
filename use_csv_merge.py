import csv_merge as cs

file_path = '/Users/wangmu/Desktop/20181222'

di = cs.make_it_dict(file_path)
n=0
for x, y in di.items():
    if "exit code 1" in y:
        print(x,"exit code 1")
    else:
        print(x, len(y))
    n += 1
print(n)
