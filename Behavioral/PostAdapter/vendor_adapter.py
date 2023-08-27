from Behavioral.PostAdapter.abs_adapter import AbsAdapter


class VendorAdapter(AbsAdapter):
    @property
    def name(self):
        return self.adaptee.name

    @property
    def address(self):
        return '{} {}'.format(
            self.adaptee.number,
            self.adaptee.street
        )
