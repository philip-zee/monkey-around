import pytest

from shipping_package.src.array_transform import rotate_matrix_90_clockwise


class TestArrayTransform:
    """Test cases for the array_transform function."""

    @pytest.mark.parametrize("input_array,expected", [
        ( [[1, 2, 3], [4, 5, 6],[7, 8, 9]], [[7, 4, 1], [8, 5, 2], [9, 6, 3]]),
        ( [[1, 2], [3, 4]], [[3, 1], [4, 2]]),
        ( [[1, 2, 3], [4, 5, 6]], [[4, 1], [5, 2], [6, 3]]),
        ( [[1]], [[1]]),
        ( [], []),
    ])
    def test_rotate_matrix_90_clockwise(self, input_array, expected):
        """Test rotate_matrix_90_clockwise function with various inputs."""

        assert rotate_matrix_90_clockwise(input_array) == expected

