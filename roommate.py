"""
roommate.py - roommate matching library

Logic itself is very "hackathon-y" but the overall data, algorithm, and
presentation are self-contained and decoupled so each individual section
can be reused, refactored, and reincorporated into a real app if needed.
"""

import math

class Student:
    """Store a student's responses."""

    # Weights for distance function
    weights = {
        "bedtime": 1,
        "wake_time": 1,
        "sleep_env": 1,
        "visitors": 1,
        "neatness": 1,
        "floor_cov": 1,
        "sharing": 1,
    }

    def __init__(self, line):
        """
        The single responsibility of this constructor is to construct a
        Student from an array of plain strings. Therefore, this is the
        only code needed to change in order to adapt to different data
        representations.

        XXX: OK so this part isn't quite fully decoupled from the file
        reading. Probably shouldn't separate loading data between two
        locations, but consolidating parsing logic would either require
        a constructor with a stupid number of parameters or writing a
        Builder pattern for this class, both of which are definitely
        worse than this?
        """
        self.name, self.email, self.facebook, self.junior, \
        self.gender, self.bedtime, self.wake_time, self.sleep_env, \
        self.visitors, self.neatness, self.floor_cov, self.sharing, \
        self.bio, self.room_time, self.room_activity = line

    def distance(self, o):
        """
        Return the relative distance between the current and another
        Student as a floating-point value. First, all trait differences
        are normalized to a [0, 1] scale, except for bedtime, which
        ranges over [0, 12] so that a one-hour difference would
        translate to one distance unit. This should make it easier to
        adjust the weights, because a default weight of 1 would have
        approximately the same meaning across all attributes as distance
        distance units are somewhat comparable between criteria.
        """
        # No mixing grade levels or purpling
        if self.junior != o.junior or self.gender != o.gender:
            return math.inf

class Matcher():
    """Compute the distance matrix."""
    def __init__(self):
        self.students = []

    def match(self):
        """
        Return a distance matrix where the value at the i-th row and
        the j-th column represents the relative distance between the two
        roommates.
        """
        pass

def Presenter():
    """Export the results into a human-readable form."""
    pass

if __name__ == "__main__":
    pass
