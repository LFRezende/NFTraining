// SPDX-License-Identifier: MIT
pragma solidity ^0.8.1;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";

contract SimpleCollectible is ERC721 {
    // Remember the inheritance of a contract that has a constructor demands inheriting it as well.
    // Visibility for Constructor is Ignored --> No need to declare public.
    constructor() ERC721("Puppy", "PUP") {}
    // tokenCounter amounts the owners of a PUP-like ERC-721 protocol.
    uint256 tokenCounter = 0;
    // Creating and Assigning (uniquely) multiple NFTs
    // Safe Minting garanties the tokenId is unique, not repeated
    // Minting new NFTs
    function createCollectible() public returns (uint256){
        uint256 newTokenId = tokenCounter;
        _safeMint(msg.sender, newTokenId);
        tokenCounter ++;
        return newTokenId;
    }
}
