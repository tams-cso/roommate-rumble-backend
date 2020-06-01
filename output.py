import csv

from roommate import Student

FILENAME = "room_habits_questionnaire.tsv"

students = []

with open(FILENAME) as csvf:
    reader = csv.reader(csvf, delimiter="\t")
    next(reader)
    next(reader)
    next(reader)  # skip first three lines

    for row in reader:
        students.append(
            Student(
                first_name=row[9],
                last_name=row[10],
                gender=row[12],
                goes_to_bed=row[13],
                gets_up=row[14],
                to_go_to_sleep=row[15],
                cannot_go_to_sleep=row[16],
                gaming=row[21],
                social_net=row[22],
                phone=row[23],
                sleeping=row[24],
                studying=row[25],
                tv=row[26],
                exercising=row[27],
                personal_space=row[28],
                percent_floor=row[29],
                sharing=row[30],
                brings=row[31],
            )
        )

    for s in students:
        print("{}: {}".format(s, s.getDistanceList([x for x in students if x is not s])))
