for i in filter(lambda x: x % 2, range(1, 10+1)):
    print(i)

some_str = 'aaAbbB C F DDd EEe'
for i in filter(lambda x: x.islower(), some_str):
    print(i)