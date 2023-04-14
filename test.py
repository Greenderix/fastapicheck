import sys

# Словарь для хранения переменных и их значений
variables = {}

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ValueError("Division by zero")
    return a // b

# Функция для выполнения пользовательской функции
def execute_function(function_name, args):
    if function_name == "add":
        return add(args[0], args[1])
    elif function_name == "sub":
        return sub(args[0], args[1])
    elif function_name == "mul":
        return mul(args[0], args[1])
    elif function_name == "div":
        return div(args[0], args[1])
    elif function_name in variables:
        # Выполнение рекурсивного вызова функции
        function_args = [int(arg) if arg.isdigit() else variables[arg] for arg in variables[function_name]]
        return execute_function(function_name, function_args)
    else:
        raise ValueError("Unknown function: {}".format(function_name))

# Функция для выполнения команды и записи результата в переменную
def execute_command(command):
    global variables
    parts = command.split()
    if parts[0] == "init":
        # Инициализация переменной
        var_name = parts[1]
        if parts[2].isdigit():
            var_value = int(parts[2])
        else:
            var_value = parts[2]
        variables[var_name] = var_value
    elif parts[0] == "function":
        # Объявление пользовательской функции
        function_name = parts[1]
        args = parts[2:]
        variables[function_name] = args
    elif parts[0] == "return":
        # Возврат результата из функции
        var_name = parts[1]
        print(variables[var_name]) # Вывод результата в stdout
    elif parts[0] == "end_program":
        # Завершение программы
        sys.exit(0)
    else:
        # Выполнение пользовательской функции
        function_name = parts[0]
        args = [int(arg) if arg.isdigit() else variables[arg] for arg in parts[1:]]
        result = execute_function(function_name, args)
        # Запись результата в переменную
        var_name = parts[-1]
        variables[var_name] = result

# Главная функция решения
def solution(f_in, f_out):
    for line in f_in:
        command = line.strip()
        execute_command(command)

if __name__ == "__main__":
    solution(sys.stdin, sys.stdout)
