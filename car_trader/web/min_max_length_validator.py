from enum import Enum


# <--------  Min Max Length Validator --------->
class MinMaxLengthMixin:
    @classmethod
    def choices(cls):
        return [(x.name, x.value) for x in cls]

    @classmethod
    def min_length(cls):
        return min(len(value) for _, value in cls.choices())

    @classmethod
    def max_length(cls):
        return max(len(value) for _, value in cls.choices())


class Region(MinMaxLengthMixin, Enum):
    all_regions = "Всички области"
    blagoevgrad = "Благоевград"
    burgas = "Бургас"
    varna = "Варна"
    veliko_turnovo = "Велико Търново"
    vidin = "Видин"
    vratsa = "Враца"
    gabrovo = "Габрово"
    dobrich = "Добрич"
    dupnitsa = "Дупница"
    kardzhali = "Кърджали"
    kyustendil = "Кюстендил"
    lovech = "Ловеч"
    montana = "Монтана"
    pazardzhik = "Пазарджик"
    pernik = "Перник"
    pleven = "Плевен"
    plovdiv = "Пловдив"
    razgrad = "Разград"
    ruse = "Русе"
    silistra = "Силистра"
    sliven = "Сливен"
    smolyan = "Смолян"
    sofia = "София"
    stara_zagora = "Стара Загора"
    targovishte = "Търговище"
    haskovo = "Хасково"
    yambol = "Ямбол"


class Engine(MinMaxLengthMixin, Enum):
    engine = "Двигател"
    gasoline = "Бензинов"
    diesel = "Дизелов"
    electric = "Електрически"
    hybrid = "Хибриден"
    plug_in_hybrid = "Plug-in Хибрид"
