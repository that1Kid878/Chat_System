from Backend.App.Core import security
from uuid import uuid4
from datetime import timedelta
import pytest
from Backend.App.Core import exceptions


class TestAccessToken:
    def test_access_token_content(self):
        id = str(uuid4())
        name = "that1Kid"
        expireDelta = timedelta(hours=2)
        Token = security.Create_New_Acces_Token(name, id, expireDelta)
        payload = security.Decode_Access_Token(Token)
        assert payload.get("id") == id
        assert payload.get("sub") == name

    def test_expired_access_token(self):
        id = str(uuid4())
        name = "that1Kid"
        Expired_Token = security.Create_New_Acces_Token(name, id, timedelta(hours=-2))
        with pytest.raises(exceptions.Expired_Access_Token):
            security.Decode_Access_Token(Expired_Token)

    def test_invalid_access_token(self):
        Invalid_Token = "oiwjhdnfkoiiosdjdksoiajhsdnfkkkdj"
        with pytest.raises(exceptions.Invalid_Access_Token):
            security.Decode_Access_Token(Invalid_Token)
