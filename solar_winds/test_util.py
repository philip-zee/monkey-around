from unittest import main
from unittest import TestCase

from util import read, write, delete, start, abort, commit


class TestUtil(TestCase):

    def test_read_write(self):
        data = [{}]
        assert len(data[-1]) == 0
        write(data, "key", "value")
        assert len(data[-1]) == 1
        assert read(data, "key") == "value"
        assert read(data, "another_key") == "Key not found: another_key"
        write(data, "key", "value")
        assert len(data[-1]) == 1
        write(data, "another_key", "another_value")
        assert len(data[-1]) == 2


    def test_read_through(self):
        data = [{}]
        assert len(data[-1]) == 0
        write(data, "a", "b")
        # Start a transaction
        start(data)
        write(data, "b", "c")
        assert read(data, "b") == "c"
        assert read(data, "a") == "b"
        # Start another transaction
        start(data)
        write(data, "c", "d")
        assert read(data, "c") == "d"
        # Read through once
        assert read(data, "b") == "c"
        # Read through all the way
        assert read(data, "a") == "b"


    def test_delete(self):
        data = [{}]
        assert len(data[-1]) == 0
        write(data, "key", "value")
        assert len(data[-1]) == 1
        delete(data, "another_key")
        assert len(data[-1]) == 1
        delete(data, "key")
        assert len(data[-1]) == 0


    def test_start(self):
        data = [{}]
        assert len(data) == 1
        start(data)
        assert len(data) == 2


    def test_abort(self):
        data = [{}]
        assert len(data) == 1
        write(data, "key", "value")
        assert read(data, "key") == "value"

        start(data)
        assert len(data) == 2
        write(data, "key", "differnt_value")
        assert read(data, "key") == "differnt_value"

        abort(data)
        assert len(data) == 1
        assert read(data, "key") == "value"

        # Second abort is ignored as there is no parent transaction
        abort(data)
        assert len(data) == 1


    def test_commit(self):
        data = [{}]
        write(data, "key", "value")
        assert read(data, "key") == "value"
        start(data)
        write(data, "another_key", "another_value")
        write(data, "key", "different_value")
        commit(data, set())
        write(data, "key", "different_value")
        write(data, "another_key", "another_value")


    def test_commit_with_delete(self):
        data = [{}]
        deleted = set()
        write(data, "key", "value")
        assert read(data, "key") == "value"
        start(data)
        write(data, "another_key", "another_value")
        assert read(data, "another_key") == "another_value"
        write(data, "key", "different_value")
        assert read(data, "key") == "different_value"
        dk = delete(data, "key")
        if dk:
            deleted.add(dk)
        commit(data, deleted)
        assert read(data, "another_key") == "another_value"
        assert read(data, "key") == "Key not found: key"



if __name__ == "__main__":
    main()

