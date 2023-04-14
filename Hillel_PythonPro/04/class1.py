from datetime import datetime, date
import re


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
                case '<':
                    self.alignment = str.ljust
                case '^':
                    self.alignment = str.center
                case '>':
                    self.alignment = str.rjust
        if self.alignment is None:
            self.alignment = str.ljust
        else:
            self.header = self.header[1:]
        self.values = [column_info.property_as_string_selector(_item) for _item in items]
        self.width = max([strlen(_value) for _value in self.values] + [len(self.header)])
        self.values = [align(_value, self.width, self.alignment) for _value in self.values]
        self.header = f" {self.header} ".center(self.width + 2, "─")
        self.footer = "─" * (self.width + 2)


class StrHelper:
    @staticmethod
    def as_table(table_header: str, items, columns_info: list[ColumnInfo]):
        _str = f" {table_header} ({'—' if items is None else len(items)} шт.)"
        if items is None:
            return _str
        _columns = [Column(_column_info, items) for _column_info in columns_info]
        _str += f"\n╭{'┬'.join([f'{_column.header}' for _column in _columns])}╮"
        for _i in range(len(items)):
            _str += f"\n│{'│'.join([f' {_column.values[_i]} ' for _column in _columns])}│"
        _str += f"\n╰{'┴'.join([f'{_column.footer}' for _column in _columns])}╯"
        return _str

    @staticmethod
    def get_only_digits(value: str) -> str:
        _str = ""
        if value is not None and len(value) > 0:
            _str = _str.join(re.findall(r'\d+', value))
        return _str

    @staticmethod
    def find(string: str, substring: str) -> bool:
        if substring is None or len(substring) == 0:
            return True
        _str = string.lower()
        _sub_str = substring.strip('*').lower()
        if substring.startswith('*') and not substring.endswith('*'):
            return _str.endswith(_sub_str)
        if not substring.startswith('*') and substring.endswith('*'):
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

class Record:
    @staticmethod
    def as_view_str(title: str, records: list[Record]) -> str:
        _str_table = StrHelper.as_table(title, records, [
            ColumnInfo('>id', lambda e: str(e.idx)),
            ColumnInfo('Дата модифікації', lambda e: AsStr.date_time(e.modified_at)),
            ColumnInfo('Прізвище', lambda e: e.last_name),
            ColumnInfo('Ім''я', lambda e: e.first_name),
            ColumnInfo('^Дата народження', lambda e: AsStr.date(e.date_of_birth)),
            ColumnInfo('Телефон', lambda e: e.phone_number),
            ColumnInfo('Адреса', lambda e: e.address),
        ])
        return _str_table



if __name__ == '__main__':
    print(StrHelper.find("Пупкін", "*пк*"))
