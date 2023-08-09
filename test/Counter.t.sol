// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

import "forge-std/Test.sol";
import "../src/Counter.sol";

contract CounterTest is Test {
    Counter public counter;

    function setUp() public {
        counter = new Counter();
        counter.setNumber(0);
    }

    function testIncrement() public {
        counter.increment();
        assertEq(counter.number(), 1);
    }

    function addressesWithPrivateKeys(uint8 numSigners)
        public
        returns (address[] memory addresses, uint256[] memory privateKeys)
    {
        string[] memory cmd = new string[](4);
        cmd[0] = "python";
        cmd[1] = "./script/gen_addresses_keys.py";
        cmd[2] = vm.toString(numSigners);
        bytes memory result = vm.ffi(cmd);
        (privateKeys, addresses) = abi.decode(result, (uint256[], address[]));
    }
}

/*
    function addressesWithPrivateKeys(uint8 numSigners)
        public
        returns (address[] memory addresses, uint256[] memory privateKeys)
    {
        string[] memory cmd = new string[](4);
        cmd[0] = "go";
        cmd[1] = "run";
        // must be executed from the parent package
        cmd[2] = "./testCommands/generateAddressesAndKeys.go";
        cmd[3] = vm.toString(numSigners);

        bytes memory result = vm.ffi(cmd);
        (privateKeys, addresses) = abi.decode(result, (uint256[], address[]));
    }
*/
