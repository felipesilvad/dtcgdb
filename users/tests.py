from django.test import TestCase
from django.shortcuts import render, redirect
from django.db.models.query import QuerySet

# Create your tests here.

# sets_total_cards = cards.values('set__slug').annotate(total=Count('set__slug'))
    
    # for usercard in usercards_set_c:
    #     print(usercard.total)

    # for usercard in usercards_set_c:
    #     if usercard.card__set__slug == sets_total_cards.slug:
    #         for setcard in sets_total_cards:
    #             idkman = usercard.total * setcard.total_unique


    # QuerySet [
    #     for usercard in usercards_set_c:
    #         for setcard in sets_total_cards:
    #             {'set': setcard.slug, 'total':
    #                 if usercard.card__set__slug == setcard.slug:
    #                     usercard.total * setcard.total_unique
    #             }
    # ]

    
usercards_set_c= [{'card__set__slug': 'bt1', 'total': 4}, {'card__set__slug': 'bt2', 'total': 1}, {'card__set__slug': 'p', 'total': 1}, {'card__set__slug': 'st1', 'total': 2}]
sets_total_cards = [{'slug': 'bt1', 'total_unique': 115}, {'slug': 'bt2', 'total_unique': 112}, {'slug': 'bt3', 'total_unique': 112}, {'slug': 'bt4', 'total_unique': 115}, {'slug': 'p', 'total_unique': 100}, {'slug': 'st1', 'total_unique': 16}, {'slug': 'st2', 'total_unique': 16}, {'slug': 'st3', 'total_unique': 16}, {'slug': 'st4', 'total_unique': 16}, {'slug': 'st5', 'total_unique': 16}, {'slug': 'st6', 'total_unique': 16}]

set_percentages = {}

for setcards in sets_total_cards:
     for usercards in usercards_set_c:
        if usercards['card__set__slug'] == setcards['slug']:
            set_percentages[setcards['slug']] = round((usercards['total'] / setcards['total_unique']) * 100, 2)

print(set_percentages)
# for setcards in sets_total_cards:
#     for usercards in usercards_set_c:
#         if usercards['card__set__slug'] == setcards['slug']:
#             print(setcards['slug'], ":", round((usercards['total'] / setcards['total_unique']) * 100, 2), "%")