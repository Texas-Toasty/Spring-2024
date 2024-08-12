import math


def distance(coord1, coord2):
    x1, y1, z1 = coord1
    x2, y2, z2 = coord2

    dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
    return round(dist, 2)


def get_user_input():
    while True:
        try:
            x1 = float(input("Enter the x-coordinate for the first point: "))
            y1 = float(input("Enter the y-coordinate for the first point: "))
            z1 = float(input("Enter the z-coordinate for the first point: "))

            x2 = float(input("Enter the x-coordinate for the second point: "))
            y2 = float(input("Enter the y-coordinate for the second point: "))
            z2 = float(input("Enter the z-coordinate for the second point: "))

            if not (-1000.0 <= x1 <= 1000.0) or not (-1000.0 <= y1 <= 1000.0) or not (-1000.0 <= z1 <= 1000.0) or \
                    not (-1000.0 <= x2 <= 1000.0) or not (-1000.0 <= y2 <= 1000.0) or not (-1000.0 <= z2 <= 1000.0):
                raise ValueError("Coordinates must be within the bounds -1000.0 and 1000.0.")

            coord1 = (x1, y1, z1)
            coord2 = (x2, y2, z2)
            return coord1, coord2
        except ValueError as e:
            print(f"Invalid input: {e}")
            continue


def main():
    coord1, coord2 = get_user_input()

    dist = distance(coord1, coord2)

    print(f"\nDistance between {coord1} and {coord2}: {dist} units")


if __name__ == "__main__":
    main()
