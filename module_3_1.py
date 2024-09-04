calls = 0
def count_calls():
    calls = 1
    return print(calls)
def string_info(string):
    return print([len(string),string.upper(), string.lower()])

string_info("grsdrgdrgihnihn ih ")

def is_contains(string, list_to_search):
    for i in list_to_search:
        if string == list_to_search[i]:
            return print(True)
        else:
            return print(False)
is_contains("aaa", [1,"aaa",2])
is_contains("aaa", [1,"rrr",2])
count_calls()