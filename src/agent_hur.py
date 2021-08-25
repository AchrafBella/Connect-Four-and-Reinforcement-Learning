from agents import Agent
import numpy as np
from operator import itemgetter
import itertools as it


class HeuristicAgent(Agent):
    """
    This agent use an heuristic that makes him choose wisely the place of piece by looking all the possible places
    he chooses the place with the high score
    """
    def __init__(self, agent_name, disk):
        super().__init__(agent_name, disk)

    def patterns(self, observation, pairs, dimension):
        """ deterministic way
        this function will get the patterns for the move for each move will assign a specific weight
        to weight my moves i choose a scale from 1 to 10
        :param observation:
        :param pairs:
        :param dimension:
        :return:
        """
        weights = []
        last_row, last_col = dimension[0] - 1, dimension[1] - 1
        first_col = 0
        for pair in pairs:
            if pair[0] == last_row and pair[1] == last_col:
                # check the left
                if observation[pair[0]][pair[1] - 1] == self.get_disk():
                    weight = 4
                    weights.append((pair, weight))
                else:
                    weight = 0
                    weights.append((pair, weight))

            if pair[0] == last_row and pair[1] == first_col:
                # check only the right
                if observation[pair[0]][pair[1] + 1] == self.get_disk():
                    weight = 4
                    weights.append((pair, weight))
                else:
                    weight = 0
                    weights.append((pair, weight))

            if pair[0] == last_row and pair[1] != last_col and pair[1] != first_col:
                # check right, left and both diagonal
                if observation[pair[0]][pair[1] + 1] == self.get_disk():
                    weight = 5
                    weights.append((pair, weight))
                if observation[pair[0]][pair[1] - 1] == self.get_disk():
                    weight = 5
                    weights.append((pair, weight))
                if observation[pair[0] - 1][pair[1] + 1] == self.get_disk():
                    weight = 6
                    weights.append((pair, weight))
                if observation[pair[0] - 1][pair[1] - 1] == self.get_disk():
                    weight = 6
                    weights.append((pair, weight))
                else:
                    weight = 0
                    weights.append((pair, weight))

            if pair[1] == last_col and pair[0] != last_row:
                # check the down, left or diagonal
                if observation[pair[0]][pair[1] - 1] == self.get_disk():
                    weight = 3
                    weights.append((pair, weight))
                if observation[pair[0] + 1][pair[1]] == self.get_disk():
                    weight = 3
                    weights.append((pair, weight))
                if observation[pair[0] + 1][pair[1]] != self.get_disk() and observation[pair[0] + 1][pair[1]] != 0:
                    weight = 6
                    weights.append((pair, weight))
                if observation[pair[0] + 1][pair[1] - 1] == self.get_disk():
                    weight = 3
                    weights.append((pair, weight))
                else:
                    weight = 0
                    weights.append((pair, weight))

            if pair[1] == first_col and pair[0] != last_row:
                # check the down, left or diagonal
                if observation[pair[0]][pair[1] + 1] == self.get_disk():
                    weight = 3
                    weights.append((pair, weight))
                if observation[pair[0] + 1][pair[1]] == self.get_disk():
                    weight = 3
                    weights.append((pair, weight))
                if observation[pair[0] + 1][pair[1]] != self.get_disk() and observation[pair[0] + 1][pair[1]] != 0:
                    weight = 6
                    weights.append((pair, weight))
                if observation[pair[0] + 1][pair[1] + 1] == self.get_disk():
                    weight = 3
                    weights.append((pair, weight))
                else:
                    weight = 0
                    weights.append((pair, weight))
            else:
                weight = 0
                weights.append((pair, weight))

        return weights

    def action(self, env):
        """
        :param env:
        :return:
        """
        if np.all(env.get_state() == 0):
            row, col = 5, np.random.randint(0, 6)
            return row, col
        vacant_places = np.argwhere(env.get_state() == 0)
        vacant_places = sorted(vacant_places, key=itemgetter(1))
        gs = it.groupby(vacant_places, key=itemgetter(1))
        valid_moves = [max(v, key=itemgetter(0)) for k, v in gs]
        move = max(self.patterns(env.get_state(), valid_moves, env.get_dimension()), key=itemgetter(1))
        row, col = move[0]
        return row, col
