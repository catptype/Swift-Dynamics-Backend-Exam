## Question
![](/assets/q_idempotency.png)
## Response Section

### ความหมายของ Idempotency ในบริบท RESTful API

Idempotency คือคุณสมบัติของ Request ที่ไม่ว่า Client จะส่งซ้ำกี่ครั้งก็ตาม สถานะของข้อมูลบนฝั่ง Server จะยังคงเท่ากับการส่ง Request สำเร็จเพียงครั้งเดียวเสมอ

ซึ่งใน RESTful API จะแบ่ง HTTP Methods ตามคุณสมบัติดังนี้:
* **Safe Methods (GET, HEAD, OPTIONS, TRACE):** เป็น Methods ที่เน้นการอ่านข้อมูลอย่างเดียว ไม่มีการเปลี่ยนแปลงสถานะบน Server
* **Idempotent Methods (PUT, DELETE):** เป็น Methods ที่มีการแก้ไขข้อมูล แต่ถูกออกแบบมาให้ผลลัพธ์สุดท้ายที่ Server คงที่เสมอ
    * PUT: กำหนดสถานะข้อมูลให้เป็นไปตามที่ระบุ (ไม่ว่าจะส่งซ้ำกี่ครั้ง ค่าสุดท้ายก็ยังคงเดิม)
    * DELETE: กำหนดให้ข้อมูลนั้นถูกลบออก (ไม่ว่าจะส่งซ้ำกี่ครั้ง ผลลัพธ์คือข้อมูลนั้นถูกลบไปแล้วเสมอ)
* **Non-Idempotent Method (POST):** โดยปกติ POST จะไม่นับว่าเป็น Idempotent เพราะหากส่งซ้ำจะทำให้เกิดการสร้างทรัพยากรใหม่ทุกครั้ง แต่ Methods นี้สามารถทำให้เป็น Idempotent ได้โดยที่ Client ต้องแนบ Idempotency Key มาใน Header เพื่อให้ Server ตรวจสอบว่า "Request นี้เคยถูกประมวลผลไปแล้วหรือยัง" เพื่อให้คงสภาพผลลัพธ์ที่เหมือนการส่งเพียงครั้งเดียวตามนิยามของ Idempotent

### ตัวอย่าง Implement Code Python ด้วย Framework FastAPI
```Python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

# Simulated database
db: Dict[int, dict] = {1: {"name": "Item 1", "price": 100}}

# Set to track processed IDs for POST idempotency
processed_ids = set()

class Item(BaseModel):
    name: str
    price: int

class CreateRequest(BaseModel):
    request_id: str # Used as idempotency key
    item: Item

# 1. GET (Safe/Idempotent) - Fetch data
@app.get("/items/{item_id}")
async def get_item(item_id: int):
    if item_id not in db:
        raise HTTPException(status_code=404, detail={"error": "Item not found"})
    return {"status": "success", "data": db[item_id]}

# 2. POST (Non-Idempotent -> Idempotent via request_id) - Create data
@app.post("/items")
async def create_item(payload: CreateRequest):

    try:
        request_id = int(payload.request_id)
    except:
        raise HTTPException(status_code=400, detail="request_id must be an integer")

    if request_id in processed_ids: # Return existing if request_id already processed
        return {"status": "already_processed", "data": db.get(payload.id)}
    
    if request_id in db:
        return {"status": "already_existed", "data": db.get(payload.id)}

    db[request_id] = payload.item.dict()
    processed_ids.add(request_id) # Store request_id to prevent duplicates
    return {"status": "created", "data": db[request_id]}

# 3. PUT (Idempotent) - Replace data
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    db[item_id] = item.dict() # Always overwrites with the same content
    return {"status": "updated", "data": db[item_id]}

# 4. DELETE (Idempotent) - Remove data
@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    if item_id in db:
        del db[item_id] # Deletes if exists, resulting in the same "gone" state
        return {"status": "deleted"}
    return {"status": "already_gone"}
```