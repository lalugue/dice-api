from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from random import randrange

app = FastAPI(docs_url="/docs")

valid_dice_values = ["d4", "d6", "d8", "d10", "d12", "d20"]


def generate_dice_value(dice):
    if dice not in valid_dice_values:
        return "invalid"
    sides = int(dice[1:])
    return randrange(1, sides + 1)


@app.get("/")
def default_dice():
    return {
        "dice_set": [{"id": 0, "dice": "d6", "value": generate_dice_value("d6")}],
        "links": [
            {
                "name": "dice",
                "href": "/dice",
                "query_params": ["dice"],
                "valid_values": valid_dice_values,
                "example": "/dice/?dice=d4,d6,d8",
                "type": "GET",
            },
            {"name": "documentation", "href": "/docs", "type": "GET"},
        ],
    }


@app.get("/dice/")
def dice(dice=None):
    if not dice:
        return RedirectResponse("/")
    dice = dice.split(",")
    dice_set = []
    for idx, d in enumerate(dice):
        value = generate_dice_value(d)
        if value == "invalid":
            raise HTTPException(status_code=422, detail="Invalid dice detected: %s" % d)
        dice_set.append({"id": idx, "dice": d, "value": value})
    return {"dice_set": dice_set}
