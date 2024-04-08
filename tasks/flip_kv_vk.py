from typing import TypeVar

__all__ = (
    "flip_kv_vk",
    "flip_kv_vk_safe",
)


KT = TypeVar("KT")
KV = TypeVar("KV")


def flip_kv_vk(d: dict[KT, KV]) -> dict[KV, KT]:
    """Формирует словарь, в котором в качестве ключей - значения
    переданного словаря, а в качестве значений - ключи.

    Example:
        >> flip_kv_vk({'tokyo': 'Токио', 'moscow': 'Москва'})
        {
            'Токио': 'tokyo',
            'Москва': 'moscow',
        }
    """
    resultDic = {}
    for key, value in d.items():
        resultDic[value] = key
    return resultDic


def flip_kv_vk_safe(d: dict[KT, KV]) -> dict[KV, list[KT]]:
    """Формирует словарь, в котором в качестве ключей - значения
    переданного словаря, а в качестве значений - список ключей,
    конфликтующих значений.

    Example:
        >> flip_kv_vk({'Санкт-Петербург': '+3', 'Москва': '+3'})
        {
            '+3': ['Москва', 'Санкт-Петербург'],
        }
    """
    resultDic = {}
    for key, value in d.items():
        if resultDic.__contains__(value):
            resultDic[value].append(key)
        else:
            resultDic[value] = [key]
    return resultDic
