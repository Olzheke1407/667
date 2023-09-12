def map_keywords(**kwargs):
    keys = {}
    for key, value in kwargs.items():
        try:
            hash(key)
        except TypeError:
            key = str(key)
        keys[key] = value
    return keys


result = map_keywords(name="Олжас", age=18, city="Атырау")
print(result)
