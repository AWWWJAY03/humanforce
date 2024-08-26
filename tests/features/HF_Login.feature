# Created by Ray John at 8/26/24
Feature: Humanforce Login
  As an Employee with valid credentials, I want to visit <test tenant> and login successfully and access the home page where I can see a greeting with my name.

  Scenario Outline: Successful login to Humanforce
    When User logs in as <Tenant>
    Then User should see a greeting with <Name>
    Examples:
      | Tenant    | Name   |
      | Admin     | Bruce  |
      | Manager   | Jean   |
      | Employee  | Wade   |

  Scenario Outline: Unsuccessful login to Humanforce
    When User logs in as <Tenant>
    Then User should see a correct <Error Message>
    Examples:
      | Tenant   | Error Message                                        |
      | Invalid  | The Employee code/email and/or password is invalid.  |
      | Empty    | The Employee code or email field is required.        |
