# Created by Jose del Rio 2020/08/28
# Copyright 2020 Jose del Rio. All rights reserved.


# Problem statement:
# -----------------
#   Implement a group_by_owners function that:
#   - Accepts a dictionary containing the file owner name for each file name
#   - Returns a dictionary containing a list of file names for each owner name, in any order.
#
#   For example, for dictionary {'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'}
#   the group_by_owners function should return {'Randy': ['Input.txt', 'Output.txt'], 'Stan': ['Code.py']}


def group_by_owners(files):
    group = {}
    for file, owner in files.items():
        group[owner] = group.get(owner, []) + [file]
    return group


def test_group_by_owners():
    data_input = {
        'Input.txt': 'Randy',
        'Code.py': 'Stan',
        'Output.txt': 'Randy'
    }
    expected_output = {'Randy': ['Input.txt', 'Output.txt'],
                       'Stan': ['Code.py']}

    result = group_by_owners(data_input)

    assert result.keys() == expected_output.keys()
    for res, exp in zip(result, expected_output):
        assert set(res) == set(exp)
    print(result)


if __name__ == "__main__":
    test_group_by_owners()
