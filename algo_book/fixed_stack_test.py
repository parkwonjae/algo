from enum import Enum
from algo_book.fixed_stack import FixedStack

Menu = Enum('Menu', ['push', 'pop', 'peek', 'search', 'dump', 'exit'])


def select_menu():
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep='   ', end='')
        n = int(input(': '))
        if 1<=n<=len(Menu):
            return Menu(n)


s = FixedStack(64)

while True:
    print(f'현재 데이터 개수 {len(s)} / {s.capacity}')
    menu = select_menu()

    if menu == Menu.push:
        x = int(input('inter data'))
        try:
            s.push(x)
        except FixedStack.Full:
            print('stack is full')

    elif menu == Menu.pop:
        try:
            x = s.pop()
            print(f'pop data is {x}')
        except FixedStack.Empty:
            print('stack is empty')

    elif menu == Menu.peek:
        try:
            x = s.peek()
            print(f'peek data is {x}')
        except FixedStack.Empty:
            print('stack is empty')

    elif menu == Menu.search:
        x = int(input('search data is : '))
        if x in s:
            print(f'{s.count(x)} contains, front is {s.find(x)}')
        else:
            print('no search')

    elif menu == Menu.dump:
        s.dump()

    else:
        break