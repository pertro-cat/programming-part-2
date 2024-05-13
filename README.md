# Лабораторна 1 рівень 2: Про поле де робот садить гарбузи

Зеник подарував Марічці ділянку городу розміром n на m, поділену на клітинки розміром 1 на 1 метр. У кожній клітинці Марічка посадила гарбузи, щоб дарувати їх залицальникам. Марічка почала садити гарбузи починаючи із верхньої лівої, і при досягненні правої межі — розверталась і рухалась справа наліво, як вказано в прикладі для m x n, де m — кількість рядків, а n — кількість стовпців:

1 2 3 4  
8 7 6 5  
9 10 11 12  
16 15 14 13  

Для садіння Марічка вирішила використати робота-садівника, який садить в кожну клітинку задану кількість зернят, які слід вказати як одномірний масив m x n. Якщо Марічка хоче посадити таку кількість гарбузів:

1 2 3 4  
5 6 7 8  
9 10 11 12  
13 14 15 16  

Тоді роботу необхідно подати на вхід таку послідовність (маршрут робота не незмінним):

1 2 3 4  
8 7 6 5  
9 10 11 12  
16 15 14 13  

Реалізуйте алгоритм, який отримає на вхід масив розміром m та n, в кожній клітинці якого знаходиться бажана кількість гарбузів та поверне одномірний масив, скільки зернин має висаджувати робот при руху згідно маршруту, вказаного в цій задачі (маршрут є незмінним).

Для перевірки виконання роботи реалізованого алгоритму слід використати бібліотеку unittest. Ваш тести мають перевірити роботу алгоритму при значеннях m == n == 5, m = 2, n = 4, n = 1, m = 6.




"""
Лабораторна 1 рівень 2
Про поле де робот садить гарбузи
Зеник подарував Марічці ділянку городу розміром n на m, поділену на клітинки розміром 1 на 1 метр. У кожній клітинці Марічка посадила гарбузи, щоб дарувати їх залицальникам. Марічка почала садити гарбузи починаючи із верхньої лівої, і при досягненні правої межі - розверталась і рухалась справа наліво, як вказано в прикладі для m x n, де m - кількість рядків, а n - кількість стовпців:

1 2 3 4 8 7 6 5 9 10 11 12 16 15 14 13

Для садіння Марічка вирішила використати робота-садівника, який садить в кожну клітинку задану кількість зернят, які слід вказати як одномірний масив m x n. Якщо Марічка хоче посадити таку кількість гарбузів

1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16

Тоді роботу необхідно подати на всід таку послідовність (маршрут робота не незмінним):

1 2 3 4 8 7 6 5 9 10 11 12 16 15 14 13

Реалізуйте алгоритм, який отримає на вхід масив розміром m та n, в кожній клітинці якого знаходиться бажана кількість гарбузів та поверне одномірний масив, скільки зернин має висаджувати робот при руху згідно маршруту, вказаного в цій задчі (маршрут є незмінним)

Для перевірки виконання роботи реалізованого алгоритму слід використати бібліотеку unittest . Ваш тести мають перевірити роботу алгоритму при значеннях m == n == 5, m =2, n =4, n = 1, m = 6

"""

"""
Лабораторна 2 рівень 3
Про максимальну кількісь хом'яків
Зоомагазин займається продажем хом’ячкiв. Це мирнi домашнi iстоти, проте, як виявилося, вони мають цiкаву харчову поведiнку. Для того, щоб прогодувати хом’ячка, який живе наодинцi, потрiбно H пакетiв корму на день. Однак, якщо кiлька хом’ячкiв живуть разом, у них прокидається жадiбнiсть. У такому випадку кожен хом’ячок з’їдає додатково G пакетiв корму в день за кожного сусiда. Денна норма H та жадiбнiсть G є iндивiдуальними для кожного хом’ячка. Всього в магазинi є C хом’ячкiв. Ви бажаєте придбати якомога бiльше, проте у вас є всього S пакетiв їжi на день. Визначте максимальну кiлькiсть хом’ячкiв, яку ви можете прогодувати.

Реалізуйте функцію, яка поверне число - максимальне число хо Вхідні параметри функції: S — ваш денний запас їжi. 0 ≤ S ≤ 109 C — загальна кiлькiсть хом’ячкiв, яка є в продажу, 1 ≤ C ≤ 105 Матриця hamsters, яка містить С рядків, перший стовчик якої містить денну норму корму, другий - рiвень жадiбностi кожного хом’ячка. Деннs нормb є цілими додатніми числами і гарантовано меншими за 109. Іноді у вас можуть бути не жадібні хом’ячки, але також можуть траплятись і надзвичайно жадібні, рівень жадібності може бути як нульовим, так і великим цілим числом

Приклад 1

S = 7 C = 3 hamsters = `[ [1 2], [2 2], [3 1]]``

Результат: 2

Пояснення: Можна взяти першого хом’ячка та будь-якого з iнших двох.

Приклад 2

S = 19 C = 4 hamsters = `[ [5 0], [2 2], [1 4], [5 1]]

Результат: 3 Пояснення: Третiй хом’ячок надто жадiбний. Можна взяти всiх iнших трьох, тодi за день вони з’їдять (5 + 0 · 2) + (2 + 2 · 2) + (5 + 1 · 2) = 18 пакетiв

Приклад 3 hamstr .in S = 2 C = 2 hamsters = `[[1 50000], [1 60000]]

Результат: 1 Пояснення: Обидва хом’ячки надто жадiбнi, щоб їсти разом.

Для перевірки виконання роботи реалізованого алгоритму слід використати бібліотеку unittest та перевірити роботу вашої функції на прикладах, наведених вище
"""

"""
Лабораторна 3 рівень 3
Пошук наступника в бінарному дереві 
Для заданого бінарного дерева та конкретної вершини в цьому дереві реалізуйте функцію пошуку наступного елемента під час серединного проходу (in-order traversal). Наступник - це вузол, який має значення більше за заданий вузол і знаходиться найближче до нього при серединному обході.

Нехай у вас задане бінарне дерево такого вигляду:

    10
   /  \
  5    15
 / \     \
3   7    20
         /
        12

Для вершини зі значенням 7, наступник - це вузол зі значенням 10.

Функція отримує на вхід корінь бінарного дерева та вершину, для якої потрібно знайти наступника.

Клас, який описує бінарне дерево (та будь який вузол дерева) має вигляд:

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent
Ваша функція має мати такий вигляд:

def find_successor(tree: BinaryTree, node: BinaryTree) -> BinaryTree:
Реалізація даної задачі не вимагає написання коду вставки чи виділення елементів з бінарного дерева. У тесті ви можете створити достатню кількість елементів класу BinaryTree наступним чином:

root = BinaryTree(3)
root.left = BinaryTree(9)
root.right = BinaryTree(20)
"""

"""
Лабораторна 4 рівень 3
Черга з пріорітетом авл дерево
Реалізуйте структуру даних "черга з пріоритетами" на основі червоно-чорного дерева, в якому батьківський елемент має вищий пріоритет, ніж елемент справа, або нижчий або рівний пріоритет, ніж пріоритет його лівої дитини.

Операції, які підтримує ваша черга:

Вставка елемента з заданим значенням та пріоритетом до черги.
Видалення та повернення елемента з найвищим пріоритетом з черги.
Перегляд черги без її зміни.
Для реалізації такої черги з пріоритетами слід використати окремий клас Node, де кожен елемент буде мати два поля: значення та пріоритет. При вставці елемента до черги, його потрібно розмістити у відповідному порядку з урахуванням пріоритету.

Назва файлу реалізації - red_black_priority_queue.py
"""

"""
Лабораторна 5 рівень 3
Про шагового коня 
умови нема, бо слак замилив повідомлення 
"""

"""
Лфбораторна 6 рівень 3
Про ігровий сервер 
Iгровий сервер 88889
Код задачi: GAMSRV
Важливим фактором для багатокористувацької онлайн-гри є низька мережева затримка
вiд користувача до сервера. При цьому, пристрої в Iнтернетi спiлкуються один з
одним, використовуючи мережевi маршрути, якi проходять через низку промiжних
вузлiв-маршрутизаторiв. Кожна ланка цього маршруту має власну ненульову затримку.

Client 1

Client 2
Router 1 Router 2 SERVER Client 3 10 ms 80 ms 50 ms 20 ms
40 ms
100 ms

• Кожен вузол мережi може виконувати одну з трьох ролей: Client, Router або
Server.
• Server може бути лише один на всю мережу.
• Усi комунiкацiї двостороннi: якщо вузол A може спiлкуватися з вузлом B,
вузол B може спiлкуватися з вузлом A з такою ж затримкою.
• Якщо iснує кiлька шляхiв вiд клiєнта до сервера, клiєнт гарантовано пiде
шляхом з найменшою сумарною затримкою (навiть якщо цей шлях пролягає
через iншого клiєнта).
• Усi затримки — сталi додатнi числа.
Для прикладу вище, затримки до клiєнтiв становлять:
• Client 1: 10 + 80 + 50 = 140 ms
• Client 2: 100 + 50 = 150 ms
• Client 3: 20 ms
Максимальною затримкою в такому випадку є 150 ms. Однак, якщо ми помiняємо
ролями вузли “Router 2” i “Server”, затримки скоротяться до 90 ms, 100 ms i 70 ms
вiдповiдно, тодi максимальна затримка буде становити 100 ms.

Client 1

Client 2
Router 1 SERVER Router 2 Client 3 10 ms 80 ms 50 ms 20 ms
40 ms
100 ms

1

Ви розробляєте онлайн-гру для користувачiв зi всiєї країни, i бажаєте розмiстити
центральний iгровий сервер таким чином, щоб максимальна затримка мiж сервером
i кожним клiєнтом була мiнiмальною. В якостi сервера можна вибрати будь-який
вузол мережi, який не є клiєнтом.
Маючи iнформацiю про топологiю мережi (якi вузли з’єднанi з якими, i яка затримка
кожного з’єднання), знайдiть таке розташування сервера, яке мiнiмiзує найбiльше
значення затримки до клiєнта. Виведiть це значення затримки.
Вхiднi данi
Вхiдний файл gamsrv .in складається з M + 2 рядкiв.
• Перший рядок мiстить N i M — кiлькiсть вузлiв та з’єднань вiдповiдно.
3 ≤ N ≤ 1000, 2 ≤ M ≤ 1000
• Другий рядок мiстить перелiк цiлих чисел, роздiлених пробiлом — номери
вузлiв, якi є клiєнтами. Усi вузли в мережi нумеруються вiд 1 до N.
• Наступнi M рядкiв мiстять трiйки натуральних чисел startnode, endnode, latency
— номер початкового вузла, кiнцевого вузла та затримка для кожного з’єднання.
1 ≤ latency ≤ 109
.

Вихiднi данi
Вихiдний файл gamsrv .out повинен мiстити одне число — мiнiмальне значення найбiльшої
затримки до клiєнта (яке ми отримаємо при оптимальному розташуваннi сервера).
"""

"""
Лабораторна 7 рівень 2
Скінченні автомати 
Створити функцію на мові програмування Python, яка приймає дві стрічки: "haystack" (довільний текст) та "needle" (шукана стрічка). Програма повинна знайти індекси всіх входжень стрічки "needle" в стрічці "haystack" та повернути цей індекс, використовуючи  метод скінченних автоматів для пошуку підстрічки у стрічці
"""

"""
Лабораторна 8 рівень 2
З'єднати всі острови оптоволокном у Венеції
До вас звернулась мерія міста Венеції з незвичним проханням. Це місто складається з островів які розділені каналами. Кожен острів має свою унікальну локацію і з'єднаний з іншими островами мостами. Мерія міста хоче провести оптоволоконний інтернет на кожен з островів таким чином, щоб кожен острів був з'єднаний з кожним іншим безпосередньо, або через інші острови. Вам потрібно допомогти порахувати мінімальну довжину кабелів, які потрібно прокласти, щоб відстань між всіма островами була мінімальна.

Вхідні дані:

файл islands.csv, який містить матрицю суміжності, де елемент [i][j] вказує на відстань між островами i та j.
Вихідні дані:

Мінімальна довжина підводних кабелів, які потрібно прокласти.
При виборі алгоритму слід вважати, що кількість островів у місті становить N (1 ≤ N ≤ 100)
"""

"""
Лабораторна 9 рівень 2
Індіана Джонс В пошуках Святого Грааля Iндiана Джонс
Iндiана Джонс i останнiй прямокутний обхiд
Код задачi: IJONES
В пошуках Святого Грааля Iндiана Джонс зiткнувся з небезпечним випробуванням.
Йому потрiбно пройти крiзь прямокутний коридор, який складається з крихких плит
(пригадайте сцену з фiльму «Iндiана Джонс i останнiй хрестовий похiд»). На кожнiй
плитi написана одна лiтера:

a a a
c a b
d e f

Можна починати з будь-якої плити в найлiвiшому стовпцi. Виходом iз коридору є
верхня права та нижня права плити (для прикладу вище — a та f).
Iндiана спритний, i може переходити не лише на сусiдню плиту, а й перестрибувати
через кiлька плит. Проте, щоб не провалитися крiзь пiдлогу, вiн повинен дотримуватися
таких правил:
1. Пiсля кожного кроку Iндiана повинен опинятися правiше, нiж був перед цим.

a a a
c a b
d e f
2. Завжди можна переходити на одну плиту праворуч.
a a a
c a b
d e f

3. Крiм руху на одну плиту праворуч, можна перестрибувати, проте лише на ту
саму лiтеру. Наприклад, з лiтери a можна перестрибнути на будь-яку iншу
лiтеру a за умови, що ми цим ходом просунемося правiше.

a a a
c a b
d e f

1

Для заданого коридору, пiдрахуйте, скiльки всього iснує способiв пройти його успiшно.
Вхiднi данi
Вхiдний файл ijones .in складається з H + 1 рядкiв.
• Перший рядок мiстить два числа W i H, роздiленi пробiлом: W — ширина
коридору, H — висота коридору, 1  W, H  2000.
• Кожен з наступних H рядкiв мiстить слово довжиною W символiв, яке складається
з малих латинських лiтер вiд a до z.
Вихiднi данi
Вихiдний файл ijones .out повинен мiстити одне цiле число — кiлькiсть рiзних
шляхiв для виходу з коридору.

# Див. приклади нижче #

2

Приклад 1
ijones .in
3 3
aaa
cab
def
ijones .out
5
Пояснення: Iснує 3 варiанти обходу, якщо починати з лiтери a, i по одному варiанту,
якщо починати з лiтери c або d.
Приклад 2
ijones .in
10 1
abcdefaghi
ijones .out
2

Приклад 3
ijones .in
7 6
aaaaaaa
aaaaaaa
aaaaaaa
aaaaaaa
aaaaaaa
aaaaaaa
ijones .out
201684
"""
