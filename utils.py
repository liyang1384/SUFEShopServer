def delete_null(data):
    for key in list(data.keys()):
        if not data.get(key):
            data.pop(key)
    return data