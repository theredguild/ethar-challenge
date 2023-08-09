// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

import "forge-std/Test.sol";
import "forge-std/console.sol";
import "../src/MultiSig.sol";

contract MultiSigTest is Test {
    MultiSig public multisig;
    address[] public signers;

    uint8 constant GROUP0_QUORUM = 2;
    uint8 constant GROUP1_QUORUM = 1;
    
    // all groups have the root as parent
    uint8 constant GROUP0_PARENT = 0;
    uint8 constant GROUP1_PARENT = 0;
    
    uint8 constant MAX_NUM_GROUPS = 2;

    uint8 constant SIGNERS_NUM = 4;
    uint8 constant NUM_SUBGROUPS = 1;

    uint8[MAX_NUM_GROUPS] s_testGroupQuorums;
    uint8[MAX_NUM_GROUPS] s_testGroupParents;

    uint8[] s_signerGroups;
    address[] s_testSigners;
    bytes32[] s_priv_keys;

    MultiSig.Config s_testConfig;
    MultiSig.Call[] internal s_calls;
    address internal constant MULTISIG_OWNER = 0x1232117A6dEd3a4B844206D8f892e2733A71c843;

    bytes32 internal constant NO_PREDECESSOR = bytes32("");
    bytes32 internal constant EMPTY_SALT = bytes32("");

    function setUp() public {
        vm.startPrank(MULTISIG_OWNER);
        multisig = new MultiSig();
        (s_testSigners, s_priv_keys) = addressesAndPrivKey();
        
        // assign the required quorum in each group
        s_testGroupQuorums[0] = GROUP0_QUORUM;
        s_testGroupQuorums[1] = GROUP1_QUORUM;

        // assign signers to groups
        for (uint8 i = 1; i <= SIGNERS_NUM; i++) {
            // plus one because we don't want signers in root group
            if (i < 2) {
                s_signerGroups.push(0);
            }
            else {
                s_signerGroups.push(1);
            }
        }

        for (uint8 i = 0; i < SIGNERS_NUM; i++) {
            s_testConfig.signers.push(
                MultiSig.Signer({
                    addr: s_testSigners[i],
                    index: i,
                    group: s_signerGroups[i]
                })
            );
        }
        s_testConfig.groupQuorums = s_testGroupQuorums;
        s_testConfig.groupParents = s_testGroupParents;

        multisig.setConfig(
            s_testSigners, s_signerGroups, s_testGroupQuorums, s_testGroupParents
        );
        
        vm.stopPrank();
    }

    function test_executeBatch() public {
        vm.startPrank(address(1));
        vm.deal(address(multisig), 2);
        
        MultiSig.Call[] memory call;
        call = _singletonCalls( MultiSig.Call({ target: address(1), value: 1 , data: "0x"}));
        bytes32 id = multisig.hashOperationBatch(call, NO_PREDECESSOR, EMPTY_SALT);
        MultiSig.Signature[] memory signatures = signBatch( s_priv_keys,id);
        multisig.executeBatch( call , NO_PREDECESSOR, EMPTY_SALT, signatures);

        vm.stopPrank();
    }


    function addressesAndPrivKey()
        public
        returns (address[] memory addresses, bytes32[] memory privKeys)
    {
        string[] memory cmd = new string[](2);
        cmd[0] = "python";
        cmd[1] = "./script/gen_addresses_keys.py";
        bytes memory result = vm.ffi(cmd);
        (addresses, privKeys) = abi.decode(result, (address[], bytes32[]));
    }
    
    function _singletonCalls(MultiSig.Call memory call)
        internal
        pure
        returns (MultiSig.Call[] memory)
    {
        MultiSig.Call[] memory calls = new MultiSig.Call[](1);
        calls[0] = call;
        return calls;
    }

    function signBatch(bytes32[] storage privKeys, bytes32 id) internal returns (MultiSig.Signature[] memory result) {

        result = new MultiSig.Signature[](SIGNERS_NUM);
        for (uint256 i = 0; i < SIGNERS_NUM; i++) {
            (uint8 v, bytes32 r, bytes32 s) = vm.sign(uint256(privKeys[i]), id);
            address signer = ecrecover(id, v, r, s);
            console.logAddress(signer);
            assertTrue(signer == s_testSigners[i], "invalid signature");
            result[i] = MultiSig.Signature({v: v, r: r, s: s});
        }
        return result;
    }
}

