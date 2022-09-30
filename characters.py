class character_profile:
    def __init__(self, fname, lname, age, spd, atk, dfs, money, health):
        self.fname = fname
        self.lname = lname
        self.spd = spd
        self.atk = atk
        self.dfs = dfs
        self.money = money
        self.health = health

    def get_fname(self):
        return self.fname

    def get_lname(self):
        return self.lname

    def get_age(self):
        return self.age

    def set_age(self, x):
        self.age = x

    def get_spd(self):
        return self.spd

    def set_spd(self, x):
        self.spd = x

    def get_atk(self):
        return self.atk

    def set_atk(self, x):
        self.atk = x

    def get_dfs(self):
        return self.atk

    def set_dfs(self, x):
        self.dfs = x

    def get_money(self):
        return self.money

    def set_health(self, x):
        self.health = x

    def get_health(self):
        return self.health

    def set_money(self, x):
        self.money = x

    def __str__(self):
        return f"{self.name} \n Speed: {self.spd}, Attack: {self.atk}, Defense: {self.dfs}"


class Rival:
    def __init__(self, name, health, money):
        self.name = name
        self.name = health
        self.money = money

    def damage_to_health(self, damage):
        self.health = damage - self.health

        if self.health <= 0:
            return self.money
