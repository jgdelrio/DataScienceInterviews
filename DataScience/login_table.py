# Login Table
# (Python > Data Science > Pandas)
#
# A company stores login data and password hashes in two different containers:
#   - DataFrame with columns: Id, Login, Verified.
#   - Two-dimensional NumPy array where each element is an array that contains: Id and Password.
#
# Elements on the same row/index have the same Id.
#
# Implement the function login_table that accepts these two containers and
# modifies id_name_verified DataFrame in-place, so that:
#   - The Verified column should be removed.
#   - The password from NumPy array should be added as the last column with the name "Password" to DataFrame.
#
# For example, the following code snippet:
#
#   id_name_verified = pd.DataFrame([[1, "JohnDoe", True], [2, "AnnFranklin", False]], columns=["Id", "Login", "Verified"])
#   id_password = np.array([[1, 987340123], [2, 187031122]], np.int32)
#   login_table(id_name_verified, id_password)
#   print(id_name_verified)
#
# Should print:
#      Id        Login   Password
#   0   1      JohnDoe  987340123
#   1   2  AnnFranklin  187031122


import pandas as pd
import numpy as np


def login_table(id_name_verified, id_password):
    """
    :param id_name_verified: (DataFrame) DataFrame with columns: Id, Login, Verified.
    :param id_password: (numpy.array) Two-dimensional NumPy array where each element
                        is an array that contains: Id and Password
    :returns: (None) The function should modify id_name_verified DataFrame in-place.
              It should not return anything.
    """
    # Drop Verified column
    id_name_verified.drop(['Verified'], axis=1, inplace=True)

    # Convert the id_password to dictionary and map to dataframe
    id_name_verified['Password'] = id_name_verified['Id'].map(dict(id_password))


def test_login_table():
    id_name_verified = pd.DataFrame([[1, "JohnDoe", True], [2, "AnnFranklin", False]],
                                    columns=["Id", "Login", "Verified"])
    id_password = np.array([[1, 987340123], [2, 187031122]], np.int32)
    expected_output = pd.DataFrame([[1, "JohnDoe", 987340123], [2, "AnnFranklin", 187031122]],
                                   columns=["Id", "Login", "Password"])

    login_table(id_name_verified, id_password)
    print(id_name_verified)

    assert id_name_verified.equals(expected_output)


if __name__ == "__main__":
    test_login_table()
