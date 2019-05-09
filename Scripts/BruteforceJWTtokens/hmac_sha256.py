import hmac, hashlib, base64


def generate(msg, key):
    digest = hmac.new(key, msg=msg, digestmod=hashlib.sha256).digest()
    return base64.b64encode(digest).decode()

