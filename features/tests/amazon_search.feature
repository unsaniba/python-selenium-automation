# Created by uns at 8/4/23
Feature: Test for Amazon Search

#  Scenario: verify that user can search for a table
#    Given Open Amazon page
#    When Search for a table
#    Then verify search result is "table"
#
#  Scenario: verify that user can search for a cup
#    Given Open Amazon page
#    When Search for a cup
#    Then verify search result is "cup"

  Scenario: Logged out user sees Sign in page when clicking Orders
   Given Open Amazon page
   When Click Amazon Orders link
   Then Verify Sign In page is opened


  Scenario: verify that user can search for a dress
    Given Open Amazon page
    When Search for a dress
    Then verify search result is "dress"


#  Scenario: verify that user can search for a iphone 13
#    Given Open Amazon page
#    When Search for a iphone 13
#    Then verify search result is "iphone 13"
#
#  Scenario Outline: verify that user can search for a product
#    Given Open Amazon page
#    When Search for a <search_word>
#    Then verify search result is <search_result>
#    Examples:
#      |search_word    |search_result    |
#      |cup            |"cup"            |
#      |dress          |"dress"          |
#      |iphone 13      |"iphone 13"      |

#  Scenario: verify that clicking Orders takes to signin
#    Given Open Amazon page
#    When Click Orders
#    Then verify sign in opened