from unittest.mock import patch
# from rest_framework import status

from django.test import TestCase,Client
from rest_framework.test import APIClient
from django.urls import reverse
import json
from api.detect_intent import detect_intent_texts
from api.views import collect_response

# Create your tests here.
class ApiTestCase(TestCase):
    # @patch("rest_framework.test.APIClient")
    def test_collect_response(self):
        c=APIClient()
        res=c.post(reverse('api:collect_response'),{'text': 'Foo Bar'}, format='json')
        self.assertEqual(res.status_code, 200)
    @patch("api.detect_intent.dialogflow")
    def test_detect_intent_texts(self,mock_dialogflow):
        x=detect_intent_texts("a","b","c","d")
        mock_dialogflow.SessionsClient.return_value.session_path.assert_called_with('a', 'b')
        self.assertIsNotNone(x)

