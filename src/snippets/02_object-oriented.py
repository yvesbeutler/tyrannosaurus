class CountingClicker:
    """A simple clicker which may be used at the door to track how
    many people entered the room.
        
        int:  count
        func: click(int)
        func: read()
    """

    # constructor
    def __init__(self, count = 0):
        self.count = count
    
    # defines the string representation of the class
    def __repr__(self):
        return f"CountingClicker(count={self.count})"

    def click(self, step = 1):
        """Increases the counter by a given value"""
        self.count += step
    
    def read(self):
        """Shows current counting state"""
        return self.count

# Create an instance and assert some functionality
clicker = CountingClicker()

assert clicker.read() == 0, "The clicker should start at zero"

clicker.click()
assert clicker.read() == 1, "The clicker should increase by one by default"

clicker.click(5)
assert clicker.read() == 6, "The clicker should increase by five"

print(clicker.read(), "people entered the room.")
