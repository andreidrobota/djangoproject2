from django.test import TestCase
from .forms import CollaborateForm

# Create your tests here.


class TestCollaborateForm(TestCase):

    def test_form_is_valid(self):
        """
        test for all fields
        """
        form = CollaborateForm({
            'name': 'test',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertTrue(form.is_valid(), msg="Form is unvalid")


    def test_name_is_required(self):
        form = CollaborateForm({
            'name': '',
            'email': 'test@test.com',
            'message': 'Hello!'
            }
        )
        self.assertFalse(form.is_valid(), msg="Form is valid, but a name was not provided!!")


    def test_email_is_required(self):
        form = CollaborateForm({
            'name': 'Test',
            'email': '',
            'message': '',
        })

        self.assertFalse(form.is_valid(), msg="Form is valid, but an email adress was not provided")

    
    def test_message_is_required(self):
        form = CollaborateForm({
            'name': 'test',
            'email': 'test@test.com',
            'message': ''
        })

        self.assertFalse(form.is_valid(), msg="Form is valid, but a message was not provided!")