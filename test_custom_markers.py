import pytest

@pytest.mark.regression
def test_database_insert_record(database_connection):
    if (database_connection):
        print("Insertion Successful. ")
        assert True

@pytest.mark.sanity
def test_ui_view_details(ui_open):
    if (ui_open):
        print("View details Successful")
        assert True

