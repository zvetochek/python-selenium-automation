# Created by laris at 7/11/2024
Feature: Test on Target cart functionality

  Scenario: User can add product into the cart
    Given Open target page
    When Search for coffee
    And Click on coffee picture
    And Click on the button 'Add to cart'
    And Click on 'View cart & check out button'
    Then Verify if one item is added in the cart


