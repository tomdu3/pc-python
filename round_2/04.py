# Nested Dictionary Updater: Develop a function that takes a nested dictionary and updates a value given its key path as a list.

def nested_dict_updater(dict, key_path, value):
    if len(key_path) == 1:
        dict[key_path[0]] = value
        return dict
    return {key_path[0]: nested_dict_updater(dict[key_path[0]], key_path[1:], value)}


dict_original = {'a': {'b': {'c': 1}}}

dict = nested_dict_updater(dict_original, ['a', 'b', 'd'], 2)

print(dict)
