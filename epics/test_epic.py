from django.test import Client
from django.test import TestCase
from django_webtest import WebTest
from django.core.urlresolvers import reverse
from models import Epic
from forms import EpicForm



# views (uses reverse)
class EpicTest(TestCase):

    """
    ensure the form test is present
    TODO: use reverse urls
    """
    def test_epic_list_view(self):
        w =  self.client.get("/epics/")
        self.assertEqual(w.status_code, 200)

    """
    ensure the list of epics is passed
    TODO: use reverse urls
    """

    def test_epic_list(self):
    	w =  self.client.get("/epics/")
        self.assertIn("epics_list", w.context)

    """
    ensure the form test is present
    TODO: use reverse urls
    """
    
    def test_epic_create_view(self):
    	frm = self.client.get("/epics/create/")
    	self.assertEqual(frm.status_code, 200)

class EpicFormTest(WebTest):

    def setUp(self):
        self.epic = Epic.objects.create(
		    title="Test Epic from Unit test", 
		    content="Automatic test content", 
			points="2",
			)


    def test_valid_data(self):
    	testName    = "testing epic form"
    	testContent =  ("This epic is created automatically by the test test_valid_data \\n" 
		               "there is an additional line here")
    	testPoints  = "8"

    	form = EpicForm({
        "title"    : testName,
		"content" : testContent,
		"points"  : testPoints,
        })

        epic = form.save()
        self.assertEqual(epic.title, testName)
        self.assertEqual(epic.content, testContent)
        self.assertEqual(epic.points, int(testPoints))


    def test_blank_data(self):
    	form = EpicForm({

    		})
    	self.assertFalse(form.is_valid())
    	self.assertEqual(form.errors, {
    		'title': ['This field is required.'],
    		'content': ['This field is required.'],
    		'points': ['This field is required.'	],
    		})
    
    #def test_edit(self):





