def all_thing_is_obj(object: any) -> int:
    if isinstance(object, (list)):
        print("List : <class 'list'>")
    elif isinstance(object, (tuple)):
        print("Tuple : <class 'tuple'>   ")
    elif isinstance(object, (set)):
        print("Set : <class 'set'>")
    elif isinstance(object, (dict)):
        print("Dict : <class 'dict'>")
    elif isinstance(object, (str)):
        print(f"{object} is in the kitchen : <class 'str'>")
    else:
        print("Type not found")
    return 42
