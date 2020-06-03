import random

import names

from roommate import Student

# testing code
students = []
students.append(
    Student(
        first_name="Todd",
        last_name="Todd",
        gender="Male",
        goes_to_bed="Doesn't matter",
        gets_up="Early, with time to spare",
        to_go_to_sleep="Blinds open to let the morning sun in",
        cannot_go_to_sleep="Unless it is absolutely quiet",
        gaming=4,
        social_net=4,
        phone=4,
        sleeping=4,
        studying=4,
        tv=4,
        exercising=4,
        personal_space="Cluttered most of the time",
        percent_floor=4,
        sharing="Willing to share most stuff if I'm asked first",
        brings="Only a few people into my room.",
    )
)
students.append(
    Student(
        first_name="Todd",
        last_name="Todd",
        gender="Male",
        goes_to_bed="Doesn't matter",
        gets_up="Early, with time to spare",
        to_go_to_sleep="Blinds open to let the morning sun in",
        cannot_go_to_sleep="Unless it is absolutely quiet",
        gaming=4,
        social_net=4,
        phone=4,
        sleeping=4,
        studying=4,
        tv=4,
        exercising=4,
        personal_space="Cluttered most of the time",
        percent_floor=4,
        sharing="Willing to share most stuff if I'm asked first",
        brings="Only a few people into my room.",
    )
)

for i in range(10):
    students.append(
        Student(
            first_name=names.get_first_name(),
            last_name=names.get_last_name(),
            gender=random.choice(["Male", "Female"]),
            goes_to_bed=random.choice(
                [
                    "Doesn't matter",
                    "Before 11pm",
                    "Before midnight",
                    "After midnight",
                    "Before 2:00 AM",
                    "After 2:00 AM",
                ]
            ),
            gets_up=random.choice(
                [
                    "Doesn't matter",
                    "Early, with time to spare",
                    "Just in time to get to class",
                ]
            ),
            to_go_to_sleep=random.choice(
                [
                    "Doesn't matter",
                    "The room has to be dark",
                    "At least one light must be on",
                    "Blinds open to let the morning sun in",
                ]
            ),
            cannot_go_to_sleep=random.choice(
                [
                    "I can sleep through anything",
                    "With a TV or music on",
                    "If my roommate has visitors in the room",
                    "Unless it is absolutely quiet",
                ]
            ),
            gaming=random.randrange(10),
            social_net=random.randrange(10),
            phone=random.randrange(10),
            sleeping=random.randrange(10),
            studying=random.randrange(10),
            tv=random.randrange(10),
            exercising=random.randrange(10),
            personal_space=random.choice(
                [
                    "Always neat and organized",
                    "Neat most of the time",
                    "Cluttered most of the time",
                    "Always messy and disorganized",
                ]
            ),
            percent_floor=random.randrange(10),
            sharing=random.choice(
                [
                    "What's mine is yours and vice versa",
                    "Willing to share most stuff if I'm asked first",
                    "Willing to share certain items only",
                    "Not comfortable sharing my stuff",
                ]
            ),
            brings=random.choice(
                [
                    "Anyone into my room. My room is a social area.",
                    "Only a few people into my room.",
                ]
            ),
        )
    )

for s in students:
    print("{}: {}".format(s, s.getDistanceList([x for x in students if x is not s])))
