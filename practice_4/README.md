# Задание 1
![Результат выполнения задания 1](images/p4_ex1.png)

# Задание 2
![Результат выполнения задания 2](images/p4_ex2.png)

# Задание 3
![Результат выполнения задания 3](images/p4_ex3_1.png)
![Результат выполнения задания 3](images/p4_ex3_2.png)
![Результат выполнения задания 3](images/p4_ex3_3.png)

# Задание 4
```python
import os
import subprocess


def get_all_git_objects():
    git_objects_dir = os.path.join(".git", "objects")
    if not os.path.exists(git_objects_dir):
        print("Каталог .git/objects не найден. Убедитесь, что это git-репозиторий.")
        return []

    objects = []
    for root, dirs, files in os.walk(git_objects_dir):
        dirs[:] = [d for d in dirs if d not in ("info", "pack")]
        for file in files:
            obj_hash = os.path.basename(root) + file
            objects.append(obj_hash)

    return objects


def cat_git_object(obj_hash):
    result = subprocess.run(
        ["git", "cat-file", "-p", obj_hash],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    if result.returncode == 0:
        return result.stdout.strip()
    else:
        return f"Ошибка при чтении объекта {obj_hash}: {result.stderr.strip()}"


def main():
    objects = get_all_git_objects()
    if not objects:
        print("Нет объектов в репозитории.")
        return

    print(f"Найдено {len(objects)} объектов.")
    for obj_hash in objects:
        print(f"\n--- Содержимое объекта {obj_hash} ---")
        print(cat_git_object(obj_hash))


if __name__ == "__main__":
    main()
```
# Выполнение

![Результат выполнения задания 3](images/p4_ex4.png)
