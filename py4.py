import os
import subprocess


def get_all_git_objects():
    # Получаем путь к каталогу объектов
    git_objects_dir = os.path.join(".git", "objects")
    if not os.path.exists(git_objects_dir):
        print("Каталог .git/objects не найден. Убедитесь, что это git-репозиторий.")
        return []

    objects = []
    # Проходим по всем подкаталогам в .git/objects (кроме info и pack)
    for root, dirs, files in os.walk(git_objects_dir):
        dirs[:] = [d for d in dirs if d not in ("info", "pack")]
        for file in files:
            # Хэш объекта состоит из имени подкаталога и имени файла
            obj_hash = os.path.basename(root) + file
            objects.append(obj_hash)

    return objects


def cat_git_object(obj_hash):
    # Читаем содержимое объекта
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
