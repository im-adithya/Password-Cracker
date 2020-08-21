import hashlib

def crack_sha1_hash(hash, use_salts=False):
    f1 = open('top-10000-passwords.txt')
    if use_salts==True:
        for i in f1:
            f2 = open('known-salts.txt')
            for j in f2:
                tobe1 = i.rstrip()+j.rstrip()
                tobe2 = j.rstrip()+i.rstrip()
                if(hashlib.sha1(tobe1.encode('utf-8')).hexdigest() == hash or hashlib.sha1(tobe2.encode('utf-8')).hexdigest() == hash):
                    return i.rstrip()
    else:
        for i in f1:
            if(hashlib.sha1(i.rstrip().encode('utf-8')).hexdigest()==hash):
                return i.rstrip()

    return 'PASSWORD NOT IN DATABASE'