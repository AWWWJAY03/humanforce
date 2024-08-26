# Created by Ray John at 8/26/24
Feature: HF Academy
  As a Manager, I want to utilise the HF Academy to access help articles to allow me to use the product better. When I login to <test tenant> I want to be able to access the this functionality by clicking on the 'HF Academy' button located at the bottom left of the page. Once the pop-up window appears, I want to search for 'Personal' and find the article titled 'How do I view or update my details' after scrolling down. After reading the article, I want to navigate back to the Home Page and finally log out of the system.

  Scenario: Verify the display of 'How do I view or update my details' article
    Given User logs in as Manager
    When User launches HF Academy
    And User searches for Personal in HF Academy
    Then User should see How do I view or update my details? article
    When User closes HF Academy dialog box
    And User logs out from the application
    Then User should be successfully logged out





