pragma solidity ^0.5.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC721/ERC721Full.sol";

contract certificate is ERC721Full {
    constructor() public ERC721Full("Authentic Item", "AUTH") {}

  struct authCertificate {
        uint256 value; 
        string brand;
        string productDescription;
        uint256 serialNumber; 
  
  }
    mapping(uint256 => authCertificate) public _data;  

    function awardCertificate(address customer, string memory tokenURI)
        public
        returns (uint256)
    {
        uint256 newCertificateId = totalSupply();
        _mint(customer, newCertificateId);
        _setTokenURI(newCertificateId, tokenURI);

        return newCertificateId;
    }
    
    function burn(uint256 tokenId) public {
        _burn(tokenId);
    
    }
    
}