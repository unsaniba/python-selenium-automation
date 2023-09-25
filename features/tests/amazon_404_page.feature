# Created by uns at 9/24/23
Feature: Test for 404 Page

  Scenario: User is able to navigate to amazon blog from 404 page
    Given Open Amazon product B07NF5WGQ111 page
    And Store original window
    When Click on a dog image
    And Switch to new window
    Then Verify blog is opened
    And Close blog
    And Return to original window