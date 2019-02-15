def generate_range(n):
    """Generates a range within zero and the given value {n} lazily"""
    i = 0
    while i < n:
        yield i
        i += 1

# the values are lazy-loaded at runtime
for i in generate_range(100):
    print(f"i: {i}")


