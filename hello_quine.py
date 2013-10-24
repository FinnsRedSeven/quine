import base64
q = '"""'
b64source = """aW1wb3J0IGJhc2U2NApxID0gJ3t9JwpiNjRzb3VyY2UgPSB7fQpfX3NvdXJjZV9fID0gYmFzZTY0LmI2NGRlY29kZShiNjRzb3VyY2UpLmZvcm1hdChxLCBxICsgYjY0c291cmNlICsgcSkKCnByaW50IF9fc291cmNlX18gKyAiIiIgIiIiCg=="""
__source__ = base64.b64decode(b64source).format(q, q + b64source + q)

print __source__ + """ """
