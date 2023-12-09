# FreeCodeCamp Arithmetic Arranger Challenge

Welcome to the FreeCodeCamp Arithmetic Arranger Challenge! This project is part of the FreeCodeCamp curriculum and focuses on developing a Python program to arrange and format arithmetic problems.

## Challenge Overview

The challenge involves creating a Python function, `arithmetic_arranger`, that arranges arithmetic problems in a vertical format. The function should handle various error conditions and provide clear and organized output.

## Function Signature:

```python
def arithmetic_arranger(problems, show_answers=False):
    """
    Arrange arithmetic problems vertically.

    Args:
        problems (list): A list of strings representing arithmetic problems.
        show_answers (bool, optional): If True, display the answers along with the problems. Default is False.

    Returns:
        str: A string containing the vertically arranged arithmetic problems.

    Raises:
        ValueError: If the input problems are not correctly formatted.

    Examples:
        >>> arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
        '    32      3801      45      123\n+  698    -    2    + 43    +  49\n-----    ------    ----    -----'

        >>> arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
        '    32         1      9999      523\n+  8    - 3801    + 9999    -  49\n----    ------    ------    -----'

    """
    # Implementation details...
