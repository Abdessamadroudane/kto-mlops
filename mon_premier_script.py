import unittest

def count_names_with_more_than_seven_letters(noms):
    """
    Compte les noms de plus de sept lettres.

    Args:
        noms (list of str): Une liste de noms.

    Returns:
        int: Le nombre de noms de plus de sept lettres.
    """
    compte = 0
    for nom in noms:
        if len(nom) > 7:
            compte += 1
            print("Nom avec plus de sept lettres:", nom)
        else:
            print("Nom avec sept lettres ou moins:", nom)
    return compte

class TestNamesMethod(unittest.TestCase):
     def test_names(self):
        noms = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
        plus_de_sept = count_names_with_more_than_seven_letters(noms)
        self.assertEqual(plus_de_sept, 4)

if __name__ == '__main__':
    unittest.main()
