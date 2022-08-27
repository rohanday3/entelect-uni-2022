from pydoc import resolve
import math
from resource import ResourceType

class Score:
    """
    Score class


    """

    def __init__(self, resources, quota, step_allowance):
        self.travel_score = 0
        self.resources = resources
        self.quota = quota
        self.travel_rewards = 0
        self.travel_penulties = 0
        self.step_allowance = step_allowance
        self.resource_score = 0
        self.party = {}

    def calculate_travel_score(self, path, party, step_allowance):
        """
        Finds travel score of party w/ step allowance
        """
        pass

    def scout_present(self, rewards, penalties):
        self.travel_rewards = rewards*2
        self.travel_penalties = penalties*2
        self.party["Scout"] = True

    def healer_present(self, step_allowance):
        self.step_allowance(math.ceil(step_allowance*1.2))
        self.party["Healer"] = True

    def gatherer_present(self, resources):
        self.resources = resources*2
        self.party["Gatherer"] = True

    # calculate resource score for current path
    def calculate_resources(self, resources, gatherer_present = False):
        if gatherer_present:
            gatherer_present(resources)

        resource_score = 0
        for i, resource in enumerate(resources):
            resource_score += resource.type.value
