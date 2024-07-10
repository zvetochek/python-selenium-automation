# Created by laris at 7/8/2024
Feature: Target Search Page Features

  Scenario: Check the cart
    Given Open target page
    When Click on cart icon
    Then Verify 'Your cart is empty' message is shown

