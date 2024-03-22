class User:
    def __init__(self, name, national_id):
        self.name = name
        self.national_id = national_id


def main():
    User("ali", "1234")
    User("seyed", "4568")


if __name__ == "__main__":
    main()
