

def get_choices_value(key, choices):
    dic = dict(choices)

    if key in dic:
        return dic[key]
    return key
