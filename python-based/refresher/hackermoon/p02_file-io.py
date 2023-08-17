# OLD

f= open('test.txt') # note default is mode='r'
# do something with f here
f.close()

with open('test.txt') as f: # NEW; no close() needed
    print(f.read())
    # f.read() moves the "cursor" to the end of the file
    assert not f.read()
    f.seek(0)
    assert f.read()
    # f.read() returns a string now (unless test.txt is empty)

print('----------------')
print()

with open('test.txt', 'w') as f:
    # f.read() ERROR do not do this
    f.write('this is a test ninja\n') # note there is no end parameter 
    f.writelines(['line1\n', 'line2\n']) # note no auto newline

    # other modes: a for append, rb for reading-bytes, wb for writing bytes, and r+/w+ for both reading and writing at the same time

