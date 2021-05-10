import csv

from roommate import Student

IN_FILENAME = "room_habits_questionnaire.csv"
OUT_FILENAME = "output.csv"

students = []

with open(IN_FILENAME) as csvf:
    reader = csv.reader(csvf, delimiter=",")
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
        print(
            "{}: {}".format(s, s.getDistanceList([x for x in students if x is not s]))
        )

with open(OUT_FILENAME, "w+", newline="") as csvo:
    writer = csv.writer(csvo)
    writer.writerow(
        ["Name", "Names of recommended people from most to least recommended"]
    )
    for s in students:
        writer.writerow(
            [s.name] + s.getDistanceList([x for x in students if x is not s])
        )
