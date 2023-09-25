# Created by uns at 9/24/23
Feature: Test for PRIVACY Page

  Scenario: User can open and close Amazon Privacy Notice
    Given Open Amazon T&C page
    And Store original window
    When Click on a dog image
    And Switch to new window
    Then Verify blog is opened
    And Close blog
    And Return to original window