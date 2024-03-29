import hashlib
import codecs

def encrypt_string(hash_string):
    return hashlib.sha256(hash_string.encode("utf-8")).hexdigest()

if __name__ == '__main__':
    # Check https://crackstation.net/
    hashes = []
    hashes.append(tuple(("962642e330bd50792f647c1bf71895c5990be4ebf6b3ca60332befd732aed56c", "b9"))) # albanian123
    hashes.append(tuple(("8eef79d547f7a6d6a79329be3c7035f8e377f9e629cd9756936ec233969a45a3", "be"))) # thesims9
    hashes.append(tuple(("e71067887d50ce854545afdd75d10fa80b841b98bb13272cf4be7ef0619c7dab", "bc"))) # jasnic1
    hashes.append(tuple(("889a22781ef9b72b7689d9982bb3e22d31b6d7cc04db7571178a4496dc5ee128", "72"))) # atychi1
    hashes.append(tuple(("6a16f9c6d9542a55c1560c65f25540672db6b6e121a6ba91ee5745dabdc4f208", "9f"))) # solkingfran
    hashes.append(tuple(("2317603823a03507c8d7b2970229ee267d22192b8bb8760bb5fcef2cf4c09edf", "17"))) # kapono
    hashes.append(tuple(("c6c51f8a7319a7d0985babe1b6e4f5c329403d082e05e83d7b9d0bf55876ecdc", "94"))) # kaylahh1
    hashes.append(tuple(("c01304fc36655dd37b5aa8ca96d34382ed9248b87650fffcd6ec70c9342bf451", "7f"))) # kennethix
    hashes.append(tuple(("cff39d9be689f0fc7725a43c3bdc7f5be012c840b9db9b547e6e3c454a076fc8", "2e"))) # steele99
    hashes.append(tuple(("662ab7be194cee762494c6d725f29ef6321519035bfb15817e84342829728891", "24"))) # born03101991#

    # TODO unxip the rockyou.zip
    f = codecs.open('../rockyou.txt', encoding='utf-8')
    for line in f:
        line = line.strip()
        for h_code in hashes:
            hash_line = str(encrypt_string(line + h_code[1]))
            if h_code[0] == hash_line:
                print(line  + " with h=" +  h_code[0])
                hashes.remove(h_code)
