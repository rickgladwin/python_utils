import math
import time


def display(elapsed_time: float, units: str) -> None:
    print(f'elapsed time: {elapsed_time}{units}')
    pass


class Benchmark:
    """Contains tools for benchmarking code performance"""

    time_start: float = 0
    time_end: float = 0
    selected_units: str = None
    unit_options: dict = {
        4:   {'unit': 'h',   'conversion factor': 3600,                 'long name': 'hours'},
        3:   {'unit': 'h',   'conversion factor': 3600,                 'long name': 'hours'},
        2:   {'unit': 'min', 'conversion factor': 60,                   'long name': 'minutes'},
        1:   {'unit': 's',   'conversion factor': 1,                    'long name': 'seconds'},
        0:   {'unit': 's',   'conversion factor': 1,                    'long name': 'seconds'},
        -1:  {'unit': 'ms',  'conversion factor': .001,                 'long name': 'milliseconds'},
        -2:  {'unit': 'ms',  'conversion factor': .001,                 'long name': 'milliseconds'},
        -3:  {'unit': 'ms',  'conversion factor': .001,                 'long name': 'milliseconds'},
        -4:  {'unit': 'μs',  'conversion factor': 0.000001,             'long name': 'microseconds'},
        -5:  {'unit': 'μs',  'conversion factor': 0.000001,             'long name': 'microseconds'},
        -6:  {'unit': 'μs',  'conversion factor': 0.000001,             'long name': 'microseconds'},
        -7:  {'unit': 'ns',  'conversion factor': 0.000000001,          'long name': 'nanoseconds'},
        -8:  {'unit': 'ns',  'conversion factor': 0.000000001,          'long name': 'nanoseconds'},
        -9:  {'unit': 'ns',  'conversion factor': 0.000000001,          'long name': 'nanoseconds'},
        -10: {'unit': 'ps',  'conversion factor': 0.000000000001,       'long name': 'picoseconds'},
        -11: {'unit': 'ps',  'conversion factor': 0.000000000001,       'long name': 'picoseconds'},
        -12: {'unit': 'ps',  'conversion factor': 0.000000000001,       'long name': 'picoseconds'},
        -13: {'unit': 'fs',  'conversion factor': 0.000000000000001,    'long name': 'femtoseconds'},
        -14: {'unit': 'fs',  'conversion factor': 0.000000000000001,    'long name': 'femtoseconds'},
        -15: {'unit': 'fs',  'conversion factor': 0.000000000000001,    'long name': 'femtoseconds'}
    }
    default_unit_option: dict = unit_options[0]
    default_precision: int = 6

    def start(self) -> None:
        self.time_start = time.time()

    def end(self) -> None:
        self.time_end = time.time()
        elapsed = self.time_end - self.time_start
        elapsed_sig_decimal = math.floor(math.log(elapsed, 10))
        selected_unit_set = self.default_unit_option
        if elapsed_sig_decimal in self.unit_options.keys():
            selected_unit_set = self.unit_options[elapsed_sig_decimal]

        elapsed_time = round(elapsed / selected_unit_set["conversion factor"], self.default_precision)
        units = selected_unit_set["unit"]

        display(elapsed_time=elapsed_time, units=units)
