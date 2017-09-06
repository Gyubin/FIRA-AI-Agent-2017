from gyubin_reader import reader

a = reader()
for i in range(3):
    x, y, id = a.next_batch(32, "train")
    print('{}\n{}\n{}\n\n'.format(x, y, id))
    x, y, id = a.next_batch(10, "val")
    print('{}\n{}\n{}\n\n'.format(x, y, id))
