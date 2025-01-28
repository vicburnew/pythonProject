def circle_area(rad: int) -> float:
    """Вычисление площади круга по радиусу"""
    pi = 3.14
    area_calculation = pi * rad**2
    return area_calculation


def format_output_message(rad: int, area: float) -> str:
    """Формат выходного сообщения"""
    return "Radius is " + str(rad) + "; area is " + str(round(area, 2))


def get_info(r: int) -> None:
    """Вычисление и вывод ответа"""
    area = circle_area(r)
    description = format_output_message(r, area)
    print(description)


radius = int(input("Enter circle radius (int): "))
get_info(radius)
