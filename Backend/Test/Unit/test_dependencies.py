from sqlalchemy import text
from sqlalchemy.orm import Session


def test_db_dependency(db: Session):

    result = db.execute(text("SELECT 1")).scalar()
    assert result == 1, "Database connection failed"
