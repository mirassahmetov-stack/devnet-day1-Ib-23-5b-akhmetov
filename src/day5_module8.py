import os
import requests
import json
import hashlib
from pathlib import Path

# Конфигурация
TOKEN = os.getenv("WEBEX_TOKEN") # Токен берем из переменных окружения
STUDENT_TOKEN = os.getenv("STUDENT_TOKEN", "default_token")
ART_PATH = Path("artifacts/day5/webex")
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

def get_hash8(val):
    return hashlib.sha256(val.encode()).hexdigest()[:8]

def save_json(name, data):
    with open(ART_PATH / name, "w") as f:
        json.dump(data, f, indent=2)

def webex_task():
    th8 = get_hash8(STUDENT_TOKEN)
    
    # 1. Get Me
    me = requests.get("https://webexapis.com/v1/people/me", headers=HEADERS).json()
    save_json("me.json", me)
    
    # 2. List Rooms
    rooms = requests.get("https://webexapis.com/v1/rooms", headers=HEADERS).json()
    save_json("rooms_list.json", rooms)
    
    # 3. Create Room (название содержит хэш)
    room_title = f"Ib-23-5b_Capstone_{th8}"
    room_data = {"title": room_title}
    new_room = requests.post("https://webexapis.com/v1/rooms", headers=HEADERS, json=room_data).json()
    save_json("room_create.json", new_room)
    
    room_id = new_room.get("id")
    
    # 4. Post Message
    msg_data = {"roomId": room_id, "text": f"Miras Ib-23-5b, token_hash: {th8}"}
    msg = requests.post("https://webexapis.com/v1/messages", headers=HEADERS, json=msg_data).json()
    save_json("message_post.json", msg)
    
    # 5. List Messages
    msgs = requests.get(f"https://webexapis.com/v1/messages?roomId={room_id}", headers=HEADERS).json()
    save_json("messages_list.json", msgs)
    
    print(f"Webex артефакты созданы в {ART_PATH}")

if __name__ == "__main__":
    if not TOKEN:
        print("ОШИБКА: Установи переменную WEBEX_TOKEN!")
    else:
        webex_task()