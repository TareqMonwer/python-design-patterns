from mock_customers import MOCK_CUSTOMERS
from mock_vendors import MOCK_VENDORS

ALL_CUSTOMERS = MOCK_CUSTOMERS + MOCK_VENDORS


def main():
    for customer in ALL_CUSTOMERS:
        print(
            "Name: %s; Address: %s" %
            (customer.name, customer.address)
        )


if __name__ == "__main__":
    main()

