import hashlib
from random import randint
import sys
import binascii
import asyncio
import websockets

EMAIL = "your.email@epfl.ch"
PASSWORD = "correct horse battery staple"
# H = sha256
N = 0xEEAF0AB9ADB38DD69C33F80AFA8FC5E86072618775FF3C0B9EA2314C9C256576D674DF7496EA81D3383B4813D692C6E0E0D5D8E250B98BE48E495C1D6089DAD15DC7D7B46154D6B6CE8EF4AD69B15D4982559B297BCF1885C529F566660E57EC68EDBC3C05726CC02FD4CBF4976EAA9AFD5138FE8376435B9FC61D2FC0EB06E3
g = 2
salt = 2

async def PAKE_client():
    uri = "ws://127.0.0.1:5000/"
    async with websockets.connect(uri) as websocket:
        await websocket.send(EMAIL.encode())
        print(f"> {EMAIL}")

        utf8_salt = await websocket.recv()
        bigendian_bytes_salt = binascii.unhexlify(utf8_salt)
        salt = int.from_bytes(bigendian_bytes_salt, 'big')
        print(f"< {salt}")

        print("    salt = ",salt, file=sys.stderr)

        a = 413423 # TODO: randint(32) # generate a number from 32 random bytes
        A = (g**a)%N

        bigendian_array_A = A.to_bytes((A.bit_length() + 7) // 8, 'big')
        utf8_hexadecimalstring_A = binascii.hexlify(bigendian_array_A).decode()
        await websocket.send(utf8_hexadecimalstring_A)
        print(f"> {A}")

        # receive B
        utf8_B = await websocket.recv()
        bigendian_bytes_B = binascii.unhexlify(utf8_B)
        B = int.from_bytes(bigendian_bytes_B, 'big')
        print(f"< {B}")

        # u = H(A || B)
        h1 = hashlib.sha256()
        h1.update(bigendian_array_A)
        h1.update(bigendian_bytes_B)
        print(h1.digest(), file=sys.stderr)
        u = int(h1.hexdigest(), 16)
        print(u, file=sys.stderr)

        # h2 = H(EMAIL || ":" || PASSWORD)
        h2 = hashlib.sha256()
        h2.update(EMAIL.encode())
        h2.update(":".encode())
        h2.update(PASSWORD.encode())
        # print(h2.digest(), file=sys.stderr)

        # x = H(salt || H(EMAIL || ":" || PASSWORD))
        h3 = hashlib.sha256()
        h3.update(bigendian_bytes_salt)
        h3.update(h2.digest())
        x = int(h3.hexdigest(), 16)

        S = (B - g**x)**((a+u*x)%N)
        bigendian_array_S = S.to_bytes((A.bit_length() + 7) // 8, 'big')


        h4 = hashlib.sha256()
        h4.update(bigendian_array_A)
        h4.update(bigendian_bytes_B)
        h4.update(bigendian_bytes_S)

        # Validation: send H(A || B || S) to the server
        await websocket.send(h4.digest().decode())


asyncio.get_event_loop().run_until_complete(PAKE_client())


if __name__ == '__main__':
    print("Client starts...")
