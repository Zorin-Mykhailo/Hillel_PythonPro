# [Заняття 01 • Introduction. Python basics](https://lms.ithillel.ua/groups/63c0179f2482232c29371552/lessons/63c017a02482232c29371569) 

[Video](https://lms.ithillel.ua/groups/63c0179f2482232c29371552/lessons/63c017a02482232c29371569)

[Discord](https://discord.gg/5DUAf6nKUb)

Windows Subsystem for Linux
* [Oficcial Microsoft WSL](https://learn.microsoft.com/en-us/windows/wsl/install)
* [VSCode WSL plugin](https://code.visualstudio.com/learn/develop-cloud/wsl)

VSCode
* [VSCode docs](https://code.visualstudio.com/docs/setup/windows)
* [Getting Started with Python](https://www.youtube.com/watch?v=E9U-EBG8jVk)

MRO
* [Python docs](https://www.python.org/download/releases/2.3/mro/)

LEGB
* [Python Global, Local and Nonlocal variables](https://www.programiz.com/python-programming/global-local-nonlocal-variables)

---

# [Homework 01 • Jupiter notebook installation](https://lms.ithillel.ua/groups/63c0179f2482232c29371552/homeworks/6425df7b45ae600ebe252c1e)

- Installation of Jupyter Notebook with pip
```python
# It is optional. Do it for practice if you need it
pip install notebook
```
- Configure your workspace for the coding
- Read all materials

# [Заняття 02 • Git. Python code quality. Deps management. CI/CD](https://lms.ithillel.ua/groups/63c0179f2482232c29371552/lessons/63c017a02482232c2937156a)
[GitHub репозиторій Дмитра](https://github.com/parfeniukink/hillel_04_2022)

Setup GitHub Actions
* [Setup Python](https://github.com/actions/setup-python)
* [Automating builds and tests](https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-nodejs-or-python?langId=py)

Linters
* [Flake8: Your Tool For Style Guide Enforcement](https://flake8.pycqa.org/en/latest/)

Formatters

* [Python code formatters](https://deepsource.io/blog/python-code-formatters/)
* [black](https://github.com/psf/black)
* [isort](https://github.com/PyCQA/isort)


Dependency managers
* [A Review: Pipenv vs. Poetry vs. PDM](https://dev.to/frostming/a-review-pipenv-vs-poetry-vs-pdm-39b4#:~:text=Pipenv%20uses%20a%20very%20different,with%20the%20lock%20file%20existing.)

---
## Налаштування Python проекту у Visual Studio
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
9. За допомогою `pipenv` для встановити (для розробників) пакети `black`, `flake8` та `isort`
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




# [Homework 02 • Setup code quality tools. Dependency management. CI/CD](https://lms.ithillel.ua/groups/63c0179f2482232c29371552/homeworks/642b22a18177e16a56b0c6a4)
- [ ] GitHub Actions is integrated into the project
- [ ] The link for the successful job is sent as a homework

[Building and testing Python](https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python)


# [Заняття 03 • Iterators and Generators. Code debugging](https://lms.ithillel.ua/groups/63c0179f2482232c29371552/lessons/63c017a02482232c2937156b)

