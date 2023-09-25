# Created by uns at 9/24/23
Feature: test fo bestseller Func

  Scenario: Click on Best Sellers link and verify top links
    Given Open Amazon page
    When Click BESTSELLER
    Then Verify footer has 5 links
    When Click on each top link and verify the correct page opens