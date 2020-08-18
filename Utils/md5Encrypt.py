import hashlib



def get_md5(s):
    md5=hashlib.md5()
    md5.update(s.encode("utf-8"))
    md5_encrypt=md5.hexdigest()
    return md5_encrypt


if __name__=="__main__":
    print(get_md5("aabbcc"))
