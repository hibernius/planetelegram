from planetarion_bot.ships.ship import Ship


class Factory:

    @staticmethod
    def build_ship(s) -> Ship:

        ship = Ship()

        ship.armor = s['armor']
        ship.armor_cost = s['armorcost']
        ship.base_eta = s['baseeta']
        ship.cloaked = s['cloaked']
        ship.crystal = s['crystal']
        ship.damage = s['damage']
        ship.damage_cost = s['damagecost']
        ship.emp_resistance = s['empres']
        ship.eonium = s['eonium']
        ship.guns = s['guns']
        ship.initiative = s['initiative']
        ship.metal = s['metal']
        ship.name = s['name']
        ship.race = s['race']
        ship.sclass = s['class']
        ship.t1 = s['target1']
        ship.t2 = s['target2']
        ship.t3 = s['target3']
        ship.type = s['type']

        return ship

    def build_ships(self, data):
        ships = []
        for s in data:
            ships.append(self.build_ship(s))

        return ships
