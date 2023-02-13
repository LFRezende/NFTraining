// SPDX-License-Identifier: MIT
pragma solidity ^0.6.6;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@chainlink/contracts/src/v0.6/VRFConsumerBase.sol";

contract AdvancedCollectible is ERC721, VRFConsumerBase {
    uint256 tokenCounter; // For the NFT minting
    bytes32 keyhash;      // The hash for the node which will provide the random number
    uint256 fee;          // The LINK token fee for paying the addresses
    constructor(
        address _vrfCoordinator, // The Address for the VRFCoordinator contract in the chain
        address _linkToken,      // The Address for the LINKTOKEN in the current chain
        bytes32 _keyhash,
        uint256 _fee
    )
        public
        VRFConsumerBase(_vrfCoordinator, _linkToken)
        ERC721("Dogie", "DOG")
    {
        tokenCounter = 0;
        keyhash = _keyhash;
        fee = _fee;
    }

    function createCollectible(string memory tokenURI) public returns (bytes32) {
        bytes32 requestId = requestRandomness(_keyhash, _fee);
    }
    
}
