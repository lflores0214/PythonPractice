def add5(num=0):
    try:
        if num:
            return int(num) + 5
        else:
            return "please eneter a number"
    except ValueError as err:
        return err
