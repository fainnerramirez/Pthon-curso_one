
#forma 1
set_counties = {'col', 'mex', 'bol', 'bol', 'mex'};

print(set_counties)
print(type(set_counties))

#forma 2
set_counties_2 = set(('col', 'mex', 'bol', 'bol', 'mex'))

print(set_counties_2)
print(type(set_counties_2))

list_numbers = [1,2,3,4,4,4,5,5,6,7]

set_numbers = set(list_numbers)
print(set_numbers)

convert_from_list_numbers = list(set_numbers)
print("lista")
print(convert_from_list_numbers)
