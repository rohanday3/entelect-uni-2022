from pydoc import resolve
import math
from random import randint
from resource import ResourceType

class Score:
    """
    Score class


    """

    def __init__(self, resources, quota,quota_m, step_allowance, path):
        self.travel_score = 0
        self.resources = resources
        self.quota = quota
        self.quota_m = quota_m
        self.travel_rewards = 0
        self.travel_penulties = 0
        self.step_allowance = step_allowance
        self.resource_score = 0
        self.path = path
        self.party = {}
        self.resource_multiplier = 1
        # self.randomParty()
        self.scout_present(self, 1, 0)
        self.gatherer_present(self)

    def calculate_score(self):
        """
        Finds total score of party w/ resources and travel score
        """
        if self.quotaMet:
            self.resource_multiplier*=2
        self.calculate_travel_score(self.party, self.step_allowance)
        self.calculate_resources()
        return self.travel_score + self.resource_score

    def calculate_travel_score(self):
        """
        Finds travel score of party w/ step allowance
        """
        for i in range(len(self.path)):
            if i<=self.step_allowance-1:
                self.travel_score += (self.travel_rewards*150/self.path[i].difficulty)/((i/self.step_allowance)+1)
            else:
                self.travel_score -= (self.travel_penulties*150/self.path[i].difficulty)*((i-self.step_allowance/self.step_allowance)+1)

    def scout_present(self, rewards, penalties):
        self.travel_rewards = rewards*2
        self.travel_penalties = penalties*0.5
        self.party["Scout"] = True

    def healer_present(self, step_allowance):
        self.step_allowance(math.ceil(step_allowance*1.2))
        self.party["Healer"] = True

    def gatherer_present(self):
        self.resource_multiplier *= 2
        self.party["Gatherer"] = True

    # run any 2 of the 3 functions above
    def randomParty(self):
        n = randint(1,3)
        if n == 1:
            self.scout_present(1,0)
            self.healer_present(self.step_allowance)
        elif n == 2:
            self.scout_present(1,0)
            self.gatherer_present()
        elif n == 3:
            self.gatherer_present()
            self.healer_present(self.step_allowance)
        

    # calculate resource score for current path
    def calculate_resources(self):
        """
        Finds resource score of party w/ resources
        TODO: REVIEW USE WITH NODE CLASS
        """
        for tile in self.path:
            if tile.resource != None:
                self.resource_score += tile.item.type.value*self.resource_multiplier

    def quotaMet(self):
        """
        Checks if quota is met
        """
        resource_count = [0,0,0]
        for resource in self.resources:
            if resource.type == ResourceType.COAL:
                resource_count[0] +=1
            elif resource.type == ResourceType.FISH:
                resource_count[1] +=1
            elif resource.type == ResourceType.SCRAP_METAL:
                resource_count[2] +=1
        if resource_count[0] >= self.quota[0] and resource_count[1] >= self.quota[1] and resource_count[2] >= self.quota[2]:
            return True
