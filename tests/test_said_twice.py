"""said_twice.py (lesson bad-trips-2026-11-13a): the Lu & Mattson case. His DMSO text of 2026-11-13 14:15 UTC cited the
study his My Brain Feels Damaged paragraph already cited; the check names that place before the text goes in."""
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'tools' / 'humanization'))
import said_twice  # noqa: E402

BRAIN = ("But more relevant to the drug overdose issue this article deals with, DMSO calms [NMDA- and AMPA-mediated "
         "excitotoxicity](https://pubmed.ncbi.nlm.nih.gov/11421595/) that kills brain cells.")
NEW = ("In rat brain cells in a dish, DMSO at 0.5 to 1.5% quickly turned down the signals glutamate sends through its NMDA and "
       "AMPA receptors, and the calcium they let in. It also kept glutamate from killing the cells ([Lu & Mattson, 2001]"
       "(https://pubmed.ncbi.nlm.nih.gov/11421595/)). But it also appears to be neurotoxic to healthy mice neurons when they "
       "are exposed for too long ([Hanslick, et al, 2009](https://pubmed.ncbi.nlm.nih.gov/19100327/)).")


class SaidTwice(unittest.TestCase):
    def test_lu_mattson_found(self):
        art = '## Brain\n\n' + BRAIN + '\n\n## DMSO\n\n' + NEW + '\n'
        found = said_twice.places(art, NEW)
        self.assertEqual(list(found), ['https://pubmed.ncbi.nlm.nih.gov/11421595'])
        self.assertIn('excitotoxicity', found['https://pubmed.ncbi.nlm.nih.gov/11421595'][0])

    def test_nothing_when_said_once(self):
        art = '## Brain\n\n' + BRAIN + '\n'
        self.assertEqual(said_twice.places(art, BRAIN), {})


if __name__ == '__main__':
    unittest.main()
