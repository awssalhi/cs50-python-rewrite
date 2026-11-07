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
