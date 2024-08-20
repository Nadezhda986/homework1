def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)


print_params()
print_params(5)
print_params(0,[5,7,5,7])
print_params('dfhf',False,{'7':7})
#print_params("a:'gjf'",b:'15',c:'godhf',3) # Error
print_params(b = 25), print_params(c = [1,2,3])

values_list = [3,'absdghsyeohd',False]
values_dict = {'a': "cnjf", 'b': 651, 'c': False}
print_params(*values_list)
print_params(**values_dict)


values_list_2 = [2,'qwerty']
print_params(*values_list_2, 42)