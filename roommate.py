"""
roommate.py - roommate matching library

The overall data, algorithm, and presentation are self-contained and
decoupled so each individual section can be reused, refactored, and
reincorporated into a real app later if needed.

However, the logic itself is tightly coupled to the form schema, where
one change there will necessitate edits in the weights, constructor,
and normalization function. I am not sure if there is a way around this.
"""

import csv
import math

class Student:
    """Store a student's responses."""

    # Weights for distance function
    WEIGHTS = {
        "bedtime": 12, # So a one-hour difference in bedtime translates
                       # to one distance unit
        "wake_time": 1,
        "sleep_env": 1,
        "visitors": 1,
        "neatness": 1,
        "floor_cov": 1,
        "sharing": 1,
    }

    def __init__(self, line):
        """
        Construct a Student from an array of plain strings.

        XXX: OK so this part isn't quite fully decoupled from the file
        reading. Probably shouldn't separate loading data between two
        locations, but consolidating parsing logic would either require
        a constructor with a stupid number of parameters or writing a
        Builder pattern for this class, both of which are definitely
        worse than this?
        """
        self.time, self.name, self.email, self.facebook, self.junior, \
        self.gender, self.bedtime, self.wake_time, self.sleep_env, \
        self.visitors, self.neatness, self.floor_cov, self.sharing, \
        self.bio, self.room_time, self.room_activity = line
        self.traits = self.normalize()

    def distance(self, o):
        """
        Return the relative distance between the current and another
        Student as a floating-point value.
        """
        # No mixing grade levels or purpling
        if self.junior != o.junior or self.gender != o.gender:
            return math.inf

        sum = 0
        for self_trait, o_trait in zip(self.traits, o.traits):
            diff = abs(self.traits[self_trait] - o.traits[o_trait])
            sum += Student.WEIGHTS[self_trait] * diff ** 2
        return math.sqrt(sum)

    def normalize(self):
        """
        Return a dict of integer representations of traits, all
        normalized to a [0, 1] scale. Where applicable, the scale goes
        from most to least "strict."
        """
        traits = {}

        # HACK: For bedtime, set 6 PM to 0 and 6 AM to 1. This makes
        # time distance calculations easier but will break if someone
        # enters a bedtime outside of this range.
        hour = int(self.bedtime.split(":")[0]) + 6
        minute = int(self.bedtime.split(":")[1])
        traits["bedtime"] = hour % 12 / 12 + minute / 12 / 60

        if "Early" in self.wake_time:
            traits["wake_time"] = 0
        elif "Just in time" in self.wake_time:
            traits["wake_time"] = 1/2
        else:
            traits["wake_time"] = 1

        if "absolutely quiet" in self.sleep_env:
            traits["sleep_env"] = 0
        elif "TV or music" in self.sleep_env:
            traits["sleep_env"] = 1/3
        elif "visitors" in self.sleep_env:
            traits["sleep_env"] = 2/3
        else:
            traits["sleep_env"] = 1

        if "No one" in self.visitors:
            traits["visitors"] = 0
        elif "few" in self.visitors:
            traits["visitors"] = 1/2
        else:
            traits["visitors"] = 1

        if "Always" in self.neatness:
            traits["neatness"] = 0
        elif "most" in self.neatness:
            traits["neatness"] = 1/2
        else:
            traits["neatness"] = 1

        traits["floor_cov"] = int(self.floor_cov) / 100

        if "stuff is mine" in self.sharing:
            traits["sharing"] = 0
        elif "Willing to share" in self.sharing:
            traits["sharing"] = 1/2
        else:
            traits["sharing"] = 1

        return traits

    def __str__(self):
        """Return the name of the Student."""
        return self.name

if __name__ == "__main__":
    """
    This section actually runs the algorithm and exports the data
    into a human-readable format.
    """
    # Read and store student data
    students = []
    with open("data.csv") as data:
        data.readline() # Skip header
        reader = csv.reader(data)
        for row in reader:
            students.append(Student(row))

    # Generate dict of matches from closest to furthest
    distances = {}
    for student in students:
        row = {}
        for other in students:
            row[other.name] = student.distance(other)
        distances[student.name] = \
            {k: v for k, v in sorted(row.items(), key=lambda item: item[1])}

    # Write top 10 matches into another CSV
    with open("results.csv", mode="w") as results:
        writer = csv.writer(results)
        for student in distances:
            row = []
            for other in distances[student]:
                row.append(other + '(' + str(distances[student][other]) + ')')
            writer.writerow(row)
