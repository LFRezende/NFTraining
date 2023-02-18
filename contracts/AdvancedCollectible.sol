// SPDX-License-Identifier: MIT
pragma solidity ^0.6.6;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@chainlink/contracts/src/v0.6/VRFConsumerBase.sol";

contract AdvancedCollectible is ERC721, VRFConsumerBase {
    uint256 public tokenCounter; // For the NFT minting
    bytes32 public keyhash; // The hash for the node which will provide the random number
    uint256 public fee; // The LINK token fee for paying the addresses
    enum Breed {
        PUG,
        SHIBA_INU,
        ST_BERNARD
    }
    uint256 DogAmount = 3;

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
    event requestedCollectible(bytes32 indexed requestId, address requester);
    event breedAssigned(uint256 indexed tokenId, Breed breed);

    function createCollectible() public returns (bytes32) {
        bytes32 requestId = requestRandomness(keyhash, fee); // Request a random number from the VRFCoord.
        requestIdtoSender[requestId] = msg.sender; // !!We register the address of the sender for future use!!
        emit requestedCollectible(requestId, msg.sender); // Good practice of programming.
    }

    function fulfillRandomness(bytes32 requestId, uint256 randomNumber)
        internal
        override
    {
        require(true == false, "ARRIVED!");
        Breed breed = Breed(randomNumber % DogAmount); // Sorting out the NFT to be minted!
        uint256 newTokenId = tokenCounter; // Grabbing the tokenId for the Minting (must be unique)
        tokenIdtoBreed[newTokenId] = breed; // Identify the tokenId to your PUP
        emit breedAssigned(newTokenId, breed); // Emit event that it has been bred! Remap --> emit event.
        address owner = requestIdtoSender[requestId]; // The one who first asked for minting!
        _safeMint(owner, newTokenId); // Mints the NFT and registers it to the owner, mapping to the newTokenId.
        // _setTokenURI(newTokenId, TOKEN_URI) --> Try to code it making the VRFCoord choose it!
        tokenCounter = tokenCounter + 1; // Adds to the tokenCounter in order for the next mint to have a unique id as well.
    }

    // For now, we set the TokenURI
    function setTokenURI(uint256 tokenId, string memory _tokenURI) public {
        // Verifies if is approved to call via ERC721 functions.
        require(
            _isApprovedOrOwner(_msgSender(), tokenId),
            "ERC721: Caller not approved."
        );
        _setTokenURI(tokenId, _tokenURI);
    }
}
