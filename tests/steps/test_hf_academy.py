from pytest_bdd import scenario, given, when, then, parsers

feature_file_path = '../features/HF_Academy.feature'

@scenario(feature_file_path, "Verify the display of 'How do I view or update my details' article")
def test_successful_display_of_view_my_details_articles():
    pass

@given(parsers.parse("User logs in as {user}"))
def user_login(login_page, home_page, user):
    login_page.login(user)
    home_page.dismiss_dialog_box()

@when("User launches HF Academy")
def launch_hf_academy(home_page):
    home_page.launch_hf_academy()

@when(parsers.parse("User searches for {text} in HF Academy"))
def search_hf_academy(home_page, text):
    home_page.hf_academy_search_for(text)

@then(parsers.parse("User should see {article} article"))
def verify_hf_academy_search_result(home_page, article):
    home_page.verify_hf_academy_result(article)

@when("User closes HF Academy dialog box")
def close_hf_academy_dialog(home_page):
    home_page.close_hf_academy()

@when("User logs out from the application")
def user_logs_out(home_page):
    home_page.click_logout()

@then("User should be successfully logged out")
def verify_successful_logout(login_page):
    login_page.verify_successful_logout()