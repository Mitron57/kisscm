## Задание 1
- Вывод информации о пакете
```bash
pip show matplotlib
```
### Результат
![Результат задания 1](images/p2_ex1.png)

- Установка из репозитория
```bash
git clone https://github.com/matplotlib/matplotlib.git
cd matplotlib
pip install .
```
## Задание 2
```bash
npm show express
```
### Результат
![Результат задания 2](images/p2_ex2.png)

- Установка из репозитория
```bash
git clone https://github.com/expressjs/express.git
cd express
npm install
```
## Задание 3
`matplot.dot:`
```graphviz
digraph "matplotlib Dependencies" {
    A [label="matplotlib"];
    B [label="numpy"];
    C [label="pillow"];
    D [label="cycler"];
    E [label="pyparsing"];
    F [label="kiwisolver"];
    G [label="python-dateutil"];
    H [label="contourpy"];
    I [label="fonttools"];
    J [label="packaging"];

    A -> B;
    A -> C;
    A -> D;
    A -> E;
    A -> F;
    A -> G;
    A -> H;
    A -> I;
    A -> J;
}
```
 - Рендер изображения
```bash
dot -Tpng matplot.dot -o matplot.png
```
### Результат
![Результат задания 3.1](images/matplot.png)

`express.dot`

```graphviz
digraph "express Full Dependencies" {
    A [label="express"];
    B [label="accepts"];
    C [label="array-flatten"];
    D [label="body-parser"];
    E [label="content-disposition"];
    F [label="cookie"];
    G [label="debug"];
    H [label="depd"];
    I [label="encodeurl"];
    J [label="escape-html"];
    K [label="etag"];
    L [label="finalhandler"];
    M [label="fresh"];
    N [label="merge-descriptors"];
    O [label="methods"];
    P [label="on-finished"];
    Q [label="parseurl"];
    R [label="path-to-regexp"];
    S [label="proxy-addr"];
    T [label="qs"];
    U [label="range-parser"];
    V [label="safe-buffer"];
    W [label="send"];
    X [label="serve-static"];
    Y [label="setprototypeof"];
    Z [label="statuses"];
    AA [label="type-is"];
    AB [label="utils-merge"];
    AC [label="vary"];

    # express dependencies
    A -> B;
    A -> C;
    A -> D;
    A -> E;
    A -> F;
    A -> G;

    # accepts dependencies
    B -> H;
    B -> I;
    B -> J;
    B -> K;

    # body-parser dependencies
    D -> L;
    D -> M;
    D -> N;
    D -> O;
    D -> P;
    D -> Q;

    # finalhandler dependencies
    L -> P;
    L -> R;
    L -> S;
    L -> Z;

    # proxy-addr dependencies
    S -> T;
    S -> U;
    S -> V;

    # send dependencies
    W -> K;
    W -> L;
    W -> X;
    W -> Y;
    W -> AB;
    W -> AC;

    # serve-static dependencies
    X -> L;
}
```

- Рендер изображения
```bash
dot -Tpng express.dot -o express.png
```
### Результат
![Результат задания 3.2](images/express.png)

## Задание 4
```minizinc
include "globals.mzn";

array[1..6] of var 0..9: digits;
constraint all_different(digits);

var int: sum_first = sum(digits[1..3]);
var int: sum_last = sum(digits[4..6]);

constraint sum_first = sum_last;
solve minimize sum_first;
```
### Результат
![Результат задания 4](images/p2_ex4.png)

## Задание 5
```minizinc
set of int: MenuVersion = {100, 110, 120, 130, 150};
set of int: DropdownVersion = {230, 220, 210, 200, 180};
set of int: IconsVersion = {100, 200};

var MenuVersion: menu;
var DropdownVersion: dropdown;
var IconsVersion: icons;

constraint if menu >= 110 then dropdown >= 200 else dropdown = 180 endif;

constraint if dropdown <= 200 /\ dropdown > 180 then icons = 200 else icons = 100 endif;

solve satisfy;
```
### Результат
![Результат задания 5](images/p2_ex5.png)

## Задание 6

```minizinc
int: root = 100;
var 100..300: foo;
var 100..300: target;
var 100..300: left;
var 100..300: right;
var 100..300: shared;


constraint if root = 100 then foo >= 100 /\ foo < 200 /\ target >= 200 /\ target < 300 endif;
constraint if foo = 110 then left >= 100 /\ left < 200 /\ right >= 100 /\ right < 200 endif;
constraint if left = 100 then shared >= 100 endif;
constraint if right = 100 then shared < 200 endif;
constraint if shared = 100 then target >= 100 /\ target < 200 endif;

solve satisfy;
```
### Результат
![Результат задания 6](images/p2_ex6.png)

## Задание 7

```python
import re
from collections import defaultdict

def parse_package_file(file_path):
    package_data = defaultdict(dict)

    with open(file_path, 'r') as file:
        for line in file:
            if ' - ' not in line:
                continue 

            package_meta, dep_list = line.split(" - ")
            pkg_name, pkg_version = package_meta.split()

            dep_dict = {}
            if dep_list.strip():
                dep_items = dep_list.split()
                for dep_item in dep_items:
                    name, version = extract_dep_info(dep_item)
                    if name:
                        dep_dict[name] = version

            package_data[pkg_name] = {
                "version": pkg_version,
                "dependencies": dep_dict
            }

    return package_data

def extract_dep_info(dep_entry):
    pattern = re.match(r'([a-zA-Z0-9_]+)\s*([^\s]*)', dep_entry)
    if pattern:
        return pattern.group(1).strip(), pattern.group(2).strip()
    return None, None

def attempt_dependency_resolution(packages):
    version_store = {}
    resolved = {}

    def resolve_pkg_chain(pkg_name):
        if pkg_name in resolved:
            return True

        pkg_details = packages.get(pkg_name)
        if not pkg_details:
            return False

        pkg_deps = pkg_details["dependencies"]

        for dep_name, dep_version in pkg_deps.items():
            if not handle_dependency(dep_name, dep_version, version_store):
                return False

        resolved[pkg_name] = pkg_details["version"]
        return True

    def handle_dependency(dep_name, version_constraint, version_store):
        if dep_name in version_store:
            if not is_version_compatible(version_store[dep_name], version_constraint):
                return False
        else:
            version_store[dep_name] = version_constraint
            if not resolve_pkg_chain(dep_name):
                return False
        return True

    for pkg in packages:
        if not resolve_pkg_chain(pkg):
            print(f"Error: Could not resolve dependencies for {pkg}")
            return None

    return resolved

def is_version_compatible(installed_version, constraint):
    required_version = constraint.lstrip('^>=')
    if constraint.startswith('>='):
        return installed_version >= required_version
    elif constraint.startswith('^'):
        return installed_version >= required_version
    elif constraint.startswith('<'):
        return installed_version < required_version
    else:
        return installed_version == required_version

file_path = 'dependencies.txt'
package_info = parse_package_file(file_path)
final_resolution = attempt_dependency_resolution(package_info)

if final_resolution:
    print("Dependency resolution successful!")
    for pkg, ver in final_resolution.items():
        print(f"{pkg}: {ver}")
else:
    print("Dependency resolution failed.")
```

### Тестовый файл

```txt
root 1.0.0 - foo ^1.0.0 target ^2.0.0
foo 1.1.0 - left ^1.0.0 right ^1.0.0
foo 1.0.0 -
left 1.0.0 - shared >=1.0.0
right 1.0.0 - shared <2.0.0
shared 2.0.0 -
shared 1.0.0 - target ^1.0.0
target 2.0.0 - 
target 1.0.0 -
```

### Результат
![Результат задания 7](images/p2_ex7.png)
