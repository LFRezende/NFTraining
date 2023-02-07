// SPDX-License-Identifier: MIT
pragma solidity ^0.8.1;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";

contract SimpleCollectible is ERC721 {
    // Remember the inheritance of a contract that has a constructor demands inheriting it as well.
    constructor() public ERC721("Puppy", "PUP") {}
}
