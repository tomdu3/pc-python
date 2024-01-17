# Nested Dictionary Updater: Develop a function that takes a nested dictionary and updates a value given its key path as a list.

def nested_dict_updater(dict, key_path, value):
    last_point = dict
    for key in key_path:
        if key != key_path[-1]:
            last_point = last_point.setdefault(key, {})
            continue
        last_point[key_path[-1]] = value
    return dict


dict_original = {'a': {'b': {'c': 1}}}

dict = nested_dict_updater(dict_original, ['a', 'b', 'd'], 2)

print(dict)
