from abc import ABC, abstractmethod


class BaseOrderCategory(ABC):
    """общие интерфейсы для классов Category и OrderProduct"""
    @abstractmethod
    def __str__(self):
        pass
