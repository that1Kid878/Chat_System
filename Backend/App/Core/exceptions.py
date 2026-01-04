from enum import Enum


class DB_Exceptions(Enum):
    Unique_Violation = 23505
    Foreign_Key_Violation = 23503
    Not_Null_Violation = 23502


class Missing_Parameters(Exception):
    """Function or operations missing important parameters"""


class Invalid_Parameters(Exception):
    """Function or operation using invalid parameters"""


class Existing_Data(Exception):
    """Data added into database already exists and violates the UNIQUE constraint"""


class Not_In_Referenced_Table(Exception):
    """Data in column is not in referenced table"""


class Null_Value(Exception):
    """Expected value is null"""


class Nonexistent_User(Exception):
    """User does not exist in database"""


def Integrity_Error_Handler(code: int):
    if code == DB_Exceptions.Unique_Violation:
        return Existing_Data()

    elif code == DB_Exceptions.Foreign_Key_Violation:
        return Not_In_Referenced_Table()

    elif code == DB_Exceptions.Not_Null_Violation:
        return Null_Value()

    return Exception
