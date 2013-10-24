import base64
b64source = 'aW1wb3J0IGJhc2U2NApiNjRzb3VyY2UgPSAne30nCl9fc291cmNlX18gPSBiYXNlNjQuYjY0ZGVjb2RlKGI2NHNvdXJjZSkuZm9ybWF0KGI2NHNvdXJjZSkKCnByaW50IF9fc291cmNlX18gPT0gb3BlbihfX2ZpbGVfXykucmVhZCgpCg=='
__source__ = base64.b64decode(b64source).format(b64source)

print __source__ == open(__file__).read()
