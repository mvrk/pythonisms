from functools import wraps
from time import sleep
import pytest_watch


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, collection=None):
        self.head = None
        self._length = 0
        if collection:
            for item in reversed(collection):
                self.insert(item)

    def __getitem__(self, index):
        if index < 0:
            raise IndexError
        for i, item in enumerate(self):
            if i == index:
                return item

    def __str__(self):
        string = ''
        for value in self:
            string += f'[{value}]'

    def __iter__(self):
        def generator():
            current = self.head
            while current:
                yield current.value
                current = current.next

        return generator()

    def traverse(self, action):
        current = self.head
        while current:
            action(current.value)
            current = current.next

    def __eq__(self, other):
        return list(self) == list(other)

    def __len__(self):
        return len(list(iter(self)))


def has_beef(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        type_of_spicy = func(*args, **kwargs)

        spiced = type_of_spicy.upper() + "has hot spicy"

        return spiced


def wait_for_noodle(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        sleep(3)
        return func(*args, **kwargs)

    return wrapper


@wait_for_noodle
@has_beef
def say(txt):
    return txt


if __name__ == "__main__":
    print(say("beef noddle"))
