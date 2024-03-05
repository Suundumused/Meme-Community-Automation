def arg_message(args):
    try:
        if len(args) > 0:
            return args[-1]
    except:
        return args
