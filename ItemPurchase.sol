pragma solidity ^0.5.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC721/ERC721Full.sol";

contract ShopRegistry is ERC721Full {
    constructor() public ERC721Full("ShopRegistryToken", "FASHION") {}

    struct Item {
        string name;
        string manufacturer;
        uint256 itemValue;
        string fashionJson;
}

    mapping(uint256 => Item) public fashionCollection;

    event Buy(uint256 tokenId, uint256 itemValue, string reportURI, string fashionJson);
    
    function imageUri(
        uint256 tokenId

    ) public view returns (string memory imageJson){
        return fashionCollection[tokenId].fashionJson;
    }


    function purchaseItem(
        address owner,
        string memory name,
        string memory manufacturer,
        uint256 itemCost,
        string memory tokenURI,
        string memory tokenJSON
    ) public returns (uint256) {
        uint256 tokenId = totalSupply();

        _mint(owner, tokenId);
        _setTokenURI(tokenId, tokenURI);

        fashionCollection[tokenId] = Item(name, manufacturer, itemCost, tokenJSON);

        return tokenId;
    } 
}
