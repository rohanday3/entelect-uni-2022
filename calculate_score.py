from pydoc import resolve
import math
from resource import ResourceType

class Score:
    """
    Score class


    """

    def __init__(self, resources, quota, step_allowance, path):
        self.travel_score = 0
        self.resources = resources
        self.quota = quota
        self.travel_rewards = 0
        self.travel_penulties = 0
        self.step_allowance = step_allowance
        self.resource_score = 0
        self.path = path
        self.party = {}
        self.resource_multiplier = 1

    def calculate_travel_score(self, party, step_allowance):
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
        self.resource_multiplier = 2
        self.party["Gatherer"] = True

    # calculate resource score for current path
    def calculate_resources(self, resources, gatherer_present = False):
        """
        Finds resource score of party w/ resources
        TODO: REVIEW USE WITH NODE CLASS
        """

        if gatherer_present:
            gatherer_present()

        for tile in self.path:
            if tile.resource != None:
                if tile.resource.type == resources:
                    self.resource_score += tile.item.type.value*self.resource_multiplier
