import math


class Efficiency:

    def __init__(self, ship_factory, stats):
        self.ships = ship_factory.build_ships(stats)

    def calculate(self, ship_search, ship_count):

        ship = self.get_ship(ship_search)

        if ship is None:
            return f"Ship '{ship_search}' not found"

        damage = ship.damage * ship_count
        shots = ship.guns * ship_count
        kill = self.get_attack_verb(ship)

        if ship.t1 == 'Roids':
            killed = math.floor(damage / 50)
            return f'Ship will capture {killed} roids'

        if ship.t1 == 'Structure':
            killed = math.floor(damage / 500)
            return f'Ship will destroy {killed} structures'

        kill_result = f'{ship_count} {ship.name} will {kill}:'

        for tier, target_class in enumerate(self.get_target_classes(ship)):
            kill_result += f'\n\n{target_class}'
            target_ships = self.get_target_ships(target_class)
            for target_ship in target_ships:
                killed = self.get_target_ships_killed(target_ship, damage, shots, tier)
                kill_result += f'\n{killed} {target_ship.name}'

        return kill_result

    def find_ship(self, search):
        return [s for s in self.ships if s.name.lower() == search.lower()]

    @staticmethod
    def get_actual_damage(damage, target_ship):
        return damage / target_ship.armor

    @staticmethod
    def get_attack_verb(ship):
        match ship.type:
            case 'EMP':
                kill = 'hug'
            case 'Steal':
                kill = 'steal'
            case _:
                kill = 'kill'
        if ship.damage <= 0:
            kill = 'hug'

        return kill

    @staticmethod
    def get_emp_damage(shots, target_ship):
        return shots * (100 - target_ship.emp_resistance) / 100

    def get_ship(self, ship_search):
        ship_result = self.find_ship(ship_search)
        return ship_result[0] if ship_result else None

    @staticmethod
    def get_ship_value(ship, count):
        return int(((ship.metal + ship.crystal + ship.eonium) * count) / 100)

    def get_target_classes(self, ship):
        return [t for t in self.get_tiers(ship) if t]

    def get_target_ships(self, target_class):
        return [s for s in self.ships if s.sclass == target_class]

    def get_target_ships_killed(self, target_ship, damage, shots, tier):
        damage_multiplier = [1, 0.7, 0.5]
        killed = self.get_actual_damage(damage, target_ship) if damage > 0 else self.get_emp_damage(shots, target_ship)
        return int(killed * damage_multiplier[tier])

    @staticmethod
    def get_target_ships_value(target_ship, count):
        return int(((target_ship.metal + target_ship.crystal + target_ship.eonium) * count) / 100)

    @staticmethod
    def get_tiers(ship):
        return [ship.t1, ship.t2, ship.t3]
