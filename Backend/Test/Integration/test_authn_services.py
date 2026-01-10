from Backend.App.Services.authn_services import Login
from Backend.App.Core.exceptions import Invalid_Credentials, Nonexistent_User
import pytest


class TestLogin:
    def test_basic_login(db, mock_user):
        Username = "that1Kid"
        Password = "Akidanaqi10"
        result = Login(Username, Password, db)
        assert result.get("access_token")
        assert result.get("refresh_token")

    def test_invalid_credentials(db, mock_user):
        Username = "that1Kid"
        Password = "abcdefghijk"
        with pytest.raises(Invalid_Credentials):
            Login(Username, Password, db)

    def test_invalid_username(db, mock_user):
        Username = "Mr_Krabs"
        Password = "Akidanaqi10"
        with pytest.raises(Nonexistent_User):
            Login(Username, Password, db)
