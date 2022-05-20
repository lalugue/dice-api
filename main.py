from fastapi import FastAPI
from random import randrange

app = FastAPI()

valid_dice_values = ['d4','d6','d8','d10','d12','d20']

def generate_dice_value(dice):
    if dice not in valid_dice_values:
        return "invalid"
    sides = int(dice[1:])
    return randrange(1,sides+1)

@app.get("/")
def default_dice():
    return {'id':0,'dice':'d6', 'value': generate_dice_value('d6'), 'links': [
        {
            'name': 'dice',
            'link': '/dice',
            'params': ['dice'],
            'valid_values': valid_dice_values,
            'example': '/dice?dice=d4,d6,d8'
        }
    ]}


@app.get("/dice/")
@app.get("/dice/{dice}")
def dice(dice=None):   
    if not dice:
        return default_dice()  
    dice = dice.split(',')   
    dice_set=[]
    for idx,d in enumerate(dice):
        value = generate_dice_value(d)
        if value == 'invalid':
            return {'error': 'Invalid dice detected: %s' % d}
        dice_set.append({'id':idx, 'dice': d, 'value': value})
    return {'dice_set': dice_set}
    
