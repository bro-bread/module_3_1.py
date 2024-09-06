def count_calls():
    calls = 0
    calls = calls + 1
    return print(calls)

def string_info(string):
    return print([len(string),string.upper(), string.lower()]), count_calls(), print(" ")

def is_contains(string, list_to_search): # FFFFFFFFFFFFFFFFFFFFFFFF
    wow = (len(list_to_search))
    for i in range(1,wow):
            if string == list_to_search[i] or string.upper() == list_to_search[i] or string.lower() == list_to_search[i]:
                return print(True), count_calls(), print(" ")
            else:
                return print(False), count_calls(), print(" ")

string_info("grsdrgdrgihnihn ih ")
is_contains("abcd", [1,"abcd"])
is_contains("abcd", [1,"abcd"])
is_contains("abc", [1,"abca"])
count_calls()
