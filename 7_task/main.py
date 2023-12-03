from cleaner_api import CleanerApi

# главная программа
cleaner = CleanerApi()
cleaner.activate_cleaner((
    'move 100',
    'move 100',
    'turn -90',
    'set soap',
    'start',
    'move 50',
    'stop'
    ))

print(cleaner.get_x())
print(cleaner.get_y())
print(cleaner.get_angle())
print(cleaner.get_state())
