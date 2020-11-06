import copy
import random
from typing import List


class Hat:
    contents = []

    def __init__(self, **kwargs):
        res = []
        for element in kwargs:
            res.append([element] * kwargs[element])

        self.contents = [item for sublist in res for item in sublist]

    def draw(self, number_to_draw) -> List[str]:
        if number_to_draw > len(self.contents):
            return self.contents

        content = copy.copy(self.contents)
        random.shuffle(content)
        result = content[:number_to_draw]
        self.contents = content[number_to_draw:]
        return result


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success_results = 0
    for i in range(num_experiments):
        new_hat = copy.copy(hat)
        result = new_hat.draw(num_balls_drawn)
        success = True
        for expected_ball in expected_balls:
            success = success and (result.count(expected_ball) >= expected_balls[expected_ball])
        if success:
            success_results += 1
    return success_results / num_experiments
