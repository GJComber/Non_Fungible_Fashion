pragma solidity ^0.5.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC721/ERC721Full.sol";

contract nonFungibleFashion is ERC721Full {
    constructor() public ERC721Full("FashionToken", "FASH") {}

    struct Fashion {
        string brandName;
        string productDescription;
        uint256 itemValue;
        string fashionJson;
    }

    mapping(uint256 => Fashion) public fashionCollection;

    event Authenticate(uint256 tokenId, uint256 itemValue, string reportURI, string fashionJson);
    
    function imageUri(
        uint256 tokenId

    ) public view returns (string memory imageJson){
        return fashionCollection[tokenId].fashionJson;
    }


    function registerFashion(
        address owner,
        string memory brandName,
        string memory productDescription,
        uint256 initialAuthenticatedValue,
        string memory tokenURI,
        string memory tokenJSON
    ) public returns (uint256) {
        uint256 tokenId = totalSupply();

        _mint(owner, tokenId);
        _setTokenURI(tokenId, tokenURI);

        fashionCollection[tokenId] = Fashion(brandName, productDescription, initialAuthenticatedValue, tokenJSON);

        return tokenId;
    }

    function newAuthentication(
        uint256 tokenId,
        uint256 newAuthenticatedValue,
        string memory reportURI,
        string memory tokenJSON
        
    ) public returns (uint256) {
        fashionCollection[tokenId].itemValue = newAuthenticatedValue;

        emit Authenticate(tokenId, newAuthenticatedValue, reportURI, tokenJSON);

        return (fashionCollection[tokenId].itemValue);
    }
}


