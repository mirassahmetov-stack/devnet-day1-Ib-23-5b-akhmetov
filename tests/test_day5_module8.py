import pytest
import json
import os
import hashlib

def test_summary_exists():
    assert os.path.exists("artifacts/day5/summary.json")

def test_token_hash_logic():
    with open("artifacts/day5/summary.json", "r") as f:
        summary = json.load(f)
    token = os.getenv("STUDENT_TOKEN", "default_token")
    expected_hash = hashlib.sha256(token.encode()).hexdigest()[:8]
    assert summary["student"]["token_hash8"] == expected_hash

def test_pt_version_check():
    # Проверка версии в JSON ответах
    for file in ["network_devices.json", "hosts.json"]:
        path = f"artifacts/day5/pt/{file}"
        if os.path.exists(path):
            with open(path, "r") as f:
                data = json.load(f)
                assert data.get("version") == "1.0"