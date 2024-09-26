class VerboseList(list):
    """A list that provides verbose output for modifications."""

    def append(self, item):
        """Add an item to the end of the list and print a notification."""
        super().append(item)
        print(f"Added {item} to the list.")

    def extend(self, iterable):
        """Extend the list by appending elements from the iterable and print a notification."""
        super().extend(iterable)
        print(f"Extended the list with {len(iterable)} items.")

    def remove(self, item):
        """Remove the first occurrence of item from the list and print a notification."""
        print(f"Removing {item} from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Remove and return the item in the list and print a notification."""
        popped_item = super().pop(index)
        print(f"Popped {popped_item} from the list.")
        return popped_item
