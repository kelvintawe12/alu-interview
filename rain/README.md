# Rainwater Retention

## Allowed Editors
- vi
- vim
- emacs

## Environment
- All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
## Tasks

### 0. Rain (mandatory)
Given a list of non-negative integers representing the heights of walls with unit width 1, as if viewing the cross-section of a relief map, calculate how many square units of water will be retained after it rains.

#### Prototype
```python
def rain(walls):
    """
    Calculate the amount of rainwater retained.

    Args:
        walls (list): A list of non-negative integers representing the heights of walls.

    Returns:
        int: Total amount of rainwater retained.
    """
```

- `walls` is a list of non-negative integers.
- Return: Integer indicating total amount of rainwater retained.
- Assume that the ends of the list (before index 0 and after index `walls[-1]`) are not walls, meaning they will not retain water.
- If the list is empty return 0.

#### Example
```python
jesse@ubuntu:~/$ cat 0_main.py
#!/usr/bin/python3
"""
0_main
"""
rain = __import__('0-rain').rain

if __name__ == "__main__":
    walls = [0, 1, 0, 2, 0, 3, 0, 4]
    print(rain(walls))
    walls = [2, 0, 0, 4, 0, 0, 1, 0]
    print(rain(walls))

jesse@ubuntu:~/$ 
jesse@ubuntu:~/$ ./0_main.py
6
6
jesse@ubuntu:~/$ 
```

#### Visual Representation
- Walls: `[0, 1, 0, 2, 0, 3, 0, 4]`

- Walls: `[2, 0, 0, 4, 0, 0, 1, 0]`

## Repository
- GitHub repository: `alu-interview`
- Directory: `rain`
- File: `0-rain.py`