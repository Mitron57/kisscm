# Задание 1
### Условие

Реализовать на Jsonnet приведенный ниже пример в формате JSON. Использовать в реализации свойство программируемости и принцип DRY.

### Код

```jsonnet
local groupPrefix = 'БИВТ-';
local year = '-21';
local groupNum = std.range(1, 10);

local createGroup = function(i) groupPrefix + std.toString(i) + year;

local studentData = [
  {name: "Иванов А.В.", age: 20, groupIndex: 2},
  {name: "Петров Б.С.", age: 21, groupIndex: 3},
  {name: "Сидоров В.Д.", age: 22, groupIndex: 1},
  {name: "Кузнецов Г.И.", age: 20, groupIndex: 4}
];

{
  groups: [createGroup(i) for i in groupNum],

  students: [
    {
      age: student.age,
      group: createGroup(student.groupIndex),
      name: student.name
    } for student in studentData
  ],

  subject: "Программирование"
}

```

### Вывод

```json
{
  "groups": [
    "БИВТ-1-21",
    "БИВТ-2-21",
    "БИВТ-3-21",
    "БИВТ-4-21",
    "БИВТ-5-21",
    "БИВТ-6-21",
    "БИВТ-7-21",
    "БИВТ-8-21",
    "БИВТ-9-21",
    "БИВТ-10-21"
  ],
  "students": [
    {
      "age": 20,
      "group": "БИВТ-2-21",
      "name": "Иванов А.В."
    },
    {
      "age": 21,
      "group": "БИВТ-3-21",
      "name": "Петров Б.С."
    },
    {
      "age": 22,
      "group": "БИВТ-1-21",
      "name": "Сидоров В.Д."
    },
    {
      "age": 20,
      "group": "БИВТ-4-21",
      "name": "Кузнецов Г.И."
    }
  ],
  "subject": "Программирование"
}
```



# Задание 2
### Условие

Реализовать на Dhall приведенный ниже пример в формате JSON. Использовать в реализации свойство программируемости и принцип DRY.

### Код

```dhall
let Group = Text
let Student = { age : Natural, group : Group, name : Text }

let createGroup : Natural -> Group =
      λ(n : Natural) → "БИВТ-" ++ (Natural/show n) ++ "-21"

let groupIndices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] : List Natural

let groups = List/map Natural Group createGroup groupIndices

let createStudent : Natural -> Group -> Text -> Student =
      λ(age : Natural) → λ(group : Group) → λ(name : Text) →
        { age = age, group = group, name = name }

let studentData =
      [ { age = 20, groupIndex = 2, name = "Иванов А.В." }
      , { age = 21, groupIndex = 3, name = "Петров Б.С." }
      , { age = 22, groupIndex = 1, name = "Сидоров В.Д." }
      , { age = 20, groupIndex = 4, name = "Кузнецов Г.И." }
      ]

let students =
      List/map
        { age : Natural, groupIndex : Natural, name : Text }
        Student
        (λ(student : { age : Natural, groupIndex : Natural, name : Text }) →
          createStudent student.age (createGroup student.groupIndex) student.name
        )
        studentData

in  { groups = groups, students = students, subject = "Программирование" }
```



# Задание 3
### Условие

Язык нулей и единиц.

### Код

```
<digit> ::= 0 | 1
<string> ::= <digit> | <digit> <string>
```



# Задание 4
### Условие

Язык правильно расставленных скобок двух видов.

### Код

```
<string> ::= "(" <string>? ")" 
           | "{" <string>? "}" 
           | ""
```



# Задание 5
### Условие

Язык выражений алгебры логики.

### Код

```
<expression> ::= <term>
               | "(" <expression> <operation> <expression> ")"
               | "~" "(" <term> ")"

<term> ::= <variable>
         | "~" <variable>
         | "(" <term> <operation> <term> ")"

<variable> ::= "x" | "y" | "z" | "w"

<operation> ::= "&" | "|"
```