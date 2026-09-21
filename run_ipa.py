import base64, zlib, marshal, types

with open("ipa.protected", "rb") as f:
    code = marshal.loads(zlib.decompress(base64.b64decode(f.read())))

exec(code, {"__name__": "__main__", "__file__": "run_ipa.py"})
