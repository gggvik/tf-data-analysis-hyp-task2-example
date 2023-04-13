import pandas as pd
import numpy as np

from scipy.stats import mannwhitneyu

chat_id = 250483508 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    imp_crit = 0.04
    t, p_value = mannwhitneyu(x, y)
    return (p_value < imp_crit)
