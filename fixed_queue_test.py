from enum import Enum
from fixed_queue import FixedQueue

Menu = Enum('Menu', [
    'inque',
    'deque',
    'peek',
    'search',
    'dump',
    'exit',
])


def select_menu() -> Menu:
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep='   ', end='')
        n = int(input(': '))
        if 1<=n<=len(Menu):
            return Menu(n)

q = FixedQueue(64)

while True:
    print(f'현재 데이터 개수 : {len(q)}/ {q.capacity}')
    menu = select_menu()

    if menu == Menu.inque:
        x = int(input('input inque data'))
        try:
            q.enque(x)
        except FixedQueue.Full:
            print('queue is full')

    elif menu == Menu.deque:
        try:
            x = q.deque()
            print(f'deque data is {x}')
        except FixedQueue.Empty:
            print('queue is empty')

    elif menu == Menu.peek:
        try:
            x= q.peek()
            print(f'peek data is {x}')
        except FixedQueue.Empty:
            print('queue is empty')

    elif menu == Menu.search:
        x = int(input('search data input'))
        if x in q:
            print(f'{q.count(x)}개 포함되고, 만 앞의 위치는 {q.find(x)}')
        else:
            print('no search')

    elif menu == Menu.dump:
        q.dump()
    else:
        break