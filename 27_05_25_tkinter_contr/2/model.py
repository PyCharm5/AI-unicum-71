class Model:
    @staticmethod
    def add_numbers(nums):
        try:
            return sum(map(float, nums.split("+")))
        except ValueError:
            return "Ошибка в вычислении"