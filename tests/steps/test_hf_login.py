from pytest_bdd import then, parsers, scenario, when

feature_file_path = '../features/HF_Login.feature'

@scenario(feature_file_path, 'Successful login to Humanforce')
def test_successful_login():
    pass

@scenario(feature_file_path, 'Unsuccessful login to Humanforce')
def test_unsuccessful_login():
    pass

@when(parsers.parse("User logs in as {user}"))
def user_login(login_page, user):
    login_page.login(user)
    
@then(parsers.parse("User should see a greeting with {name}"))
def verify_name_in_greetings(home_page, name):
    home_page.verify_name_in_greetings(name)

@then(parsers.parse("User should see a correct {message}"))
def verify_login_error_message(login_page, message):
    login_page.verify_login_error_is_displayed(message)