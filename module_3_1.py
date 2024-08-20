calls = 0
def count_calls():
   global calls
   calls+=1

def string_info(string):
   count_calls()
   return (len(string), string.upper(), string.lower())

def is_contains(str_, list_to_search):
   count_calls()
   is_in_list = False
   str_ = str_.lower()
   for i in list_to_search:
      if str_ == i.lower():
         is_in_list = True
   return is_in_list


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)


