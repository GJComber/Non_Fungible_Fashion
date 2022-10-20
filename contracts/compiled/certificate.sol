pragma solidity ^0.5.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC721/ERC721Full.sol";

contract certificate is ERC721Full {
    constructor() public ERC721Full("Authentic Item", "AUTH") {}

    function awardCertificate(address buyer, string memory tokenURI)
        public
        returns (uint256)
    {
        uint256 approval = totalSupply();
        _mint(buyer, newCertificateId);
        _setTokenURI(newCertificateId, description);

        return newCertificateId;
    }
}