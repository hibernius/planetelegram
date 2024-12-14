import prettytable


class Attack:

    def __init__(self, attacks=None):
        if attacks is None:
            attacks = []
        self.attacks = attacks

    def add(self, attack):
        self.attacks.append(attack)

    def get(self):
        return self.attacks

    def get_formatted(self):
        tatts = [(i + 1, d['targ'], d['land'], d['ship']) for i, d in enumerate(self.attacks)]
        table = prettytable.PrettyTable(['ID', 'Targ', 'Land', 'Ship'])
        table.align['ID'] = 'l'
        table.align['Targ'] = 'l'
        table.align['Land'] = 'l'
        table.align['Ship'] = 'l'

        for attack_id, targ, land, ship in tatts:
            table.add_row([attack_id, targ, land, ship])

        return table

    def remove(self, attack_id):
        del self.attacks[attack_id]
