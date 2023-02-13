// SPDX-License-Identifier: MIT
pragma solidity ^0.6.6;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@chainlink/contracts/src/v0.6/VRFConsumerBase.sol";

contract AdvancedCollectible is ERC721, VRFConsumerBase {
    uint256 tokenCounter; // For the NFT minting
    bytes32 keyhash; // The hash for the node which will provide the random number
    uint256 fee; // The LINK token fee for paying the addresses
    enum Breed {
        PUG,
        SHIBA_INU,
        ST_BERNARD
    }
    uint256 DogAmount = Breed.length;

    constructor(
        address _vrfCoordinator, // The Address for the VRFCoordinator contract in the chain
        address _linkToken, // The Address for the LINKTOKEN in the current chain
        bytes32 _keyhash,
        uint256 _fee
    )
        public
        VRFConsumerBase(_vrfCoordinator, _linkToken)
        ERC721("Dogie", "DOG")
    {
        // We could parametize ERC721 inputs as well
        tokenCounter = 0;
        keyhash = _keyhash; // We already set the node at the beginning
        fee = _fee; // We already set the LINK token fee at the beginning
    }

    mapping(uint256 => Breed) public tokenIdtoBreed;
    mapping(bytes32 => address) public requestIdtoSender;

    function createCollectible() public returns (bytes32) {
        bytes32 requestId = requestRandomness(_keyhash, _fee); // Request a random number from the VRFCoord.
        requestIdtoSender[requestId] = msg.sender; // !!We register the address of the sender for future use!!
    }

    function fulfillRandomness(bytes32 requestId, uint256 randomNumber)
        internal
        override
    {
        Breed breed = Breed(randomNumber % DogAmount); // Sorting out the NFT to be minted!
        uint256 newTokenId = tokenCounter; // Grabbing the tokenId for the Minting (must be unique)
        tokenIdtoBreed[newTokenId] = breed; // Identify the tokenId to your PUP
        address owner = requestIdtoSender[requestId]; // The one who first asked for minting!
        _safeMint(owner, newTokenId); // Mints the NFT and registers it to the owner, mapping to the newTokenId.
        tokenCounter++; // Adds to the tokenCounter in order for the next mint to have a unique id as well.
    }
}
