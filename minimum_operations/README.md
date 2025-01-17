# Minimum Operations

## Problem Description

The goal of this project is to calculate the fewest number of operations required to achieve exactly `n` characters in a text file starting with a single "H" character. The only two operations allowed are:

- **Copy All**: Copies all characters in the file.
- **Paste**: Pastes one character to the file.

### Objective:
Given a number `n`, calculate the fewest number of operations needed to result in exactly `n` "H" characters in the file. If `n` is impossible to achieve, return 0.

### Example:

For `n = 9`, the sequence of operations would be:
H => Copy All => Paste => HH => Paste => HHH => Copy All => Paste => HHHHHH => Paste => HHHHHHHH

The number of operations required is 6.

## Solution Approach

To determine the fewest number of operations, the problem can be broken down by prime factorization. Each prime factor of `n` contributes to the minimum number of operations required. The solution involves repeatedly dividing `n` by its smallest factors and counting the operations.

### Steps:
1. Start with `n = 1`.
2. Copy All (1 → 1) and then use Paste to multiply it by its prime factors.
3. For each factor, the number of operations is equivalent to the factor's value.
4. If `n` is a prime number, it contributes one operation.

### Time Complexity:
The time complexity of this solution is **O(sqrt(n))**, as we only need to check factors up to the square root of `n`.

## How to Run the Code

### Prerequisites:
- Python 3.x should be installed on your system (tested with Python 3.4.3 on Ubuntu 14.04 LTS).

### Steps:
1. Clone the repository:
   ```bash
   git clone https://github.com/kelvintawe12/alu-interview.git
