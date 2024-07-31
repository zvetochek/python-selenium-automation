# Created by laris at 7/9/2024
Feature: Verifying target sign in page

  Scenario: Verify if Sign In form opens
    Given Open target page
    When Click Sign In header
    And From right side navigation menu click Sign In
    Then Verify Sign In form opened

    Scenario: Register a test user on target manually
      Given Open target page
      When Click Sign In header
      And From right side navigation menu click Sign In
      And Input email and password on Signin page
      And Click Sign In button
      Then Verify user is logged in

    Scenario: Register a user with incorrect email and password
      Given Open target page
      When Click Sign In header
      And From right side navigation menu click Sign In
      And Input incorrect email and password on Signin page
      And Click Sign In button
      Then Verify 'Please enter a valid email or phone number' message is shown
