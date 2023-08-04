from panther.db import Model


class Person(Model):
    first_name: str
    last_name: str
    age: int


class Book(Model):
    author: Person
    pages_count: int
    is_available: bool
