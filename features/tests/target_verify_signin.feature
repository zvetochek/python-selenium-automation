# Created by laris at 7/9/2024
Feature: Verifying target sign in page

  Scenario: Verify if Sign In form opens
    Given Open target page
    When Click Sign In
    And From right side navigation menu click Sign In
    Then Verify Sign In form opened

