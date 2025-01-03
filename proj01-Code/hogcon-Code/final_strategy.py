PLAYER_NAME = 'qqq'

from math import sqrt, floor
def pp(o):
    return 2*abs((o%10)-((o//10))%10) +1
def ss(s):
    if sqrt(s)==floor(sqrt(s)):
        return True
    return False

def sw(s, o, t=8, n=6):
    p = pp(o)
    ns = s + p
    if p >= t and not ss(ns):
        return 0
    elif ss(ns) and (o - s) > t:
        return 0
    else:
        return n
    
def final_strategy(score, opponent_score):
    return sw(score, opponent_score)