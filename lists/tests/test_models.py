from django.core.exceptions import ValidationError
from django.test import TestCase
from lists.models import Item, List


class ListAndItemModelsTest(TestCase):
    def test_saving_and_retrieving_items(self):
        '''아이템을 저장하고 다시 가져왔을 때 정상적인지?'''
        list_ = List()
        list_.save()

        first_item = Item()
        first_item.text = '첫 번째 아이템'
        first_item.list = list_
        first_item.save()

        second_item = Item()
        second_item.text = '두 번째 아이템'
        second_item.list = list_
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, '첫 번째 아이템')
        self.assertEqual(first_saved_item.list, list_)
        self.assertEqual(second_saved_item.text, '두 번째 아이템')
        self.assertEqual(second_saved_item.list, list_)

    def test_cannot_save_empty_list_items(self):
        '''item.save()를 실행시(빈 리스트 저장되는지 테스트하는거니까) ValidationError가 발생해야 한다'''
        list_ = List.objects.create()
        item = Item(list=list_, text='')
        with self.assertRaises(ValidationError):
            item.save()
            item.full_clean()