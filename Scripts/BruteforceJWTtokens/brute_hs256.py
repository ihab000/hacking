import base64, sys
from hmac_sha256 import generate

def transform(key):
    if isinstance(key, int):
        return bytes(key)
    return key.encode()
    
def read_from_file(filename):
    l_strings = list()
    with open(filename, 'r') as f:
        for i in f.readlines():
            l_strings.append(i.rstrip())
    return l_strings

def brute_from_file(msg_file, key_file, with_dot=True):
    l_msges = format_tokens(read_from_file(msg_file), with_dot)
    l_keyes = read_from_file(key_file)
    return_file = list()
    for key in l_keyes:
        responses = list()
        for msg in l_msges:
            resp = brute_hs256(msg, key)
            responses.append(resp)
        return_file.append((key, responses))
    return return_file

def brute_from_file_with_key(msg_file, key, with_dot=True):
    l_msges = format_tokens(read_from_file(msg_file), with_dot)
    return_file = list()
    responses = list()
    for msg in l_msges:
        resp = brute_hs256(msg, key)
        responses.append(resp)
    return_file.append((key, responses))
    return return_file

def brute_hs256(msg, key):
    b_msg = base64.b64decode(msg)
    b_key = transform(key)
    return generate(b_msg, b_key)

def format_tokens(tokens, with_dot=True):
    new_tokens = list()
    if with_dot:
        for i in tokens:
            token = i.split(".")[0] + "." + i.split(".")[1] + "=="
            new_tokens.append(token)
    else:
        for i in tokens:
            new_tokens.append(i.split(".")[0] + i.split(".")[1] + "==") 
    return new_tokens

def print_bruted(bruted, offset=40):
    for key, bruted_vals in bruted:
        if len(key) > offset:
            offset = len(key) + 5
        keystr = key + " "*(offset - len(key))
        for i in bruted_vals:
            print("{}{}".format(keystr,i))

if __name__ == '__main__':
    length = len(sys.argv)
    if length == 3:
        bruted = brute_from_file(sys.argv[1], sys.argv[2])
    elif length == 4:
        bruted = brute_from_file(sys.argv[1], sys.argv[2], False)
    else:
        print("Usage:\npython3 brute_hs256.py [msg_file key_file [add_equels_to_base64]]")
        key = "1557338095"
        print(brute_hs256("eyJhbGciOiJIUzI1NiJ9eyJhZG1pbnVzZXJfaWQiOm51bGwsInVzZXJfaWQiOm51bGwsImFub255bW91cyI6dHJ1ZSwidXNlcnNlc3Npb25faWQiOjExMjc1MjU5fQ==", key))
        sys.exit(0)
    print_bruted(bruted)
