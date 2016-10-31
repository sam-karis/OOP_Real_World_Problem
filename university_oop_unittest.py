import unittest

from university_oop import person

class PersonClassTest(unittest.TestCase):
    """docstring for personClassTest"""

    def test_person_instance(self):
        sam = person('Sammy')
        self.assertIsInstance(sam, person, msg='The object should be an instance of the `Person` class')

    def test_object_type(self):
        sam = person('Sammy')
        self.assertTrue((type(sam) is person), msg="The object should be a type of 'person'")

    def test_default_person_name(self):
        name = person()
        sam = person('sammy', 123456, "9:30")
        self.assertEqual(['ABSENT','Still in the compound'],[name.availabity, sam.availabity],
                         msg="The person availabity should be 'ABSENT' if no time_in was passed as an argument")

    def test_default_person_name(self):
        sam = person('sammy', 123456, "9:30PM")
        self.assertEqual('Still in the compound',sam.availabity,
                         msg="The person availabity should be 'Still in the compound' if time_in was passed as an argument and no time_out argument")

    def test_default_person_name(self):
        sam = person('sammy', 123456, "9:30AM", "4.00PM")
        self.assertEqual('Left the compund already',sam.availabity,
                         msg="The person availabity should be 'Still in the compound' if time_in and time_out was passed as an argument")

    def test_person_properties(self):
        sam = person('sammy', 123456, "9:30AM", "4.00PM")
        self.assertListEqual(['sammy', 123456, '9:30AM', '4.00PM'],
                             [sam.name, sam.Id_no, sam.time_in, sam.time_out],
                             msg='The person  name, Id_no, time_in and time_out should be a property of the person')

if __name__ =='__main__':
    unittest.main()