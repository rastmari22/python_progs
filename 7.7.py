shifr_dict=dict()
keys=['md5','sha1','sha224','sha256','sha384','sha512']

stroka=input('Введите строчку: ')
# stroka='питон'
import hashlib
for alg in keys:
    shifr_dict[alg]=hashlib.new(alg,stroka.encode())
# shifr_dict['md5']=hashlib.md5(b'stroka')
# shifr_dict['sha1']=hashlib.sha1(b'stroka')
# shifr_dict['sha224']=hashlib.sha224(b'stroka')
# shifr_dict['sha256']=hashlib.sha256(b'stroka')
# shifr_dict['sha384']=hashlib.sha384(b'stroka')
# shifr_dict['sha512']=hashlib.sha512(b'stroka')
sorted_shifr=dict(sorted(shifr_dict.items()))

for i in sorted_shifr:
    print(i,': ',shifr_dict[i].hexdigest())