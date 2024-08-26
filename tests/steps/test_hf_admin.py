from pytest_bdd import scenario, given, when, then, parsers

feature_file_path = '../features/HF_Admin.feature'
test_data = [
    {"name": "Name1", "short_name": "ShortName1", "export_code": "ExportCode1"},
    {"name": "Name2", "short_name": "ShortName2", "export_code": "ExportCode2"},
    {"name": "Name3", "short_name": "ShortName3", "export_code": "ExportCode3"},
]

@scenario(feature_file_path, "Verify Successful Add of New Records")
def test_successful_add_of_new_record():
    pass

@scenario(feature_file_path, "Verify Successful Delete of Existing Records")
def test_successful_delete_of_existing_records():
    pass

@given(parsers.parse("User logs in as {user}"))
def user_login(login_page, home_page, user):
    login_page.login(user)

@when(parsers.parse("User navigates to {path}"))
def user_navigates_to_admin_area(admin_page, path):
    admin_page.go_to_link(path)

@when("User adds new record using test data")
def add_record(admin_page):
    for data in test_data:
        admin_page.add_new_record(data)

@then("User should see newly created record")
def verify_newly_created_record(admin_page):
    for data in test_data:
        admin_page.verify_newly_added_record(data)

@when("User deletes all records")
def delete_records(admin_page):
    for data in test_data:
        admin_page.delete_record(data)

@then("User should not see delete records")
def verify_deleted_record(admin_page):
    for data in test_data:
        admin_page.delete_record(data)