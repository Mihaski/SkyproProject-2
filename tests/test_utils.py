import json

from src.utils import load_data_from_json


def test_load_data_from_json_file_not_found():
    result = load_data_from_json("not_existing.json")

    assert result == []


def test_load_data_from_json_multiple_categories(tmp_path, monkeypatch):
    data = [
        {"name": "Смартфоны", "description": "Телефоны", "products": []},
        {"name": "Телевизоры", "description": "Телевизоры", "products": []},
    ]

    data_dir = tmp_path / "data"
    data_dir.mkdir()

    (data_dir / "products.json").write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")

    monkeypatch.chdir(tmp_path)

    result = load_data_from_json()

    assert len(result) == 2
    assert result[0].name == "Смартфоны"
    assert result[1].name == "Телевизоры"


def test_load_data_from_json_empty(tmp_path):
    json_file = tmp_path / "products.json"
    json_file.write_text("[]", encoding="utf-8")

    result = load_data_from_json(str(json_file))

    assert result == []
