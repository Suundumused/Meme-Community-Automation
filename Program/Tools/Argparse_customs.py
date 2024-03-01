import argparse

def tuple_type(arg):
    try:
        values = [int(item) if item.isdigit() else item for item in arg.split(',')]
        return tuple(values)
    
    except ValueError:
        raise argparse.ArgumentTypeError("Invalid tuple format. Must be comma-separated integers/strings without spaces.")
