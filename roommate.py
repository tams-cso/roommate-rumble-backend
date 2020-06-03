import math


class Student:

    # Note: weights are all 1, besides these
    WEIGHTS = {
        "bedtime": 12,
        "waketime": 12,
        "to_sleep": 5,
        "cannot_sleep": 5,
        "percent_floor": 0.01,
    }

    # create and normalize person object
    # updated to support new TSV
    # note: I personally think a stupid number of parameters is okay
    # since we are only going to be using the constructor in once place
    def __init__(
        self,
        first_name,
        last_name,
        gender,
        goes_to_bed,
        gets_up,
        to_go_to_sleep,
        cannot_go_to_sleep,
        gaming,
        social_net,
        phone,
        sleeping,
        studying,
        tv,
        exercising,
        personal_space,
        percent_floor,
        sharing,
        brings,
    ):
        self.traits = {}
        self.name = first_name + " " + last_name
        self.gender = gender
        self.traits["bedtime"] = [
            "Doesn't matter",
            "Before 11pm",
            "Before midnight",
            "After midnight",
            "Before 2:00 AM",
            "After 2:00 AM",
        ].index(goes_to_bed) + 1
        self.traits["waketime"] = [
            "Doesn't matter",
            "Early, with time to spare",
            "Just in time to get to class",
        ].index(gets_up) + 1
        self.traits["to_sleep"] = [
            "Doesn't matter",
            "The room has to be dark",
            "At least one light must be on",
            "Blinds open to let the morning sun in",
        ].index(to_go_to_sleep) + 1
        self.traits["cannot_sleep"] = [
            "I can sleep through anything",
            "With a TV or music on",
            "If my roommate has visitors in the room",
            "Unless it is absolutely quiet",
        ].index(cannot_go_to_sleep) + 1
        self.traits["gaming"] = int(gaming)
        self.traits["social_net"] = int(social_net)
        self.traits["phone"] = int(phone)
        self.traits["sleeping"] = int(sleeping)
        self.traits["studying"] = int(studying)
        self.traits["tv"] = int(tv)
        self.traits["exercising"] = int(exercising)
        self.traits["personal_space"] = [
            "Always neat and organized",
            "Neat most of the time",
            "Cluttered most of the time",
            "Always messy and disorganized",
        ].index(personal_space) + 1
        self.traits["percent_floor"] = int(percent_floor)
        self.traits["sharing"] = [
            "What's mine is yours and vice versa",
            "Willing to share most stuff if I'm asked first",
            "Willing to share certain items only",
            "Not comfortable sharing my stuff",
        ].index(sharing) + 1
        self.traits["brings"] = [
            "Anyone into my room. My room is a social area.",
            "Only a few people into my room.",
        ].index(brings) + 1

    def dist(self, other):
        """ Returns Euclidian distance between self and other """

        # different genders cant mix, grade level is assumed to be the same (juniors)
        if self.gender != other.gender:
            return math.inf

        sum = 0
        for key in self.traits.keys():
            weight = self.WEIGHTS.get(key, 1)  # defaults to a weight of 1
            diff_sq = abs(self.traits[key] - other.traits[key]) ** 2
            sum += weight * diff_sq

        return math.sqrt(sum)

    def getDistanceList(self, others):
        """ Takes in an array of Students and returns sorted list of best matches (best --> worst) """
        dists = []
        for s in others:
            if self.gender == s.gender:
                dists.append((s.name, self.dist(s)))

        sorted_list = sorted(dists, key=lambda x: x[1])
        return [x[0] for x in sorted_list]

    def __str__(self):
        """ Returns name to print out """
        return self.name
