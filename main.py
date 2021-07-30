from environment import Env
import numpy as np

if __name__ == "__main__":

    Env = Env()
    Env.drop_peace(5, 6, 1)
    Env.drop_peace(4, 6, 1)
    Env.drop_peace(4, 3, 1)
    game_over = Env.is_done()
    print("the game is {}".format(game_over))
    Env.display_env()