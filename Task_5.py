import json
import time

# Функция для генерации итогового отчета
def generate_final_report():
    # Инициализация словаря с содержимым отчета
    final_report = {
        "задачи": [
            {
                "номер": 1,
                "название": "Задание 1",
                "трудности": "Никаких трудностей не возникло.",
                "время_выполнения": "00:10:00",  # Пример времени выполнения
                "выводы": "Задание успешно выполнено.",
                "предложения": "Оптимизировать код для повышения читаемости."
            },
            {
                "номер": 2,
                "название": "Задание 2",
                "трудности": "Проблемы с импортом библиотеки.",
                "время_выполнения": "00:15:00",
                "выводы": "Библиотека была импортирована корректно после исправления.",
                "предложения": "Проверять импорты в начале."
            },
            # Добавьте аналогичные словари для других заданий...
        ],
        "итог": "Все задания выполнены успешно, некоторые трудности были решены."
    }

    # Запись отчета в JSON-файл
    with open('project_root/output/final_report.json', 'w', encoding='utf-8') as report_file:
        json.dump(final_report, report_file, ensure_ascii=False, indent=4)

# Вызов функции для генерации итогового отчета
generate_final_report()
