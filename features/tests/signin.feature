# Created by uns at 9/24/23
Feature: SignIn Tests

    Scenario: Sign In page can be opened from SignIn popup
    Given Open Amazon page
    When Click on button from SignIn popup
    Then Verify sign in page opened


  Scenario: Amazon users see sign in button
    Given Open Amazon page
    Then Verify Sign In is Clickable
    When Wait for 3 sec
    Then Verify Sign In is Clickable
    Then Verify Sign In disappears
    Given Open Amazon page


  Scenario: Adding a product to the cart
    Given Open Amazon Product page
    When Click on cart icon
    Then Verify 'Your Shopping Cart is empty.' text present


  Scenario: open product page and add to cart
    Given Open Amazon Product page
    When Click on cart icon
    Then Verify the item is added to Cart



  Scenario: Click on Best Sellers link and verify top links
    Given Open Amazon page
    When Click BESTSELLER
    Then Verify footer has 5 links
    When Click on each top link and verify the correct page opens


