from sqlalchemy import text
from Backend.App.Core.database import SessionLocal


def test_db_dependency():
    Session = SessionLocal()

    result = Session.execute(text("SELECT 1")).scalar()
    assert result == 1, "Database connection failed"

    Session.close()
