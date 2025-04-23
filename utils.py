def log_operation(op_name, a, b=None):
    if b is not None:
        print(f"Performing {op_name} on {a} and {b}")
    else:
        print(f"Performing {op_name} on {a}")
