from pydoc import resolve
import math
from random import randint
from resource import ResourceType
import resource
from tile import Tile
from math import erf


class Score:
    """
    Score class


    """

    def __init__(self, quota, quota_m, step_allowance, map, path=[], resources=[]):
        self.travel_score = 0
        self.resources = resources
        self.quota = quota
        self.quota_m = quota_m
        self.travel_rewards = 2
        self.travel_penulties = 0.5
        self.step_allowance = step_allowance
        self.resource_score = 0
        self.path = path
        self.party = {}
        self.resource_multiplier = 1
        self.diff_map = map.diff_map
        self.tiles = map.tiles
        # self.randomParty()
        self.scout_present()
        self.gatherer_present()

    def clear_score(self):
        """
        Clears score
        """
        self.travel_score = 0
        self.resource_score = 0

    def calculate_score(self):
        """
        Finds total score of party w/ resources and travel score
        """
        self.calculate_resources()
        if self.quotaMet:
            self.resource_score *= 2
        self.calculate_travel_score()
        return self.travel_score + self.resource_score

    def calculate_next_step_score(self, position, step, resources):
        """
        Finds score of next step
        """
        travel_score = 0
        total_score = 0
        resource_score = 0

        resource_score = self.calculate_resources_step(resources, position)
        if self.quotaCheck(resources):
            resource_score *= 2
        if step <= self.step_allowance:
            travel_score = (
                (self.travel_rewards * 150) / self.diff_map[position[0]][position[1]]
            ) / (erf((step - 1) / self.step_allowance) + 1)
        else:
            travel_score = -(
                (self.travel_penulties * 150) / self.diff_map[position[0]][position[1]]
            ) * (erf((step - self.step_allowance) / self.step_allowance) + 1)
            # print(
            #     f"({(self.travel_penulties * 150)} / {self.diff_map[position[0]][position[1]]}) * (({step - self.step_allowance} / {self.step_allowance}) + 1)"
            # )
        total_score = travel_score + resource_score
        # print("Travel Score: " + str(travel_score))
        # print("Resource Score: " + str(resource_score))
        # print("Total Score: " + str(total_score))
        return total_score

    def calculate_travel_score(self):
        """
        Finds travel score of party w/ step allowance
        """
        for i in range(1, len(self.path)):
            if i <= self.step_allowance:
                self.travel_score += (
                    (self.travel_rewards * 150)
                    / self.diff_map[self.path[i][0]][self.path[i][1]]
                ) / (erf((i - 1) / self.step_allowance) + 1)
                # print(
                #     f"({(self.travel_rewards * 150) / self.diff_map[self.path[i][0]][self.path[i][1]]}) / {(erf((i - 1) / self.step_allowance) + 1)}"
                # )
            else:
                self.travel_score -= (
                    (self.travel_penulties * 150)
                    / self.diff_map[self.path[i][0]][self.path[i][1]]
                ) * (erf((i - self.step_allowance) / self.step_allowance) + 1)
                # print(
                #     f"(-{(self.travel_penalties * 150) / self.diff_map[self.path[i][0]][self.path[i][1]]}) * {(erf((i - self.step_allowance) / self.step_allowance) + 1)}"
                # )
            self.travel_score = round(self.travel_score)

    def scout_present(self):
        self.travel_rewards = 2
        self.travel_penalties = 0.5
        self.party["Scout"] = True

    def healer_present(self, step_allowance):
        self.step_allowance(math.ceil(step_allowance * 1.2))
        self.party["Healer"] = True

    def gatherer_present(self):
        self.resource_multiplier = 2
        self.party["Gatherer"] = True

    # run any 2 of the 3 functions above
    def randomParty(self):
        n = randint(1, 3)
        if n == 1:
            self.scout_present(1, 0)
            self.healer_present(self.step_allowance)
        elif n == 2:
            self.scout_present(1, 0)
            self.gatherer_present()
        elif n == 3:
            self.gatherer_present()
            self.healer_present(self.step_allowance)

    # calculate resource score for current path
    def calculate_resources(self):
        """
        Finds resource score of party w/ resources
        """
        for i in range(1, len(self.path)):
            # print([tile for tile in self.tiles])
            # print(self.tiles)
            tile = Tile.getTile(self.tiles, [self.path[i][0], self.path[i][1]])
            if tile.item != None:
                self.resource_score += tile.item.type.value * self.resource_multiplier

    def calculate_resources_step(self, resources, position):
        """
        Finds resource score of party w/ resources
        """
        if len(resources) == 0:
            return 0
        if (
            resources[len(resources) - 1].y == position[0]
            and resources[len(resources) - 1].x == position[1]
        ):
            return resources[len(resources) - 1].type.value
        return 0

    def quotaCheck(self, resources):
        """
        Checks if quota is met
        """
        resource_count = [0, 0, 0]
        for item in resources:
            if item.type == ResourceType.Coal:
                resource_count[0] += 1
            elif item.type == ResourceType.Fish:
                resource_count[1] += 1
            elif item.type == ResourceType.Scrap_metal:
                resource_count[2] += 1
            if (
                resource_count[0] >= self.quota[0]
                and resource_count[1] >= self.quota[1]
                and resource_count[2] >= self.quota[2]
            ):
                return True
        return False

    def quotaMet(self):
        """
        Checks if quota is met
        """
        resource_count = [0, 0, 0]
        for i in range(1, len(self.path)):
            tile = Tile.getTile(self.tiles, [self.path[i][0], self.path[i][1]])
            if tile.item != None:
                self.resource_score += tile.item.type.value * self.resource_multiplier
            if tile.item.type == ResourceType.Coal:
                resource_count[0] += 1
            elif tile.item.type == ResourceType.Fish:
                resource_count[1] += 1
            elif tile.item.type == ResourceType.Scrap_metal:
                resource_count[2] += 1
            if (
                resource_count[0] >= self.quota[0]
                and resource_count[1] >= self.quota[1]
                and resource_count[2] >= self.quota[2]
            ):
                return True
        return False
