import json
import os
import hashlib

def get_hash8(token):
    return hashlib.sha256(token.encode()).hexdigest()[:8]

def build_summary():
    token = os.getenv("STUDENT_TOKEN", "default_token")
    hash8 = get_hash8(token)
    
    summary = {
        "schema_version": "5.0",
        "student": {
            "name": "Miras",
            "group": "IS31",
            "token_hash8": hash8
        },
        "yang": {"ok": False, "evidence_sha": ""},
        "webex": {"ok": False, "room_title_contains_hash8": False},
        "pt": {"ok": False, "empty_ticket_seen": False},
        "validation_passed": False
    }

    # Проверка YANG
    yang_path = "artifacts/day5/yang/pyang_tree.txt"
    if os.path.exists(yang_path):
        with open(yang_path, "r") as f:
            if "+--rw interfaces" in f.read():
                summary["yang"]["ok"] = True

    # Проверка Webex
    webex_path = "artifacts/day5/webex/room_create.json"
    if os.path.exists(webex_path):
        with open(webex_path, "r") as f:
            data = json.load(f)
            if hash8 in data.get("title", ""):
                summary["webex"]["ok"] = True
                summary["webex"]["room_title_contains_hash8"] = True

    # Проверка Packet Tracer
    pt_check = "artifacts/day5/pt/external_access_check.json"
    if os.path.exists(pt_check):
        with open(pt_check, "r") as f:
            if "empty ticket" in f.read():
                summary["pt"]["empty_ticket_seen"] = True
                summary["pt"]["ok"] = True

    with open("artifacts/day5/summary.json", "w") as f:
        json.dump(summary, f, indent=4)
    print("Summary Day 5 built successfully.")

if __name__ == "__main__":
    build_summary()