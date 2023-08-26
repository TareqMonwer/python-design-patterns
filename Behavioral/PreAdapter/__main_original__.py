from mock_customers import MOCK_CUSTOMERS


def main():
    for customer in MOCK_CUSTOMERS:
        print(
            "Name: %s; Address: %s" %
            (customer.name, customer.address)
        )


if __name__ == "__main__":
    main()

