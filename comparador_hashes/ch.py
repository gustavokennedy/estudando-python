import hashlib

arquivo1 = 'a.txt'
arquivo2 = 'b.txt'

hash1 = hashlib.new('ripemd160')

#Compara Hash 1
hash1.update(open(arquivo1, 'rb').read())

#Compara Hash 2
hash2 = hashlib.new('ripemd160')
hash2.update(open(arquivo2, 'rb').read())

if hash1.digest() != hash2.digest():
    print(f'0 arquivo: {arquivo1} é diferente do arquivo: {arquivo2}')
    print('O hash do primeiro arquivo é ', hash1.hexdigest())
    print('O hash do segundo arquivo é ', hash2.hexdigest())
else:
    print(f'O arquivo: {arquivo1} é igual ao arquivo {arquivo2}')
    print('O hash do primeiro arquivo é ', hash1.hexdigest())
    print('O hash do segundo arquivo é ', hash2.hexdigest())