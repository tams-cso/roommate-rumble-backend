"""
roommate.py - roommate matching library

The overall data, algorithm, and presentation are self-contained and
decoupled so each individual section can be reused, refactored, and
reincorporated into a real app later if needed.

However, the logic itself is tightly coupled to the form schema, where
one change there will necessitate edits in the weights, constructor,
and normalization function. I am not sure if there is a way around this.
"""

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
        self.name, self.email, self.facebook, self.junior, \
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

        if self.wake_time == "Early, with time to spare":
            traits["wake_time"] = 0
        elif self.wake_time == "Just in time to get to class":
            traits["wake_time"] = 1/2
        else:
            traits["wake_time"] = 1

        if self.sleep_env == "Unless it is absolutely quiet":
            traits["sleep_env"] = 0
        elif self.sleep_env == "With a TV or music on":
            traits["sleep_env"] = 1/3
        elif self.sleep_env == "If my roommate has visitors in the room":
            traits["sleep_env"] = 2/3
        else:
            traits["sleep_env"] = 1

        if self.visitors == "No one in my room. My room is only for myself and my roommate":
            traits["visitors"] = 0
        elif self.visitors == "Only a few people into my room.":
            traits["visitors"] = 1/2
        else:
            traits["visitors"] = 1

        if self.neatness == "Always neat and organized":
            traits["neatness"] = 0
        elif self.neatness == "Neat most of the time":
            traits["neatness"] = 1/2
        else:
            traits["neatness"] = 1

        traits["floor_cov"] = int(self.floor_cov) / 100

        if self.sharing == "All my stuff is mine":
            traits["sharing"] = 0
        elif self.sharing == "Willing to share most stuff if I'm asked first":
            traits["sharing"] = 1/2
        else:
            traits["sharing"] = 1

        return traits

if __name__ == "__main__":
    pass
