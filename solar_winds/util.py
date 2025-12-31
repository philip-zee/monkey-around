def read(stack, key):
    if key in stack[-1].keys():
        return stack[-1][key]
    elif len(stack) > 1:
        value = None
        for i in range(len(stack)):
            if key in stack[i].keys():
                value = stack[i][key]
        if value is None:
            return f"Key not found: {key}"
        else:
            return value
    else:
        return f"Key not found: {key}"


def write(stack, key, val):
    if val:
        stack[-1][key] = val
    else:
        print(f"Nothing written: Need a value")



def delete(stack, key):
    if key in stack[-1].keys():
        stack[-1].pop(key)
        return key
    else:
        print(f"Key not found: {key}")
        return None


def start(stack, inherit=False):
    if inherit:
        stack.append(stack[-1])
    else:
        stack.append({})


def abort(stack):
    if len(stack) > 1:
        stack.pop()
    else:
        print("Error: Not in a transaction")


def commit(stack, deleted):
    if len(stack) <= 1:
        print("Error: Not in a transaction")
    else:
        t = stack.pop()
        # I am choosing to sync all data into the parent
        # transaction regardless of the existence of key
        for k in t:
            write(stack, k, t[k])
    for k in deleted:
        if k in stack[-1].keys():
            stack[-1].pop(k)
