from util import read, write, delete, start, abort, commit

def main():
    data = [{}]
    deleted_keys = set()
    while True:
        line = input("> ")
        info = line.split()
        try:
            info[0] = info[0].upper()
            if info[0] == "QUIT":
                print("Exiting...")
                exit()
            elif info[0] == "READ":
                print(read(data, info[1]))
            elif info[0] == "WRITE":
                write(data, info[1], info[2])
            elif info[0] == "DELETE":
                deleted_key = delete(data, info[1])
                if deleted_key:
                    deleted_keys.add(deleted_key)
            elif info[0] == "START":
                start(data)
            elif info[0] == "COMMIT":
                commit(data, deleted_keys)
                deleted_keys = set()
            elif info[0] == "ABORT":
                abort(data)
                deleted_keys = set()
        except IndexError:
            print("Please check your input and try again")


if __name__ == "__main__":
    main()
