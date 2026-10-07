
import base64, hashlib

SEED = 0

CIPHERTEXT_B64 = "WDEE0t3AlOS44tHJ3QKOMxmBIjJzCw=="
ITER = 1 << 20

def _k(seed, n):
    h = str(seed).encode()
    for _ in range(ITER):
        h = hashlib.sha256(h).digest()
    out, c = b"", 0
    while len(out) < n:
        out += hashlib.sha256(h + c.to_bytes(4, "big")).digest(); c += 1
    return out[:n]

ct = base64.b64decode(CIPHERTEXT_B64)
pt = bytes(a ^ b for a, b in zip(ct, _k(SEED, len(ct))))
try:
    print(pt.decode("ascii"))
except UnicodeDecodeError:
    print(pt)
