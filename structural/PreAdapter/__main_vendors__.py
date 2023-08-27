from mock_customers import MOCK_CUSTOMERS
from mock_vendors import MOCK_VENDORS
TYPE = "vendors"


def main():
    if TYPE == "vendors":
        for vendor in MOCK_VENDORS:
            print("Name: %s; Address: %s %s" %
                  (vendor.name, vendor.number, vendor.street))

    elif TYPE == "customers":
        for customer in MOCK_CUSTOMERS:
            print(
                "Name: %s; Address: %s" %
                (customer.name, customer.address)
            )
    else:
        raise ValueError("Incorrect type: " + TYPE)


if __name__ == "__main__":
    main()

