import csv

from roommate import Student

IN_FILENAME = "2024_males.csv"
OUT_FILENAME = "2024_males.csv"

students = []

with open(IN_FILENAME, encoding='latin-1') as csv_file:
    reader = csv.reader(csv_file, delimiter=",")
    next(reader)
    # skip first three lines

    for row in reader:
        students.append(
            Student(
                first_name=row[1],
                last_name=row[2],
                gender=row[4],
                goes_to_bed=row[5],
                gets_up=row[6],
                to_go_to_sleep=row[7],
                cannot_go_to_sleep=row[8],
                gaming=row[13],
                social_net=row[14],
                phone=row[15],
                sleeping=row[16],
                studying=row[17],
                tv=row[18],
                exercising=row[19],
                personal_space=row[20],
                percent_floor=row[21],
                sharing=row[22],
                brings=row[23],
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
    students.sort(key=(lambda s: s.name.split()[1])) #sort by last name
    for s in students:
        writer.writerow(
            [s.name] + s.getDistanceList([x for x in students if x is not s])
        )
