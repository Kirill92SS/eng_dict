def func(**args):
    for i , j in args.items():
        print(i, j)


dct = {'i': 'am',
       'you': 'are'}
lst = [1, 2, 3, 4]
func(**dct)
