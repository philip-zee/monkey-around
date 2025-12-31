Somethings in life are meant to be fun.

## Projects

This repository contains multiple Python projects for learning and practice.

### 1. shipping_package

A project for managing and analyzing shipping packages with utilities for array transformations.

**Features:**
- `ShippingPackage` class for categorizing packages based on dimensions (bulky) and mass (heavy)
- Array transformation utilities (e.g., matrix rotation)
- Comprehensive test suite with pytest

**Structure:**
```
shipping_package/
├── src/
│   ├── shipping_package.py
│   └── array_transform.py
├── test/
│   ├── test_shipping_package.py
│   └── test_array_transform.py
└── pyproject.toml
```

**Setup:**
```bash
cd shipping_package
uv sync --all-extras
uv run pytest
```

### 2. solar_winds

A REPL (read-eval-print loop) exercise that implements an in-memory key/value storage system with support for nested transactions.

**Features:**
- Key/value storage system
- Nested transaction support (START, COMMIT, ABORT)
- Transaction inheritance option
- Interactive REPL interface

**Commands:**
- `READ key` - Read a value from storage
- `WRITE key value` - Write a key-value pair
- `DELETE key` - Delete a key from storage
- `START` - Begin a new transaction
- `COMMIT` - Commit current transaction
- `ABORT` - Abort current transaction
- `QUIT` - Exit the program

**Files:**
- `data.py` - Main REPL entry point
- `util.py` - Utility functions for storage operations
- `test_util.py` - Tests for utility functions

**Setup:**
```bash
cd solar_winds
python -m venv venv
source venv/bin/activate  # On macOS/Linux
python data.py
```

