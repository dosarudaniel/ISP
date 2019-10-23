import hashlib
import codecs

def encrypt_string(hash_string):
    return hashlib.sha256(hash_string.encode("utf-8")).hexdigest()

def generate_sister_password(pswd):
    pswds = []
    pswds.append(pswd.title())
    pswds.append(pswd.replace('e', '3'))
    pswds.append(pswd.replace('e', '3').title())
    pswds.append(pswd.replace('o', '0'))
    pswds.append(pswd.replace('o', '0').title())
    pswds.append(pswd.replace('i', '1'))
    pswds.append(pswd.replace('i', '1').title())
    pswds.append(pswd.replace('i', '1').replace('o', '0').replace('e', '3'))
    pswds.append(pswd.replace('i', '1').replace('o', '0').replace('e', '3').title())
    pswds.append(pswd.replace('i', '1').replace('e', '3'))
    pswds.append(pswd.replace('i', '1').replace('e', '3').title())
    pswds.append(pswd.replace('o', '1').replace('e', '3'))
    pswds.append(pswd.replace('o', '1').replace('e', '3').title())
    pswds.append(pswd.replace('i', '1').replace('o', '0'))
    pswds.append(pswd.replace('i', '1').replace('o', '0').title())

    return pswds

if __name__ == '__main__':
    # Check https://crackstation.net/
    hashes = []
    hashes.append("2e41f7133fd134335f566736c03cc02621a03a4d21954c3bec6a1f2807e87b8a") # alban1an123
    hashes.append("7987d2f5f930524a31e0716314c2710c89ae849b4e51a563be67c82344bcc8da") #
    hashes.append("076f8c265a856303ac6ae57539140e88a3cbce2a2197b872ba6894132ccf92fb") # 0scar00
    hashes.append("b1ea522fd21e8fe242136488428b8604b83acea430d6fcd36159973f48b1102e") # captpimp
    hashes.append("fa5700d75974a94dd73f7c5d48e85afa87beba19b873d4eb8d411dd251560321") # B3llucc1
    hashes.append("326e90c0d2e7073d578976d120a4071f83ce6b7bc89c16ecb215d99b3d51a29b") # delmar00
    hashes.append("269398301262810bdf542150a2c1b81ffe0e1282856058a0e26bda91512cfdc4") # 6033503
    hashes.append("4fbee71939b9a46db36a3b0feb3d04668692fa020d30909c12b6e00c2d902c31") # 802561
    hashes.append("55c5a78379afce32da9d633ffe6a7a58fa06f9bbe66ba82af61838be400d624e") #
    hashes.append("5106610b8ac6bc9da787a89bf577e888bce9c07e09e6caaf780d2288c3ec1f0c") # 19387

    f = codecs.open('../rockyou.txt', encoding='utf-8')
    for line in f:
        line = line.strip()
        for pswd in generate_sister_password(line):
            hash_line = str(encrypt_string(pswd))
            for h_code in hashes:
                if h_code == hash_line:
                    print(pswd  + " with h=" +  h_code)
                    hashes.remove(h_code)
