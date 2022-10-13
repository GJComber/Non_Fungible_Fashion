//Solidity page

//establish pragma
pragma solidity ^0.5.0;

//imports for solidity
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC721/ERC721Full.sol";

//##############################################
//CONTRACT SET UP
//##############################################

contract Fashion is ERC721Full {
    constructor() public ERC721Full("Fashion", "FASH") {}

    function registerArtwork(address owner, string memory tokenURI)
        public
        returns (uint256)
    {
        uint256 tokenId = totalSupply();
        _mint(owner, tokenId);
        _setTokenURI(tokenId, tokenURI);

        return tokenId;
    }
}
