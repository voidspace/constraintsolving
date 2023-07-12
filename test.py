from main import find_out_mr_wrong
import unittest

sample_test_cases = [
    #  conversation                                   Mr. Wrong

    (["John:I'm in 1st position.",
      "Peter:I'm in 2nd position.",
      "Tom:I'm in 1st position.",
      'Peter:The man behind me is Tom.'], 'Tom'),

    (["John:I'm in 1st position.",
      "Peter:I'm in 2nd position.",
      "Tom:I'm in 1st position.",
      'Peter:The man in front of me is Tom.'], 'John'),

    (["John:I'm in 1st position.",
      'Peter:There is 1 people in front of me.',
      'Tom:There are 2 people behind me.',
      'Peter:The man behind me is Tom.'], 'Tom'),

    (['John:The man behind me is Peter.',
      'Peter:There is 1 people in front of me.',
      'Tom:There are 2 people behind me.',
      'Peter:The man behind me is Tom.'], None),

    (['Dowfls:There is 0 people behind me.',
      "Dowfls:I'm in 4th position.",
      "Ljiyxbmr:I'm in 2nd position.",
      'Ljiyxbmr:There is 1 people in front of me.',
      'Cvvugb:There are 2 people in front of me.',
      'Cvvugb:There is 1 people behind me.',
      'Tzjlvruhk:The man behind me is Dowfls.',
      'Tzjlvruhk:There are 2 people in front of me.'], None),

    (["Tom:The man behind me is Bob.",
      "Bob:The man in front of me is Tom.",
      "Bob:The man behind me is Gary.",
      "Gary:The man in front of me is Bob.",
      "Fred:I'm in 1st position."], "Fred"),   # if there is always a liar the answer must be Fred

    (["Wrong:The man behind me is Wrong."], "Wrong")
]


class TestMrWrong(unittest.TestCase):
    def test_mrwrong(self):
        i = 0
        for conversation, expected in sample_test_cases:
            i += 1
            with self.subTest(i=i):
                print(f'\nTest {i}')
                self.assertEqual(find_out_mr_wrong(conversation), expected)


if __name__ == '__main__':
    unittest.main()