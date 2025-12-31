# SolarWinds Exercise
This is an REPL (read-eval-print loop) exercies that drives a simple
in-memory key/value storage system, which allows for nexted transactiond.
Transactions can be committed or aborted.

EXAMPLE RUN
$ python data.py
> WRITE a hello
> READ a
hello
> START
> WRITE a hello-again
> READ a
> hello-again
> DELETE a
> READ a
key not found: a
> COMMIT
> READ a
key not found: a
> WRITE a once-more
> READ a
once-more
> ABORT
Error: Not in a transaction
> QUIT
Exiting...


# Assumptions
Both ABORT and COMMIT ends a transaction.
WRT DELETE operation, the DELETE operation is carried to the parent transaction
only upon COMMIT, not ABORT

# Enhancement
I added an optional argument, inhert, to the function start for START action.
It is defaulted to False. If it is set to True, it will copy the most recent
transaction to the new transaction as initialization

The current code does not take advantage of this option. One can simply add a
command line option to invoke this option.

### Virtual Env
To create virtural environment, run the following
```bash
$ python -m venv venv
```

To activate virtural environment, run the following
```bash
$ . venv/bin/activate
```

To deactivate virtural environment, run the following
```bash
$ deactivate
```

### Test
To test, run the following
```bash
$ pytest
```

To run individual test, run the following
```bash
$ pytest test_util.py::TestUtil::test_commit_with_delete
```
