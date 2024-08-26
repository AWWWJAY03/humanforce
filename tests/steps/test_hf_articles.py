from pytest_bdd import given, when, then, parsers, scenario

feature_file_path = '../features/HF_Articles.feature'

@scenario(feature_file_path, 'Verify successful navigation to Time & Attendance page and 7 benefits of workforce analytics for business')
def successful_navigation_to_humanforce_articles():
    pass

@given("User launched Humanforce homepage")
def launch_humanforce_homepage(humanfoce_page):
    humanfoce_page.launch_humanforce()
    # humanfoce_page.accept_cookies()
    humanfoce_page.close_chat()

@when(parsers.parse('User navigates to {link}'))
def navigate_to(humanfoce_page, link):
    humanfoce_page.click_link_by_visible_text(link)

@then(parsers.parse("I should see {article} article"))
def verify_page_is_successfully_loaded(humanfoce_page, article):
    humanfoce_page.verify_article_is_loaded_successfully(article)
