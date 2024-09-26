class CountedIterator:
    """Iterator that counts the number of items iterated."""

    def __init__(self, iterable):
        """Initialize the iterator and a counter."""
        self.iterator = iter(iterable)
        self.counter = 0

    def get_count(self):
        """Return the current count of items iterated."""
        return self.counter

    def __next__(self):
        """Fetch the next item and increment the counter."""
        try:
            item = next(self.iterator)
            self.counter += 1
            return item
        except StopIteration:
            raise StopIteration  # This will stop the iteration
