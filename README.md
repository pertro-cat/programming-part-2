# programming-part-2
this my lab V 1
Варіант 1
Дані два масиви цілих чисел nums1 і nums2, де nums1 є підмасивом nums2, якщо всі елементи nums1 знаходяться в nums2, в тому ж порядку.

Напишіть функцію is_subarray, яка приймає два масиви цілих чисел та повертає True, якщо nums1 є підмасивом nums2, та False в іншому випадку.

Приклади Вхідні дані: nums1 = 1,2,3, nums2 = 1,2,3,4 Результат: True Пояснення: Всі елементи nums1 ([1,2,3]) присутні в nums2.

Вхідні дані: nums1 = [4, 2], nums2 = [1,2,3,4] Результат: False Пояснення: Елементи nums1 ([4, 2]) не знаходяться в тому ж порядку в nums2.

Вхідні дані: nums1 = [1,3,5], nums2 = [1,2,3,4,5] Результат: True Пояснення: Елементи nums1 ([1,3,5]) присутні в nums2.

Для перевірки виконання роботи реалізованого алгоритму слід використати бібліотеку unittest та перевірити роботу вашої функції на прикладах, наведених вище
Варіант 1
Зеник подарував Марічці ділянку городу розміром n на m, поділену на клітинки розміром 1 на 1 метр. У кожній клітинці Марічка посадила гарбузи, щоб дарувати їх залицальникам. Марічка почала садити гарбузи починаючи із верхньої лівої, і при досягненні правої межі - розверталась і рухалась справа наліво, як вказано в прикладі для m x n, де m - кількість рядків, а n - кількість стовпців:

1 2 3 4 8 7 6 5 9 10 11 12 16 15 14 13

Для садіння Марічка вирішила використати робота-садівника, який садить в кожну клітинку задану кількість зернят, які слід вказати як одномірний масив m x n. Якщо Марічка хоче посадити таку кількість гарбузів

1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16

Тоді роботу необхідно подати на всід таку послідовність (маршрут робота не незмінним):

1 2 3 4 8 7 6 5 9 10 11 12 16 15 14 13

Реалізуйте алгоритм, який отримає на вхід масив розміром m та n, в кожній клітинці якого знаходиться бажана кількість гарбузів та поверне одномірний масив, скільки зернин має висаджувати робот при руху згідно маршруту, вказаного в цій задчі (маршрут є незмінним)

Для перевірки виконання роботи реалізованого алгоритму слід використати бібліотеку unittest . Ваш тести мають перевірити роботу алгоритму при значеннях m == n == 5, m =2, n =4, n = 1, m = 6
Потрібно написати програму для обходу двовимірного масиву розміром NxM у форматі "зігзагу". Зігзаговий обхід означає, що спочатку ми рухаємось по діагоналях масиву, пчинаючи з лівої верхньої точки. Другим елементом буде виведено елемент, який знаходиться справа, потім знизу і ліворуч, далі ще крок вниз і рухаємось по діагоналі знову вправо. Для масиву розміром 3x3 обхід у форматі зігзагу виглядає так (де номер у клітинці відповідає порядку її відвідин):

1 2 6 3 5 7 4 8 9

Для масиву 3 х 5 це матиме вигляд:

1 2 6 7 12 3 5 8 11 13 4 9 10 14 15

Реалізуйте алгоритм, який отримає на вхід масив розміром m та n та поверне одномірний масив з значеннями елементів вхідного масиву при обході його у порядку, зазначеному вище у задачі

Для перевірки виконання роботи реалізованого алгоритму слід використати бібліотеку unittest . Ваш тести мають перевірити роботу алгоритму при значеннях m == n == 5, m =2, n =4, n = 1, m = 6, n == m == 1
