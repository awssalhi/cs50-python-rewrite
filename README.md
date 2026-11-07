# CS50 Problem Set 6: Python rewrites

Two programs I first wrote in C, rewritten in Python.

## Mario: C vs. Python

<table>
<tr>
<th>C (mario.c, 33 lines)</th>
<th>Python (mario.py, 24 lines)</th>
</tr>
<tr>
<td>

```c
#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int height;

    // Re-prompt until height is 1 to 8
    do
    {
        height = get_int("Height: ");
    }
    while (height < 1 || height > 8);

    // Outer loop: rows 1 up to height
    for (int i = 1; i <= height; i++)
    {
        // Print (height - i) leading spaces
        for (int j = 0; j < height - i; j++)
        {
            printf(" ");
        }

        // Print (i) hashes
        for (int k = 0; k < i; k++)
        {
            printf("#");
        }

        // Move to the next line
        printf("\n");
    }
}
```

</td>
<td>

```python
# Print a right-aligned half-pyramid of the height the user chooses (1 to 8)


def main():
    height = get_height()
    for row in range(1, height + 1):
        # " " * n makes n spaces; "#" * n makes n hashes.
        # One print per row replaces the two inner loops from the C version.
        print(" " * (height - row) + "#" * row)


def get_height():
    # Keep asking until we get an integer from 1 to 8
    while True:
        try:
            height = int(input("Height: "))
        except ValueError:
            # Text like "abc" or "1.5" lands here, so ask again
            continue
        if 1 <= height <= 8:
            return height


main()
```

</td>
</tr>
</table>

**What changed:** two inner loops became `" " * n + "#" * n`, the `do...while` became `while True` with `try/except`, and type declarations, headers, and braces disappeared.

## Hello

```python
# Ask the user for their name, then greet them
name = input("What is your name? ")
print(f"hello, {name}")
```

Original C version: [cs50-pset1](https://github.com/awssalhi/cs50-pset1)
