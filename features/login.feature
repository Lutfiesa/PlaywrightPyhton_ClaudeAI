Feature: Login to SauceDemo
  As a user
  I want to login to the SauceDemo application
  So that I can access the product page

  Background:
    Given User opens the SauceDemo login page

  @positive @smoke
  Scenario: Login with valid credentials
    When User enters username "standard_user"
    And User enters password "secret_sauce"
    And User clicks the Login button
    Then User successfully logged into the product page
    And User sees the title "Products"

  @positive
  Scenario Outline: Login with various valid users
    When User enters username "<username>"
    And User enters password "<password>"
    And User clicks the Login button
    Then User successfully logged into the product page

    Examples:
      | username                | password     |
      | standard_user           | secret_sauce |
      | problem_user            | secret_sauce |
      | performance_glitch_user | secret_sauce |

  @negative
  Scenario: Login with empty username
    When User enters username ""
    And User enters password "secret_sauce"
    And User clicks the Login button
    Then User sees the error message "Epic sadface: Username is required"

  @negative
  Scenario: Login with empty password
    When User enters username "standard_user"
    And User enters password ""
    And User clicks the Login button
    Then User sees the error message "Epic sadface: Password is required"

  @negative
  Scenario: Login with invalid credentials
    When User enters username "invalid_user"
    And User enters password "wrong_password"
    And User clicks the Login button
    Then User sees the error message "Epic sadface: Username and password do not match any user in this service"

  @negative
  Scenario: Login with locked out user
    When User enters username "locked_out_user"
    And User enters password "secret_sauce"
    And User clicks the Login button
    Then User sees the error message "Epic sadface: Sorry, this user has been locked out."
