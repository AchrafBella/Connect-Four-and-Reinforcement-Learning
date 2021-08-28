from abc import ABC, abstractmethod


class Agent(ABC):
    def __init__(self, agent_name, disk):
        self._agent_name = agent_name
        self._disk = disk

    def get_disk(self):
        return self._disk

    def get_agent_name(self):
        return self._agent_name

    @abstractmethod
    def action(self):
        pass
