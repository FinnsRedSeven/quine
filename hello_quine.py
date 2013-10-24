q = '"""'
tmp_source = """q = '{}'
tmp_source = {}
globals()['__source__'] = tmp_source.format(q, q + tmp_source + q)

print __source__
"""
globals()['__source__'] = tmp_source.format(q, q + tmp_source + q)

print __source__
