def quinefy(old_filename, new_filename):
    with open(old_filename) as old_file:
        source = old_file.read()
    q = '"""'
    text = """q = '{}'\ntext = {}\n{}\nprint text.format(q, q + text + q)"""
    quine = text.format(q, q + text.format('{}', '{}', source) + q, source)
    with open(new_filename, 'w') as new_file:
        new_file.write(quine)

quinefy('hello_world.py', 'hello_quine.py')
