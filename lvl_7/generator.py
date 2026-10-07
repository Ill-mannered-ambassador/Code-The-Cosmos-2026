#!/usr/bin/env python3
# The program that scrambled transmission.bin. Given in full; the driving number is not.
# NOTE: running this FORWARD encrypts. It does not decrypt. Think about what "undo" means.
import sys
P = 2**521 - 1
def multiplier(key):
    return ((pow(key, 3, P) ^ 0x9E3779B97F4A7C15) % P) or 2
def scramble(key, bits):
    A = multiplier(key)
    total = len(bits)
    blocks = [int(bits[i:i+500], 2) for i in range(0, total, 500)]
    enc = [(b * A) % P for b in blocks]
    return enc, total
if __name__ == "__main__":
    key = int(sys.argv[1])
    bits = open("message.bits").read().strip()
    enc, total = scramble(key, bits)
    open("out.bin","w").write("\n".join(map(str,enc))+f"\n#bits={total}\n")
    print("scrambled %d bits with multiplier derived from key" % total)
