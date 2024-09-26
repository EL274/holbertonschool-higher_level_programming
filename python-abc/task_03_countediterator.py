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


# Testing
if __name__ == "__main__":
    # Instantiate a CountedIterator object using a list
    counted_iter = CountedIterator([10, 20, 30, 40, 50])

    # Iterate over items using a loop
    for item in counted_iter:
        print(item)  # Print the item

    # Use the get_count method to retrieve and print the number of items fetched
    print(f"Total items iterated: {counted_iter.get_count()}")

