class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        while students:

            # current_student = students.pop(0)
            current_student = students.pop()
            # print(current_student)

            # if current_student == sandwiches[-1]:
            if current_student == sandwiches[0]:
                # sandwiches.pop()
                sandwiches.pop(0)
            else:
                # students.append(current_student)
                students.insert(0, current_student)

            if len(sandwiches) == 0:
                break;

            # if sandwiches[-1] not in students:
            if sandwiches[0] not in students:
                break;

        return len(students)
