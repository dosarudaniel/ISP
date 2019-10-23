import hashlib
import threading

charset = "abcdefghijklmnopqrstuvwxyz0123456789"
def encrypt_string(hash_string):
    sha_signature = hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature

def crack_4chr(hash):
    for i in range(0, len(charset)):
        for j in range(0, len(charset)):
            for k in range(0, len(charset)):
                for l in range(0, len(charset)):
                    if (encrypt_string(charset[i] + charset[j] + charset[k] + charset[l]) == hash):
                        return charset[i] + charset[j] + charset[k] + charset[l]
    return ""

def crack_5chr(hash):
    for i in range(0, len(charset)):
        for j in range(0, len(charset)):
            for k in range(0, len(charset)):
                for l in range(0, len(charset)):
                    for i1 in range(0, len(charset)):
                        if (encrypt_string(charset[i] + charset[j] + charset[k] + charset[l] + charset[i1]) == hash):
                            return charset[i] + charset[j] + charset[k] + charset[l] + charset[i1]
    return ""

def crack_6chr(hash, nr):
    print("From thread " + str(nr))
    for i in range(0, len(charset)):
        for j in range(0, len(charset)):
            for k in range(0, len(charset)):
                for l in range(0, len(charset)):
                    for i1 in range(0, len(charset)):
                        for j1 in range(0, len(charset)):
                            if (encrypt_string(charset[i] + charset[j] + charset[k] + charset[l] + charset[i1] + charset[j1]) == hash):
                                print(str(nr) + charset[i] + charset[j] + charset[k] + charset[l] + charset[i1] + charset[j1])
                                print(charset[i] + charset[j] + charset[k] + charset[l] + charset[i1] + charset[j1])
                                print(hash)
                                return charset[i] + charset[j] + charset[k] + charset[l] + charset[i1] + charset[j1]
    return ""


if __name__ == '__main__':
    hash = []
    hash.append("7c58133ee543d78a9fce240ba7a273f37511bfe6835c04e3edf66f308e9bc6e5") # xex167
    hash.append("37a2b469df9fc4d31f35f26ddc1168fe03f2361e329d92f4f2ef04af09741fb9") # xontbc
    hash.append("19dbaf86488ec08ba7a824b33571ce427e318d14fc84d3d764bd21ecb29c34ca") # szpn9
    hash.append("06240d77c297bb8bd727d5538a9121039911467c8bb871a935c84a5cfe8291e4") # feh9ay
    hash.append("f5cd3218d18978d6e5ef95dd8c2088b7cde533c217cfef4850dd4b6fa0deef72") # 7rimq7
    hash.append("dd9ad1f17965325e4e5de2656152e8a5fce92b1c175947b485833cde0c824d64") # gi02n
    hash.append("845e7c74bc1b5532fe05a1e682b9781e273498af73f401a099d324fa99121c99") # j67c
    hash.append("a6fb7de5b5e11b29bc232c5b5cd3044ca4b70f2cf421dc02b5798a7f68fc0523") # bgfvf
    hash.append("1035f3e1491315d6eaf53f7e9fecf3b81e00139df2720ae361868c609815039c") # 2vdxm
    hash.append("10dccbaff60f7c6c0217692ad978b52bf036caf81bfcd90bfc9c0552181da85a") # 26i4id


#
# From thread 0
# From thread 1
# From thread 2
#  From thread 3
# From thread 4
# 2feh9ay
# feh9ay
# 06240d77c297bb8bd727d5538a9121039911467c8bb871a935c84a5cfe8291e4
# 0xex167
# xex167
# 7c58133ee543d78a9fce240ba7a273f37511bfe6835c04e3edf66f308e9bc6e5
# 1xontbc
# xontbc
# 37a2b469df9fc4d31f35f26ddc1168fe03f2361e329d92f4f2ef04af09741fb9
# 426i4id
# 26i4id
# 10dccbaff60f7c6c0217692ad978b52bf036caf81bfcd90bfc9c0552181da85a
# 37rimq7
# 7rimq7
# f5cd3218d18978d6e5ef95dd8c2088b7cde533c217cfef4850dd4b6fa0deef72
#
# real	198m0,070s
# user	232m38,898s
# sys	46m20,672s

    threads = list()
    for i in range (0, len(hash)):
        x = threading.Thread(target=crack_6chr, args=(hash[i],i, ))
        threads.append(x)
        x.start()

    for index, thread in enumerate(threads):
        thread.join()

    #
    # for i in range (0, len(hash)):
    #     # print(" >> for " + str(i) + " trying 4 chars")
    #     # # p4 = crack_4chr(hash[i])
    #     # # if p4 == "":
    #     # print(" >> for " + str(i) + " trying 5 chars")
    #     # p5 = crack_5chr(hash[i])
    #     # if p5 == "":
    #     print(" >> for " + str(i) + " trying 6 chars")
    #     p6 = crack_6chr(hash[i])
    #     if p6 == "":
    #         print("Not yet")
    #     else:
    #         print(str(i) + " : " + p6)
    #         #     del hash[i]
    #     #     print("not yet")
    #     # else:
    #     #     print(str(i) + " : " + p5)
    #         # del hash[i]
    #     #     print("not yet")
    #     # else:
    #     #     print(str(i) + " : " + p4)
    #         # del hash[i]
