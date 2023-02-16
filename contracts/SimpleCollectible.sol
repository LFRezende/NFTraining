// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";

contract SimpleCollectible is ERC721 {
    // Remember the inheritance of a contract that has a constructor demands inheriting it as well.
    // Visibility for Constructor is Ignored --> No need to declare public (high versions from 0.7)
    constructor() public ERC721("PUG", "PUP") {}

    // tokenCounter amounts the owners of a PUP-like ERC-721 protocol.
    uint256 public tokenCounter = 0;

    // Creating and Assigning (uniquely) multiple NFTs
    // Safe Minting garanties the tokenId is unique, not repeated
    // Minting new NFTs
    function createCollectible(string memory tokenURI)
        public
        returns (uint256)
    {
        uint256 newTokenId = tokenCounter;
        _safeMint(msg.sender, newTokenId);
        _setTokenURI(newTokenId, tokenURI);
        tokenCounter++;
        return newTokenId;
    }
}
