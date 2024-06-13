'''
1. Перед вами код модуля, который подсчитывает репутацию персонажа после поединка,
но качество кода в этом модуле оставляет желать лучшего. Ваша задача — навести порядок в этом коде:
проаннотировать переменные и функции,
привести код в соответствие с PEP8.

2. Проаннотируйте код в файле main.py проекта character_creation_module. Результат скопируйте в тренажёр и
нажмите кнопку «Проверить».
Обратите внимание, что вызов функции main() в тренажёре не нужен, поэтому не нужно его копировать.
Когда проверка пройдёт успешно, отправьте код на GitHub.
'''
# Тестовые данные.
TEST_DATA: list[tuple[int, str, bool]] = [
    (44, 'success', True),
    (16, 'failure', True),
    (4, 'success', False),
    (21, 'failure', False),
]

BONUS: float = 1.1
ANTIBONUS: float = 0.8


def add_rep(current_rep: float, rep_points: int, buf_effect: bool) -> float:
    current_rep += rep_points
    if buf_effect:
        return current_rep * BONUS
    return current_rep


def remove_rep(current_rep: float,
               rep_points: int, debuf: bool) -> float:
    current_rep -= rep_points
    if debuf:
        return current_rep * ANTIBONUS
    return current_rep


def main(duel_res: list[tuple[int, str, bool]]) -> str:
    current_rep = 0.0
    for rep, result, effect in duel_res:
        if result == 'success':
            current_rep = add_rep(current_rep, rep, effect)
        if result == 'failure':
            current_rep = remove_rep(current_rep, rep, effect)
    return (f'После {len(duel_res)} поединков, '
            f'репутация персонажа — {current_rep:.3f} очков.')


# Тестовый вызов функции main.
print(main(TEST_DATA))
