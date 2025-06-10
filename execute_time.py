import time

def speed_calc_decorator(function):
    def calc_time():
        start_time = time.time()
        function()
        end_time = time.time()
        func_time = end_time - start_time
        print(f"{function.__name__} run speed is {func_time}")
    return calc_time
@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i * i
@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        i * i
fast_function()
slow_function()
