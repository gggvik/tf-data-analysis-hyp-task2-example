import pandas as pd
import numpy as np


chat_id = 250483508 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    mp_crit = 0.04
    t, p_value = ttest_ind(x, y)
    return (p_value < imp_crit)
