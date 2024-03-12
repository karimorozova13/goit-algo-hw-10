# Висновки

## Результати інтегрування:

Результати обчислення інтегралу методом Монте-Карло та вбудованою функцією quad є дуже близькими між собою. Це свідчить про ефективність розв'язку методом Монте-Карло для цього конкретного інтегралу.

## Точність інтегралу методом Монте-Карло:

Точність результату методом Монте-Карло є дуже хорошою, оскільки вона близька до результату вбудованої функції quad. Cимуляція використовує випадкові точки для ефективного апроксимування інтегралу при умові симуляції екстремальної кількості разів. У випадку, коли симуляція менше 100 разів, результат значно відрізняється від вбудованої функції quad і є неправильним.

## Продуктивність:

Pеалізація методу Монте-Карло працює ефективно, навіть для великої кількості точок (10 мільйонів) у симуляції.

Загалом, реалізація є вдалим прикладом використання методу Монте-Карло для обчислення інтегралів, і вона працює добре в порівнянні з вбудованою функцією SciPy.