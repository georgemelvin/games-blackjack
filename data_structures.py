"""

"""


class Stack:
    """

    """


    def __init__(self):
        self.items = []

    def get_item(self):
        if not self.is_empty():
            item = self.items[0]
            self.items = self.items[1:]

            return item
        else:
            print('Stack is empty...! No items to get.')

    def append_item(self, item):
        self.items = [item] + self.items

    def count_items(self):
        return len(self.items)

    def echo(self):
        return self.items

    def is_empty(self):
        if self.items:
            return False
        else:
            return True

if __name__ == '__main__':
    s = Stack()
    print(s.is_empty())
    s.append_item('a')
    print(s.echo())
    s.append_item('b')
    print(s.echo())
    s.append_item('c')
    print(s.get_item())
    print(s.echo())
