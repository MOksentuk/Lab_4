import timeit as tt
import Functions


def qsortcall(mass):
    start_time = tt.default_timer()
    print('результат:', Functions.Qsort(mass))
    print('время сортировки:', tt.default_timer() - start_time)
    return ''


def combsortcall(mass):
    start_time = tt.default_timer()
    print('результат:',Functions.combsort(mass))
    print('время сортировки:',tt.default_timer() - start_time)
    return ''


def work():
    print('Введите массив, который нужно отсортировать (в качестве разделителей используйте запятую):')
    mass = list(map(int, input().split(',')))
    print("Выберите метод сортировки (укажите его номер):\n1.Qsort\n2.Сombsort")
    i = input()
    if i == '1':
        qsortcall(mass)
    elif i == '2':
        combsortcall(mass)
    return ''
work()
