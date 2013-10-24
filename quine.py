from base64 import b64encode

def quinefy(old_filename, new_filename):
    with open(old_filename) as old_file:
        source = old_file.read()

    tmp_source = """import base64
b64source = '{}'
__source__ = base64.b64decode(b64source).format(b64source)

{}"""
    inner = tmp_source.format('{}', source)
    b64inner = b64encode(inner)
    quine = tmp_source.format(b64inner, source)

    with open(new_filename, 'w') as new_file:
        new_file.write(quine)

quinefy('hello_world.py', 'hello_quine.py')
