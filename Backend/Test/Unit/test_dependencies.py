from sqlalchemy import text
from Backend.App.Core.dependencies import get_db


def test_db_dependency():
    db_gen = get_db()
    Session = next(db_gen)

    try:
        result = Session.execute(text("SELECT 1")).scalar()
        assert result == 1, "Database connection failed"
    finally:
        try:
            next(db_gen)
        except StopIteration:
            pass
