import random
import numpy as np
from operator import itemgetter
import itertools as it


class Agent:
    """"
    this agent represent a simple a approach that consist of using the hazard
    i call this the random agent
    """
    def __init__(self, agent_name, piece):
        self.agent_name = agent_name
        self.piece = piece
        pass

    def get_piece(self):
        return self.piece

    def get_agent_name(self):
        return self.agent_name

    @staticmethod
    def action(observation, dimension):
        """
        :param observation:
        :param dimension
        :return:
        """
        columns = list()
        for col_ in range(dimension[1]):
            if observation[0][col_] == 0:
                columns.append(col_)
        col = random.choice(columns)
        for row in reversed(range(dimension[0])):
            if observation[row][col] == 0:
                return row, col


class AgentLeftMost:
    """"
    this agent use a strategy that consists of playing the piece on the left
    """
    def __init__(self, agent_name, piece):
        self.agent_name = agent_name
        self.piece = piece
        pass

    def get_piece(self):
        return self.piece

    def get_agent_name(self):
        return self.agent_name

    @staticmethod
    def action(observation, dimension):
        """
        :param observation:
        :param dimension
        :return:
        """
        for col_ in range(dimension[1]):
            for row_ in reversed(range(dimension[0])):
                if observation[row_][col_] == 0:
                    return row_, col_
                pass
            pass
        pass


class HeuristicAgent:
    """
    this agent will use a heuristic that make choose wisely the place of piece by looking all the vacant
    places around and a sign a specific score for each possible place
    """
    def __init__(self, agent_name, piece):
        self.agent_name = agent_name
        self.piece = piece
        pass

    def get_piece(self):
        return self.piece

    def get_agent_name(self):
        return self.agent_name

    def get_patterns(self, observation, pairs, dimension):
        """
        this function will get the patterns for the move for each move will assign a specific weight
        to weight my moves i choose a scale from 1 to 10
        :param observation:
        :param pairs:
        :param dimension:
        :return:
        """
        weights = list()
        last_row, last_col = dimension[0]-1, dimension[1]-1
        first_col = 0
        for pair in pairs:
            if pair[0] == last_row and pair[1] == last_col:
                # check the left
                if observation[pair[0]][pair[1]-1] == self.get_piece():
                    weight = 5
                    weights.append((pair, weight))
                else:
                    weight = 1
                    weights.append((pair, weight))

            elif pair[0] == last_row and pair[1] == first_col:
                # check only the right
                if observation[pair[0]][pair[1]+1] == self.get_piece():
                    weight = 5
                    weights.append((pair, weight))
                else:
                    weight = 1
                    weights.append((pair, weight))

            elif pair[0] == last_row:
                # check right, left and both diagonal
                if observation[pair[0]][pair[1]+1] == self.get_piece():
                    weight = 6
                    weights.append((pair, weight))
                elif observation[pair[0]][pair[1]-1] == self.get_piece():
                    weight = 6
                    weights.append((pair, weight))
                elif observation[pair[0]-1][pair[1]+1] == self.get_piece():
                    weight = 7
                    weights.append((pair, weight))
                elif observation[pair[0]-1][pair[1]-1] == self.get_piece():
                    weight = 7
                    weights.append((pair, weight))
                else:
                    weight = 7
                    weights.append((pair, weight))

            elif pair[1] == last_col:
                # check the down, left or diagonal
                if observation[pair[0]][pair[1]-1] == self.get_piece():
                    weight = 5
                    weights.append((pair, weight))
                elif observation[pair[0]+1][pair[1]] == self.get_piece():
                    weight = 8
                    weights.append((pair, weight))
                elif observation[pair[0]+1][pair[1]-1] == self.get_piece():
                    weight = 7
                    weights.append((pair, weight))
                else:
                    weight = 4
                    weights.append((pair, weight))

            elif pair[1] == first_col:
                # check only the right, diagonal, the down and the opponent piece
                if observation[pair[0]][pair[1]+1] == self.get_piece():
                    weight = 5
                    weights.append((pair, weight))
                elif observation[pair[0]+1][pair[1]] == self.get_piece():
                    weight = 8
                    weights.append((pair, weight))
                elif observation[pair[0]+1][pair[1]+1] == self.get_piece():
                    weight = 7
                    weights.append((pair, weight))
                else:
                    weight = 4
                    weights.append((pair, weight))

            else:
                # check only the right, diagonal, the down and the opponent piece
                if observation[pair[0]][pair[1] + 1] == self.get_piece():
                    weight = 5.5
                    weights.append((pair, weight))
                elif observation[pair[0]][pair[1]-1] == self.get_piece():
                    weight = 5.5
                    weights.append((pair, weight))
                elif observation[pair[0]+1][pair[1]] == self.get_piece():
                    weight = 8
                    weights.append((pair, weight))
                elif observation[pair[0]+1][pair[1]+1] == self.get_piece():
                    weight = 7.5
                    weights.append((pair, weight))
                elif observation[pair[0]+1][pair[1]-1] == self.get_piece():
                    weight = 7.5
                    weights.append((pair, weight))
                else:
                    weight = 5
                    weights.append((pair, weight))
        return weights

    def action(self, observation, dimension):
        if np.all(observation == 0):
            row, col = 5, random.randint(0, 6)
            return row, col
        vacant_places = np.argwhere(observation == 0)
        s_vacant_places = sorted(vacant_places, key=itemgetter(1))
        gs = it.groupby(s_vacant_places, key=itemgetter(1))
        valid_moves = [max(v, key=itemgetter(0)) for k, v in gs]
        move = max(self.get_patterns(observation, valid_moves, dimension), key=itemgetter(1))
        row, col = move[0]
        return row, col
