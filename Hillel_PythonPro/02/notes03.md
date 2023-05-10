# Notes02 •  Налаштування Python проекту у Visual Studio
1. Створити новий Python проект
2. Обрати пункт `Add to Source Control` -> `Git`, серед інших налаштувать в якості файлу `.gitignore template` обрати шаблон по замовчуванню (`Default (VisualStudio`); виконати решту налаштувань діалогу `Create a Git repository` та завершити операцію створення Git репозиторію натиснувши кнопку `Create and Push`.
3. ❗Вікрити Visual studio в режимі адміністратора (у правому верхньому куті Visual Studio повинен відображатись індикатор `ADMIN`)
4. Відкрити термінал через меню `View` -> `Terminal` (вкладка `Developer PowerShell`)
5. Перейти в корневу папку рішення, наприклад:
```
> cd P:\MyProjects\MySolution
```
6. Перевірити чи встановлено `pipenv`:
```
P:\MyProjects\MySolution> pip show pipenv
```
за відсутності встановити його:
```
P:\MyProjects\MySolution> pip install pipenv
```
7. Перебуваючи в кореневій папці рішення, за допомогою `pipenv` виконати команду `shell`:
```
P:\MyProjects\MySolution> pipenv shell
```
В результаті цього створиться папка з віртуальним середовищем, вона як правило розміщується в `C:\Users\<UserName>\.virtualenvs\<SolutionName>-<Hash>`, а також файл `Pipfile` в папці рішення.

8. У Visual Studio вибрати створене середовище в `Solution Explorer` -> `<SolutionName>` -> `<ProjectName>` -> `Python Environments` та за необхідності активувати його (в меню по ПКМ)
9. За допомогою `pipenv` встановити пакети  `black`, `flake8` та `isort` для розробників
```
P:\MyProjects\MySolution> pipenv install black --dev
```
```
P:\MyProjects\MySolution> pipenv install flake8 --dev
```
```
P:\MyProjects\MySolution> pipenv install isort --dev
```
В результаті в кореневій папці рішення повинен додатково зя'витись файл `Pipfile.lock`, що містить детальний (машинний) опис додатково встановлених пакетів


10. Після клонування рішення на іншому компьютері за необхідності встановити `pipenv` та створити віртуальне середовище, як було наведено в пунктах 5 та 6
11. Для синхронізаціх пакетів використати команду `sync` a для синхронізації пакетів розробника - `sync --dev`:
```
X:\MyProjects\MySolution> pipenv sync
```
```
X:\MyProjects\MySolution> pipenv sync --dev
```
