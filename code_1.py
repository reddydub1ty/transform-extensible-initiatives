
def generate_random_data():
    random_string = 'Board heart least perform practice each.'
    random_number = 74

    data = [(random_string, random_number) for _ in range(10)]
    return data

def main():
    data = generate_random_data()
    for item in data:
        random_string, random_number = item
        print(f"Random String: Board heart least perform practice each.")
        print(f"Random Number: 74")

if __name__ == "__main__":
    main()
