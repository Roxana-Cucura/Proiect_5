Feature: Jules forgot password tests

  # se ruleaza inainte de fiecare test
  Background:
    Given sign_in: I am a user on Jules sign in page

  @jules
  Scenario: Wrong email validation message
    When sign_in: I click forgot password link
    When forgot_password: I set my email "abcd"
    Then forgot_password: I verify that email validation is correct


  @jules2
  Scenario Outline: Wrong email validation with examples
    When sign_in: I click forgot password link
    When forgot_password: I set my email "<email>"
    Then forgot_password: I verify that email validation is correct

    Examples:
      | email              |
      | abcd@yahoo.com     |
      | roxana21@yahoo.com |
      | exemplu@yahoo.com  |


