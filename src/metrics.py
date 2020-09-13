import numpy as np


def hit_rate_at_k(recommended_list, bought_list, k=5):
    flags = np.isin(bought_list, recommended_list[:5])

    hit_rate = (flags.sum() > 0) * 1

    return hit_rate


def money_precision_at_k(recommended_list, bought_list, prices_recommended, k=5):

    prices = np.asarray(prices_recommended[:len(bought_list)])
    flags = np.isin(bought_list, recommended_list[:k])

    precision = np.sum(prices[flags]) / np.sum(prices)
    return precision


def recall_at_k(recommended_list, bought_list, k=5):
    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list[:k])

    flags = np.isin(bought_list, recommended_list)

    recall = flags.sum() / len(bought_list)

    return recall


def money_recall_at_k(recommended_list, bought_list, prices_recommended, prices_bought, k=5):
    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list[:k])

    prices_recommended = np.asarray(prices_recommended[:k])
    prices_bought = np.asarray(prices_bought)
    flags = np.isin(bought_list, recommended_list[:k])

    recall = np.sum(prices_recommended[flags]) / np.sum(prices_bought)

    return recall


def precision_at_k(recommended_list, bought_list, k=5):
    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list)

    bought_list = bought_list  # Тут нет [:k] !!
    recommended_list = recommended_list[:k]

    flags = np.isin(bought_list, recommended_list)

    precision = flags.sum() / len(recommended_list)

    return precision