import os
import csv
import json

def get_keypoints_for_image(current_path, image_file):
    json_path1 = r"D:\university\ProjectWorkshop\SBER Reindeintification of newts\newts_identification\DeepLabCut\instances.json"
    json_path2 = r"D:\university\ProjectWorkshop\SBER Reindeintification of newts\newts_identification\DeepLabCut\instances1.json"

    for json_path in [json_path1, json_path2]:
        with open(json_path, mode="r", encoding="utf-8") as json_file:
            data = json.load(json_file)

        # Находим image_id для файла image_file
        image_id = None
        for image in data.get("images", []):
            if os.path.basename(image.get("file_name", "")) == image_file:
                image_id = image.get("id")
                break

        if image_id is None:
            continue

        # Находим аннотацию с данным image_id
        annotation = None
        for ann in data.get("annotations", []):
            if ann.get("image_id") == image_id:
                annotation = ann
                break

        if annotation is None:
            continue

        keypoints = annotation.get("keypoints", [])
        if len(keypoints) % 3 != 0:
            continue

        # Извлекаем только координаты x и y
        coords = []
        for i in range(0, len(keypoints), 3):
            coords.append(str(keypoints[i]) + ".00")     # x
            coords.append(str(keypoints[i + 1]) + ".00")   # y
        return coords

    print("Не удалось найти координаты для изображения:", image_file)
    return None

def create_csv_in_subfolders(root_dir):
    for current_path, subdirs, _ in os.walk(root_dir):
        # Пропускаем корневую папку, если нужно создавать csv только в подпапках
        if current_path == root_dir:
            continue

        csv_file_name = "CollectedData_msrbl.csv"
        csv_path = os.path.join(current_path, csv_file_name)

        # Собираем строки CSV в список для проверки согласованности количества колонок
        row1 = [
            "scorer", "", "",
            "msrbl", "msrbl", "msrbl", "msrbl", 
            "msrbl", "msrbl", "msrbl", "msrbl", 
            "msrbl", "msrbl", "msrbl", "msrbl", 
            "msrbl", "msrbl", "msrbl", "msrbl", 
            "msrbl", "msrbl", "msrbl", "msrbl", 
            "msrbl", "msrbl", "msrbl", "msrbl", 
            "msrbl", "msrbl", "msrbl", "msrbl", 
            "msrbl", "msrbl", "msrbl", "msrbl", 
            "msrbl", "msrbl", "msrbl", "msrbl", 
            "msrbl", "msrbl", "msrbl", "msrbl", 
            "msrbl", "msrbl"
        ]
        row2 = [
            "bodyparts", "", "",
            "bodypart1", "bodypart1", "bodypart2", "bodypart2",
            "bodypart3", "bodypart3", "bodypart4", "bodypart4",
            "bodypart5", "bodypart5", "bodypart6", "bodypart6",
            "bodypart7", "bodypart7", "bodypart8", "bodypart8",
            "bodypart9", "bodypart9", "bodypart10", "bodypart10",
            "bodypart11", "bodypart11", "bodypart12", "bodypart12",
            "bodypart13", "bodypart13", "bodypart14", "bodypart14",
            "bodypart15", "bodypart15", "bodypart16", "bodypart16",
            "bodypart17", "bodypart17", "bodypart18", "bodypart18",
            "bodypart19", "bodypart19", "bodypart20", "bodypart20",
            "bodypart21", "bodypart21"
        ]
        row3 = [
            "coords", "", "",
            "x", "y", "x", "y", "x", "y", "x", "y",
            "x", "y", "x", "y", "x", "y", "x", "y",
            "x", "y", "x", "y", "x", "y", "x", "y",
            "x", "y", "x", "y", "x", "y", "x", "y",
            "x", "y", "x", "y", "x", "y", "x", "y",
            "x", "y"
        ]
        # Определяем имя файла изображения и получаем координаты
        folder_name = os.path.basename(current_path)
        image_file = folder_name + ".jpg"
        coords = get_keypoints_for_image(current_path, image_file)
        if coords is None:
            coords = [""] * 42  # 21 пара: x и y
        row4 = ["labeled-data", folder_name, "img0.png"] + coords

        # Проверяем, что количество колонок во всех строках совпадает
        expected = len(row1)
        rows = [row1, row2, row3, row4]
        for idx, row in enumerate(rows, start=1):
            if len(row) != expected:
                print("Несоответствие количества колонок в файле '{}': строка {} имеет {} столбцов, ожидается {}".format(csv_path, idx, len(row), expected))

        # Записываем строки в csv файл
        with open(csv_path, mode="w", newline="", encoding="utf-8") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(row1)
            writer.writerow(row2)
            writer.writerow(row3)
            writer.writerow(row4)

if __name__ == '__main__':
    root_directory = r"D:\university\ProjectWorkshop\SBER Reindeintification of newts\newts_identification\DeepLabCut\Tritons ReID-msrbl-2025-04-14\labeled-data"
    create_csv_in_subfolders(root_directory)