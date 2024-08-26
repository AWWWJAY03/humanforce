# Created by Ray John at 8/26/24
Feature: HF Admin
  As an Admin, I want to be able to create and modify Areas in the system. When I navigate to the Area page <Test tenant>/Admin/Area, I want to be able to add multiple new Areas and see them all listed. I also want to be able to edit, delete and then undelete one of the Areas I created.

  Scenario: Verify Successful Add of New Records
    Given User logs in as Admin
    When User navigates to /Admin/Area
    And User adds new record using test data
    Then User should see newly created record


  Scenario: Verify Successful Delete of Existing Records
    Given User logs in as Admin
    When User navigates to /Admin/Area
    And User deletes all records
    Then User should not see delete records