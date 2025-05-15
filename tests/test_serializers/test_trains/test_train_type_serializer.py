from django.test import TestCase
from trains.serializers import TrainTypeSerializer
from trains.models import TrainType

class TrainTypeSerializerTests(TestCase):
    def setUp(self):
        self.valid_data = {
            'name': 'Express',
        }
        self.train_type = TrainType.objects.create(
            name='Local',
        )

    def test_serializes_train_type_correctly(self):
        serializer = TrainTypeSerializer(self.train_type)
        self.assertEqual(serializer.data['name'], 'Local')

    def test_deserializes_valid_data(self):
        serializer = TrainTypeSerializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid())
        train_type = serializer.save()
        self.assertEqual(train_type.name, 'Express')

    def test_name_required(self):
        invalid_data = self.valid_data.copy()
        del invalid_data['name']
        serializer = TrainTypeSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('name', serializer.errors)

    def test_update_train_type(self):
        update_data = {'name': 'Updated Local'}
        serializer = TrainTypeSerializer(self.train_type, data=update_data)
        self.assertTrue(serializer.is_valid())
        updated_train_type = serializer.save()
        self.assertEqual(updated_train_type.name, 'Updated Local')

    def test_invalid_empty_name(self):
        invalid_data = self.valid_data.copy()
        invalid_data['name'] = ''
        serializer = TrainTypeSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('name', serializer.errors)
