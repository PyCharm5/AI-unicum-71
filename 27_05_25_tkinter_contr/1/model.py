class Model:
    @staticmethod
    def get_arrow_direction(key):
        arrows = {
            38: "Вверх",
            40: "Вниз",
            37: "Влево",
            39: "Вправо"
        }

        return arrows.get(key)