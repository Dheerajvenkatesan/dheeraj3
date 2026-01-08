import sys

def sort_tuples():
    data = []
    print("Enter (name, age, height) separated by commas (Press Enter on an empty line to finish):")
    while True:
        line = sys.stdin.readline().strip()
        if not line:
            break
        parts = tuple(line.split(','))
        data.append(parts)
    data.sort(key=lambda x: (x[0], int(x[1]), int(x[2])))

    print(data)

if __name__ == "__main__":
    sort_tuples()