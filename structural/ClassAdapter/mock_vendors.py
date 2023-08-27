from structural.PostAdapter.vendor_adapter import VendorAdapter
from vendor import Vendor


MOCK_VENDORS = (
    VendorAdapter(Vendor("Daraz", 1, 1209)),
    VendorAdapter(Vendor("Alibaba", 2, 2323)),
    VendorAdapter(Vendor("Amazon", 3, 3534)),
)
