from odoo.tests import TransactionCase, tagged

@tagged('test_local')
class TestCourse(TransactionCase):

    def setUp(self):
        super(TestCourse, self).setUp()
        self.course = self.env['openacademy.course'].create({
            'name': 'Test Course',
            'description': 'A course for testing purposes',
        })

    def test_course_creation(self):
        """Test that a course can be created successfully."""
        self.assertEqual(self.course.name, 'Test Course')
        self.assertEqual(self.course.description, 'A course for testing purposes')

    def test_course_copy(self):
        """Test that copying a course creates a new course with the correct name."""
        copied_course = self.course.copy()
        self.assertNotEqual(copied_course.id, self.course.id)
        self.assertEqual(copied_course.name, 'Copy of Test Course')
        self.assertEqual(copied_course.description, 'A course for testing purposes') 

    def test_course_constraints(self):
        """Test that the SQL constraints on the course model are enforced."""
        with self.assertRaises(Exception):
            self.env['openacademy.course'].create({
                'name': 'Invalid Course',
                'description': 'Invalid Course',  # This should trigger the name_description_check constraint
            })

        with self.assertRaises(Exception):
            self.env['openacademy.course'].create({
                'name': 'Test Course',  # This should trigger the name_unique constraint
                'description': 'Another course with the same name',
            })

    
