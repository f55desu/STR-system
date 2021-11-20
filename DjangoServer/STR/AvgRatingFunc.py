class CritData:
    def __init__(self, crit, user_grade, avg_grade) -> None:
        self.crit = crit
        self.user_grade = user_grade
        self.avg_grade = avg_grade

    def set_crit(self, crit):
        self.crit = crit

    def set_user_grade(self, user_grade):
        self.user_grade = user_grade

    def set_avg_grade(self, avg_grade):
        self.avg_grade = avg_grade

    def __str__(self) -> str:
        return f"\n\tCRIT = {self.crit} / USER_GRADE = {self.user_grade} / AVG_GRADE = {self.avg_grade}"

    def __repr__(self) -> str:
        return self.__str__()

class AvgData:
    def __init__(self, teacher_subject, crits_data, grade_avg) -> None:
        self.teacher_subject = teacher_subject
        self.crits_data = crits_data
        self.grade_avg = grade_avg

    def __str__(self) -> str:
        return f"TEACHER_SUBJECT = {self.teacher_subject}\n  CRITS_AVG = {self.crits_data}\n  GRADE_AVG = {self.grade_avg}"   

    def __repr__(self) -> str:
        return self.__str__()

def avg(curr_teachers_subjects, all_user_grades, criterions, user):    
    avg_data_array = []

    # avg_teach = {}
    for curr in curr_teachers_subjects:
        grade_avg = 0.0
        grade_count = 0
        crits_data = []

        for crit in criterions:
            criterion_avg = 0.0
            criterion_count = 0

            new_crit_data = CritData(None, 0, 0)
            for all in all_user_grades:
                if curr == all.teacher_subject_id and all.criterion_name == crit:
                    # учет голосов только проголосовавших юзеров, если 0 -> узер не проголосовал
                    if all.student_id == user:
                        new_crit_data.set_user_grade(all.grade)

                    if all.grade != 0:
                        # criterion avg
                        criterion_avg += all.grade
                        criterion_count += 1

                        # grade avg
                        grade_avg += all.grade
                        grade_count += 1

            if criterion_count != 0:
                criterion_avg = round(criterion_avg / criterion_count, 1)

            new_crit_data.set_crit(crit)
            new_crit_data.set_avg_grade(criterion_avg)

            crits_data.append(new_crit_data)

        if grade_count != 0:
            grade_avg = round(grade_avg / grade_count, 1)

        new_avg_data = AvgData(curr, crits_data, grade_avg)
        avg_data_array.append(new_avg_data)

    return avg_data_array
    # print(f"AVG_TEACH = {avg_teach}")

# [card_avg, criterion_avg1, ... , criterion_avgN]
# [card_avg, criterion_avg1, ... , criterion_avgN]
# [card_avg, criterion_avg1, ... , criterion_avgN]


# count = 0
    # grade_avg = 0.0
    # for all in all_user_grades:
    #     for curr in current_user_grades:
    #         if all.teacher_subject_id == curr.teacher_subject_id and all.criterion_name == curr.criterion_name:
    #             grade_avg += all.grade
    #             count += 1
    # return grade_avg / count

    # rating = 0.0
    # for rate in rateList:
    #     rating += rate  
    # return round(rating/(float)(len(rateList)), 2)