# Shipping Package Project

A Python project for managing and analyzing shipping packages with utilities for array transformations.

## Project Structure

```
shipping_package/
├── src/
│   ├── shipping_package.py      # ShippingPackage class for package analysis
│   └── array_transform.py        # Array transformation utilities
├── test/
│   ├── test_shipping_package.py  # Tests for ShippingPackage class
│   └── test_array_transform.py   # Tests for array transform functions
├── pyproject.toml                # Project configuration with uv package management
└── README.md                     # This file
```

## Features

### ShippingPackage Class
The `ShippingPackage` class represents a shipping package with the following attributes and methods:

**Attributes:**
- `width` - Package width dimension
- `height` - Package height dimension
- `length` - Package length dimension
- `mass` - Package weight/mass

**Methods:**
- `is_bulky()` - Determines if package is bulky (dimension > 150 or volume ≥ 1,000,000)
- `is_heavy()` - Determines if package is heavy (mass > 20)
- `sort()` - Categorizes package as REJECT (bulky AND heavy), SPECIAL (bulky OR heavy), or STANDARD (neither)

### Array Transform Utilities
- `rotate_matrix_90_clockwise()` - Rotates a 2D matrix 90 degrees clockwise

## Setup and Installation

### Prerequisites
- Python 3.8 or higher
- [uv](https://github.com/astral-sh/uv) package manager

### Installation

```bash
# Clone the repository
cd shipping_package

# Sync dependencies
uv sync --all-extras
```

## Running Tests

```bash
# Run all tests
uv run pytest -v

# Run specific test file
uv run pytest test/test_shipping_package.py -v

# Run with coverage
uv run pytest --cov=src
```

## Development

The project uses the following tools:
- **pytest** - Testing framework
- **black** - Code formatter
- **ruff** - Linter
- **uv** - Package manager and Python version manager

