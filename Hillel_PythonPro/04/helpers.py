import re
from datetime import date, datetime


class ColumnInfo:
    def __init__(self, header, property_as_string_selector):
        self.header = header
        self.property_as_string_selector = property_as_string_selector


class Column:
    def __init__(self, column_info: ColumnInfo, items):
        def strlen(value: str):
            return 0 if value is None else len(value)

        def align(value: str, width: int, alignfunc):
            if value is None:
                return " " * width
            return alignfunc(value, width)

        self.header = column_info.header
        self.alignment = None
        if self.header is not None and len(self.header) > 0:
            match self.header[0]:
                case "<":
                    self.alignment = str.ljust
                case "^":
                    self.alignment = str.center
                case ">":
                    self.alignment = str.rjust
        if self.alignment is None:
            self.alignment = str.ljust
        else:
            self.header = self.header[1:]
        self.values = [
            column_info.property_as_string_selector(_item) for _item in items
        ]
        self.width = max(
            [strlen(_value) for _value in self.values] + [len(self.header)]
        )
        self.values = [
            align(_value, self.width, self.alignment) for _value in self.values
        ]
        self.header = f" {self.header} ".center(self.width + 2, "─")
        self.footer = "─" * (self.width + 2)
        # ->


class StrHelper:
    @staticmethod
    def as_table(table_header: str, items, columns_info: list[ColumnInfo]):
        _str = f" {table_header} ({'—' if items is None else len(items)} шт.)"
        if items is None:
            return _str
        _columns = [Column(_column_info, items) for _column_info in columns_info]
        _str += f"\n╭{'┬'.join([f'{_column.header}' for _column in _columns])}╮"
        for _i in range(len(items)):
            _str += (
                f"\n│{'│'.join([f' {_column.values[_i]} ' for _column in _columns])}│"
            )
        _str += f"\n╰{'┴'.join([f'{_column.footer}' for _column in _columns])}╯"
        return _str

    @staticmethod
    def get_only_digits(value: str) -> str:
        _str = ""
        if value is not None and len(value) > 0:
            _str = _str.join(re.findall(r"\d+", value))
        return _str

    @staticmethod
    def find(string: str, substring: str) -> bool:
        if substring is None or len(substring) == 0:
            return True
        _str = string.lower()
        _sub_str = substring.strip("*").lower()
        if substring.startswith("*") and not substring.endswith("*"):
            return _str.endswith(_sub_str)
        if not substring.startswith("*") and substring.endswith("*"):
            return _str.startswith(_sub_str)
        return _sub_str in _str


class AsStr:
    @staticmethod
    def date_time(value: datetime):
        if value is None:
            return ""
        weekday = value.weekday() + 1
        return f"{value:%Y.%m.%d}({weekday})  {value:%H:%M:%S}"

    @staticmethod
    def date(value: date):
        if value is None:
            return ""
        weekday = value.weekday() + 1
        return f"{value:%Y.%m.%d}({weekday})"


class UsrInput:
    @staticmethod
    def get_number(input_str: str, int_constraints: list[int] = None) -> int:
        """Отримати введене з консолі користувачем число
        :param input_str: Текст запрошення вводу даних для користувача
        :param int_constraints: [Опціонально] Список можливих чисел, що може ввести користувач
        :return: Число, що було отримано від користувача
        """
        _user_input = None
        while _user_input is None:
            try:
                _user_input = int(input(f"{input_str} > "))
                if int_constraints is not None and _user_input not in int_constraints:
                    print(
                        "\33[41mПОМИЛКА ВВОДУ ДАННИХ.\33[0m оберіть з поміж \33[33mДОСТУПНИХ\33[0m числових значень!"
                    )
                    _user_input = None
            except ValueError:
                print(
                    "\33[41mПОМИЛКА ВВВОДУ ДАННИХ.\33[0m Оберіть \33[33mЧИСЛОВЕ\33[0m значення!"
                )
        return _user_input

    @staticmethod
    def get_str(
        input_str: str, min_len: int = 0, str_constraints: list[str] = []
    ) -> str:
        """Отримати введену з консолі користувачем стрічку
        :param input_str: Текст запрошення вводу даних для користувача
        :param min_len: [Опціонально] Мінімальна довжина рядка, який повинен ввести користувач
        :param str_constraints: [Опціонально] Список доступних для введення стрічок
        :return: Рядок, що був отриманий від користувача
        """
        _user_input: str | None = None
        while _user_input is None:
            _user_input = input(f"{input_str} > ")
            if (
                min_len is not None
                and _user_input is not None
                and len(_user_input) < min_len
            ):
                print(
                    f"\33[41mПОМИЛКА ВВОДУ ДАННИХ.\33[0m Ведіть рядок не коротше ніж {min_len} символи"
                )
                _user_input = None
            if (
                str_constraints is not None
                and len(str_constraints) > 0
                and _user_input not in str_constraints
            ):
                print(
                    f"\33[41mПОМИЛКА ВВОДУ ДАННИХ.\33[0m Ведіть рядок з поміж доступних варіантів ({str_constraints})"
                )
                _user_input = None
        return _user_input

    @staticmethod
    def get_date(input_str: str, can_be_none: bool = False) -> date | None:
        """Отримати введену з консолі користувачем дату
        :param input_str: Текст запрошення вводу даних для користувача
        :param can_be_none: [Опціонально] чи може бути значення отримане від користувача None
        :return: Дата, що була отримана від користувача
        """
        _result: date | None = None
        while _result is None:
            try:
                _usr_input = input(f"{input_str} > ")
                if _usr_input is None or len(_usr_input) == 0:
                    if can_be_none:
                        return None
                    else:
                        raise ValueError("Date is None")

                _temp_res: datetime = datetime.strptime(_usr_input, "%Y-%m-%d")
                if _temp_res is None:
                    print("\33[41mПОМИЛКА ВВОДУ ДАННИХ.\33[0m значення обов'язкове!")
                    _result = None
                else:
                    _result = date(_temp_res.year, _temp_res.month, _temp_res.day)
            except ValueError:
                print(
                    "\33[41mПОМИЛКА ВВВОДУ ДАННИХ.\33[0m Введіть \33[33mДАТУ\33[0m в форматі yyyy-MM-dd"
                )
                _result = None
        return _result


def main():
    ...


if __name__ == "__main__":
    main()
