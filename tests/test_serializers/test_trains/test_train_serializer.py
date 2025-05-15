from django.test import TestCase
from trains.serializers import TrainSerializer
from trains.models import Train, TrainType

class TrainSerializerTests(TestCase):
    def setUp(self):
        self.train_type = TrainType.objects.create(
            name='Express',
        )
        
        self.valid_data = {
            'name': 'Train 123',
            'cargo_num': 10,
            'places_in_cargo': 50
        }
        
        self.train = Train.objects.create(
            name='Train 456',
            cargo_num=8,
            places_in_cargo=40,
            train_type=self.train_type
        )

    def test_serializes_train_correctly(self):
        serializer = TrainSerializer(self.train)
        data = serializer.data
        
        self.assertEqual(data['id'], self.train.id)
        self.assertEqual(data['name'], 'Train 456')
        self.assertEqual(data['cargo_num'], 8)
        self.assertEqual(data['places_in_cargo'], 40)
        
        # Test nested train_type serialization
        self.assertEqual(data['train_type']['name'], 'Express')

    def test_deserializes_valid_data(self):
        serializer = TrainSerializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid())
        train = serializer.save(train_type=self.train_type)
        
        self.assertEqual(train.name, 'Train 123')
        self.assertEqual(train.cargo_num, 10)
        self.assertEqual(train.places_in_cargo, 50)
        self.assertEqual(train.train_type, self.train_type)

    def test_required_fields(self):
        required_fields = ['name', 'cargo_num', 'places_in_cargo']
        for field in required_fields:
            invalid_data = self.valid_data.copy()
            del invalid_data[field]
            serializer = TrainSerializer(data=invalid_data)
            self.assertFalse(serializer.is_valid())
            self.assertIn(field, serializer.errors)

    def test_invalid_cargo_numbers(self):
        invalid_data = self.valid_data.copy()
        invalid_data['cargo_num'] = -1
        serializer = TrainSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('cargo_num', serializer.errors)

        invalid_data = self.valid_data.copy()
        invalid_data['places_in_cargo'] = -1
        serializer = TrainSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('places_in_cargo', serializer.errors)

    def test_update_train(self):
        update_data = {
            'name': 'Updated Train 456',
            'cargo_num': 12,
            'places_in_cargo': 60
        }
        serializer = TrainSerializer(self.train, data=update_data)
        self.assertTrue(serializer.is_valid())
        updated_train = serializer.save()
        
        self.assertEqual(updated_train.name, 'Updated Train 456')
        self.assertEqual(updated_train.cargo_num, 12)
        self.assertEqual(updated_train.places_in_cargo, 60)
        self.assertEqual(updated_train.train_type, self.train_type)

    def test_partial_update(self):
        partial_data = {'cargo_num': 15}
        serializer = TrainSerializer(self.train, data=partial_data, partial=True)
        self.assertTrue(serializer.is_valid())
        updated_train = serializer.save()
        
        self.assertEqual(updated_train.cargo_num, 15)

        self.assertEqual(updated_train.name, 'Train 456')
        self.assertEqual(updated_train.places_in_cargo, 40)
        self.assertEqual(updated_train.train_type, self.train_type)

    def test_cant_update_train_type_through_serializer(self):
        TrainType.objects.create(
            name='Local',
        )
        update_data = {
            'name': 'Train 456',
            'cargo_num': 8,
            'places_in_cargo': 40,
            'train_type': {'name': 'Local',}
        }
        serializer = TrainSerializer(self.train, data=update_data)
        self.assertTrue(serializer.is_valid())
        updated_train = serializer.save()
        self.assertEqual(updated_train.train_type, self.train_type)
