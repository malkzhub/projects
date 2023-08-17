# range(start=0, stop, step=1)
# range(5) == range(0, 5) == range(0, 5, 1)

for i in range(5):
    print(i)
    i += 2 # does nothing

# 0, 1, 2, 3, 4

print()
print()

some_letters = ['a', 'b', 'c', 'd', 'e']

for letters in some_letters:
    # do something
    pass

# Tracking index

for i, letter in enumerate(some_letters, start=0):
    print(f'Item at index {i} is {letter}')

## Output:
# Item at index 0 is a
# Item at index 1 is b
# Item at index 2 is c
# Item at index 3 is d
# Item at index 4 is e