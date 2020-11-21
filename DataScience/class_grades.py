# Class Grades
#
# Implement the function class_grades, which accepts all students in a school and returns all classes
# in the school, together with their median grades.
#
# Students are stored in a two-dimensional list where each element of the list is another list with the
# following elements: Student name, class name, student grade.
#
# The function should return a two-dimensional list where each element is a list with the following elements:
# Class name, median grade for students in the class. The order of returned classes is not important
#
# For example, the following students list:
#    students = [["Ana Stevens", "1a", 5], ["Mark Stevens", "1a", 4],
#                ["Jon Jones", "1a", 2], ["Bob Kent", "1b", 4]]
#
# Should return:   [['1a', 4.0], ['1b', 4.0]]


import pandas as pd


def class_grades(students):
    """
    :param students: (list) Each element of the list is another list with the
      following elements: Student name (string), class name (string), student grade (int).
    :returns: (list) Each element is a list with the following
      elements: Class name (string), median grade for students in the class (float).
    """
    df = pd.DataFrame(students, columns=('name', 'class', 'grade'))
    class_median = df.groupby(['class']).median()['grade'].to_dict()

    return [[key, val] for key, val in class_median.items()]


def test_class_grades():
    students = [["Ana Stevens", "1a", 5], ["Mark Stevens", "1a", 4], ["Jon Jones", "1a", 2], ["Bob Kent", "1b", 4]]
    expected_output = [['1a', 4], ['1b', 4]]

    result = class_grades(students)

    assert isinstance(result, list)
    assert result == expected_output


if __name__ == "__main__":
    test_class_grades()
