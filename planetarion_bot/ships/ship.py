class Ship:

    def __init__(self):
        self._armor = None
        self._armor_cost = None
        self._base_eta = None
        self._cloaked = None
        self._crystal = None
        self._damage = None
        self._damage_cost = None
        self._emp_resistance = None
        self._eonium = None
        self._guns = None
        self._initiative = None
        self._metal = None
        self._name = None
        self._race = None
        self._sclass = None
        self._t1 = None
        self._t2 = None
        self._t3 = None
        self._type = None

    @property
    def armor(self):
        return self._armor

    @armor.setter
    def armor(self, value):
        self._armor = int(value)

    @property
    def armor_cost(self):
        return self._armor_cost

    @armor_cost.setter
    def armor_cost(self, value):
        self._armor_cost = int(value)

    @property
    def base_eta(self):
        return self._base_eta

    @base_eta.setter
    def base_eta(self, value):
        self._base_eta = int(value)

    @property
    def cloaked(self):
        return self._cloaked

    @cloaked.setter
    def cloaked(self, value):
        self._cloaked = bool(value)

    @property
    def damage(self):
        return self._damage

    @damage.setter
    def damage(self, value):
        self._damage = int(value) if value != '-' else 0

    @property
    def damage_cost(self):
        return self._damage_cost

    @damage_cost.setter
    def damage_cost(self, value):
        self._damage_cost = int(value)

    @property
    def crystal(self):
        return self._crystal

    @crystal.setter
    def crystal(self, value):
        self._crystal = int(value)

    @property
    def emp_resistance(self):
        return self._emp_resistance

    @emp_resistance.setter
    def emp_resistance(self, value):
        self._emp_resistance = int(value)

    @property
    def eonium(self):
        return self._eonium

    @eonium.setter
    def eonium(self, value):
        self._eonium = int(value)

    @property
    def guns(self):
        return self._guns

    @guns.setter
    def guns(self, value):
        self._guns = int(value)

    @staticmethod
    def handle_null_value(value, fn):
        return fn(value) if value != '-' else None

    @property
    def initiative(self):
        return self._initiative

    @initiative.setter
    def initiative(self, value):
        self._initiative = int(value)

    @property
    def metal(self):
        return self._metal

    @metal.setter
    def metal(self, value):
        self._metal = int(value)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def race(self):
        return self._race

    @race.setter
    def race(self, value):
        self._race = value

    @property
    def sclass(self):
        return self._sclass

    @sclass.setter
    def sclass(self, value):
        self._sclass = value

    @property
    def t1(self):
        return self._t1

    @t1.setter
    def t1(self, value):
        self._t1 = self.handle_null_value(value, str)

    @property
    def t2(self):
        return self._t2

    @t2.setter
    def t2(self, value):
        self._t2 = self.handle_null_value(value, str)

    @property
    def t3(self):
        return self._t3

    @t3.setter
    def t3(self, value):
        self._t3 = self.handle_null_value(value, str)

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
