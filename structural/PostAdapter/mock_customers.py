from structural.PostAdapter.customer_adapter import CustomerAdapter
from customer import Customer


MOCK_CUSTOMERS = (
    CustomerAdapter(Customer("Ahmed", "Nikunja 1, Dhaka")),
    CustomerAdapter(Customer("Shahariar", "Mirpur, Dhaka")),
    CustomerAdapter(Customer("Jahid", "London, United Kingdom")),
)
