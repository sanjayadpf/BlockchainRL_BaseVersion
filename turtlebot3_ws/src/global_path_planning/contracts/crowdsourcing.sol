// SPDX-License-Identifier: MIT

pragma solidity ^0.5.1;

contract crowdsourcing{

    address payable public owner;
    address payable public user;
    uint public pay_amount;
    uint public collateral;
    uint public cancel_fee;
    uint256 public deadline;
    bool public available;
    bool public completed;
    uint public x;
    uint public y;

    constructor(uint _x, uint _y,uint256 _deadline) public payable{
    	x=_x;
    	y=_y;
    	deadline=_deadline;
        owner = msg.sender;
        available = true;
        completed = false;
        //value definitions only
        pay_amount = 0.03 ether;
        collateral = 0.02 ether;
        cancel_fee = 0.01 ether;
    }

    function accept_contract() public payable{
        require (available == true);
        require (address(uint160(msg.sender))!=owner); //cannot call by the owner
        require (msg.value == collateral); //should send exactly the collateral amount
        deadline = now + (3*1 days);
        user = (address(uint160(msg.sender)));
        available = false;
    }

    function cancel_contract() public payable{
        require (available == false);
        //require (msg.value > cancel_fee); //no need of value we charge from the collateral
        user = (address(0));
        available = true;
        user.transfer(collateral-cancel_fee); // return the collateral but charging the cancel_fee
    }

    function timed_out() public payable{
        require(available == false);
        require(now >= deadline);
        require (msg.value > cancel_fee); 
        user = (address(0));
        available = true;
    }

    function releaseNpay () public OnlyOwner {
        require(completed == false);
        user.transfer(collateral+pay_amount);
        completed = true;
    }

    modifier OnlyOwner(){
        require (msg.sender == owner);
        _;
    }
}
