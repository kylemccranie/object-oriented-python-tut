class Math:

    @staticmethod##No access to instances, they just do something
    def add5(x):
        return x + 5

print(Math.add5(5))
