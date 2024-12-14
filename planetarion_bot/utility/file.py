import xmltodict


class File:

    @staticmethod
    def get_stats(path):
        f = open(path, 'r')
        doc = xmltodict.parse(f.read())
        stats = doc['stats']['ship']
        f.close()
        return stats
