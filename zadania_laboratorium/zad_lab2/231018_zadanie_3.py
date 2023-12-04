def task_time(name, num, time):
    seconds = time / 1000
    return f"{name} has done the task no.{num} in {seconds:4} sec."


print(task_time("Aleks", 1, 1137))
