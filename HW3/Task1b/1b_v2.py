import hashlib
import codecs

def encrypt_string(hash_string):
    sha_signature = hashlib.sha256(hash_string.encode("utf-8")).hexdigest()
    return sha_signature


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
    hash = []
    hash.append("2e41f7133fd134335f566736c03cc02621a03a4d21954c3bec6a1f2807e87b8a")
    hash.append("7987d2f5f930524a31e0716314c2710c89ae849b4e51a563be67c82344bcc8da")
    hash.append("076f8c265a856303ac6ae57539140e88a3cbce2a2197b872ba6894132ccf92fb")
    hash.append("b1ea522fd21e8fe242136488428b8604b83acea430d6fcd36159973f48b1102e")
    hash.append("fa5700d75974a94dd73f7c5d48e85afa87beba19b873d4eb8d411dd251560321")
    hash.append("326e90c0d2e7073d578976d120a4071f83ce6b7bc89c16ecb215d99b3d51a29b")
    hash.append("269398301262810bdf542150a2c1b81ffe0e1282856058a0e26bda91512cfdc4")
    hash.append("4fbee71939b9a46db36a3b0feb3d04668692fa020d30909c12b6e00c2d902c31")
    hash.append("55c5a78379afce32da9d633ffe6a7a58fa06f9bbe66ba82af61838be400d624e")
    hash.append("5106610b8ac6bc9da787a89bf577e888bce9c07e09e6caaf780d2288c3ec1f0c")

    f = codecs.open('rockyou.txt', encoding='utf-8')

    for line in f:
        line = line.strip()
        for pswd in generate_sister_password(line):
            hash_line = str(encrypt_string(pswd))
            for h_code in hash:
                hash_line = str(encrypt_string(pswd))
                if h_code == hash_line:
                    print(pswd)
