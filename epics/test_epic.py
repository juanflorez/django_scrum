from django.test import Client
from django.test import TestCase
from django.core.urlresolvers import reverse
from models import Epic


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
