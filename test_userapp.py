import pytest


@pytest.mark.regression
def test_database_insert_record(database_connection):
    if (database_connection):
        print("Insertion Successful. ")
        assert True

@pytest.mark.sanity
def test_database_update_record(database_connection):
    if (database_connection):
        print("Update Successful. ")
        assert True

@pytest.mark.sanity
def test_database_delete_record(database_connection):
    if (database_connection):
        print("Deletion Successful. ")
        assert True

@pytest.mark.regression
@pytest.mark.sanity
def test_ui_login(ui_open):
    if (ui_open):
        print("Login Successful")
        assert True


@pytest.mark.sanity
def test_ui_view_details(ui_open):
    if (ui_open):
        print("View details Successful")
        assert True

@pytest.mark.regression
def test_ui_log_out(ui_open):
    if (ui_open):
        print("Log Out Successful")
        assert True