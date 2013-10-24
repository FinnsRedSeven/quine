import base64
b64source = 'aW1wb3J0IGJhc2U2NApiNjRzb3VyY2UgPSAnJScKX19zb3VyY2VfXyA9IGJhc2U2NC5iNjRkZWNvZGUoYjY0c291cmNlKS5yZXBsYWNlKCclJywgYjY0c291cmNlLCAxKQoKcHJpbnQgJ3t9JwpwcmludCBfX3NvdXJjZV9fID09IG9wZW4oX19maWxlX18pLnJlYWQoKQo='
__source__ = base64.b64decode(b64source).replace('%', b64source, 1)

print '{}'
print __source__ == open(__file__).read()
