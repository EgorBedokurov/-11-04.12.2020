val_win = int(input('value of win - '))
val_draw = int(input('value of draw - '))
val_lose = int(input('value of lose - '))
game = {'win': val_win, 'draw': val_draw, 'loss': val_draw}
def teem_points(game):
    win = 3*game.get('win')
    draw = 2*game.get('draw')
    loss = 0
    coin_point = win + draw
    return coin_point
print('teem points - ', teem_points(game))
