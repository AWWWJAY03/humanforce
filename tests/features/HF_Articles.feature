# Created by Ray John at 8/26/24
Feature: Humanforce Website
  As viewer, I want to visit the Humanforce website https://www.humanforce.com/ and easily navigate to the 'Time & Attendance' page where I can access helpful resources at the bottom of the page. Specifically, I want to select the '7 benefits of workforce analytics for business' article and read about this topic.

  Scenario: Verify successful navigation to Time & Attendance page and 7 benefits of workforce analytics for business
    Given User launched Humanforce homepage
    When User navigates to Time & Attendance
    And User navigates to 7 benefits of workforce analytics for business
    Then I should see 7 benefits of workforce analytics for business article