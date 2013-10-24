def quinefy(old_filename, new_filename):
    with open(old_filename) as old_file:
        source = old_file.read()
    q = '"""'
    b = '{}'
    tmp_source = """q = '{}'
tmp_source = {}
globals()['__source__'] = tmp_source.format(q, q + tmp_source + q)

{}"""
    quine = tmp_source.format(q, q + tmp_source.format(b, b, source) + q, source)
    with open(new_filename, 'w') as new_file:
        new_file.write(quine)

quinefy('hello_world.py', 'hello_quine.py')
