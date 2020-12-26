from django.db import models

class Card(models.Model):
    title = models.CharField(max_length=100, null=True)
    title_jp = models.CharField(max_length=100, null=True)
    slug = models.SlugField(null=True)
    image_jp = models.ImageField(blank=True, upload_to="jp/")
    image_en = models.ImageField(blank=True, upload_to="en/")
    image_parallel = models.ImageField(blank=True, upload_to="parallel/")
    artist = models.CharField(max_length=100, null=True)
    set = models.ForeignKey("Set", blank=True, null=True, on_delete=models.CASCADE)
    number = models.CharField(max_length=100, null=True)
    CARDTYPE = [
        ('Digitama', 'Digitama'),
        ('Digimon', 'Digimon'),
        ('Tamer', 'Tamer'),
        ('Option', 'Option'),
    ]
    card_type = models.CharField(choices=CARDTYPE, max_length=20, default='Digimon')
    COLORS = [
        ('Red', 'Red'),
        ('Blue', 'Blue'),
        ('Yellow', 'Yellow'),
        ('Green', 'Green'),
        ('Purple', 'Purple'),
        ('Black', 'Black'),
        ('Colorless', 'Colorless'),
    ]
    color = models.CharField(choices=COLORS, max_length=20, default='Red')
    RARITY = [
        ('C', 'Common'),
        ('U', 'Uncommon'),
        ('R', 'Rare'),
        ('SR', 'Super Rare'),
        ('SEC', 'Secret Rare'),
        ('P', 'Promo'),
    ]
    rarity = models.CharField(choices=RARITY, max_length=100, blank=True, null=True, default='Uncommon')
    digimon = models.ForeignKey("Digimon", blank=True, null=True, on_delete=models.CASCADE)
    lv = models.IntegerField(blank=True, null=True)
    dp = models.IntegerField(blank=True, null=True)
    play_cost = models.IntegerField(blank=True, null=True)
    evolution_cost_1 = models.IntegerField(blank=True, null=True)
    evolution_cost_1_color = models.CharField(choices=COLORS, max_length=20, default='Red')
    evolution_cost_2 = models.IntegerField(blank=True, null=True)
    evolution_cost_2_color = models.CharField(choices=COLORS, max_length=20, default='Red')

    KEYWORDSEFFECTS = [
        ('Pierce', 'Pierce'),
        ('Blocker', 'Blocker'),
        ('Jamming', 'Jamming'),
        ('Draw', 'Draw'),
        ('Recovery (Deck) +', 'Recovery (Deck) +'),
        ('Security Attack +', 'Security Attack +'),
        ('Security Attack -', 'Security Attack -'),
        ('Vengeance', 'Vengeance'),
        ('Download', 'Download'),
        ('De-Digivolve', 'De-Digivolve')
    ]

    effect_blue_1 = models.CharField(max_length=100, null=True, blank=True)
    effect_purple_1 = models.CharField(max_length=100, null=True, blank=True)
    effect_txt_1 = models.TextField(blank=True, null=True)
    effect_keyword_1 = models.CharField(choices=KEYWORDSEFFECTS, max_length=100, blank=True, null=True)
    effect_keyword_int_1 = models.IntegerField(blank=True, null=True)
    effect_blue_2 = models.CharField(max_length=100, null=True, blank=True)
    effect_purple_2 = models.CharField(max_length=100, null=True, blank=True)
    effect_txt_2 = models.TextField(blank=True, null=True)
    effect_keyword_2 = models.CharField(choices=KEYWORDSEFFECTS, max_length=100, blank=True, null=True)
    effect_keyword_int_2 = models.IntegerField(blank=True, null=True)
    effect_blue_3 = models.CharField(max_length=100, null=True, blank=True)
    effect_purple_3 = models.CharField(max_length=100, null=True, blank=True)
    effect_txt_3 = models.TextField(blank=True, null=True)
    effect_keyword_3 = models.CharField(choices=KEYWORDSEFFECTS, max_length=100, blank=True, null=True)
    effect_keyword_int_3 = models.IntegerField(blank=True, null=True)

    evolutionary_effect_blue_1 = models.CharField(max_length=100, null=True, blank=True)
    evolutionary_effect_purple_1 = models.CharField(max_length=100, null=True, blank=True)
    evolutionary_effect_txt_1 = models.TextField(blank=True, null=True)
    evolutionary_effect_keyword_1 = models.CharField(choices=KEYWORDSEFFECTS, max_length=100, blank=True, null=True)
    evolutionary_effect_keyword_int_1 = models.IntegerField(blank=True, null=True)
    evolutionary_effect_blue_2 = models.CharField(max_length=100, null=True, blank=True)
    evolutionary_effect_purple_2 = models.CharField(max_length=100, null=True, blank=True)
    evolutionary_effect_txt_2 = models.TextField(blank=True, null=True)
    evolutionary_effect_keyword_2 = models.CharField(choices=KEYWORDSEFFECTS, max_length=100, blank=True, null=True)
    evolutionary_effect_keyword_int_2 = models.IntegerField(blank=True, null=True)
    evolutionary_effect_blue_3 = models.CharField(max_length=100, null=True, blank=True)
    evolutionary_effect_purple_3 = models.CharField(max_length=100, null=True, blank=True)
    evolutionary_effect_txt_3 = models.TextField(blank=True, null=True)
    evolutionary_effect_keyword_3 = models.CharField(choices=KEYWORDSEFFECTS, max_length=100, blank=True, null=True)
    evolutionary_effect_keyword_int_3 = models.IntegerField(blank=True, null=True)

    in_deck_quantity = models.IntegerField(blank=True, null=True)
    promo_name = models.CharField(max_length=100, null=True, blank=True)
    promo_release_date = models.DateField(blank=True, null=True)

    new_date = models.DateField(blank=True, null=True)
    new_parallel = models.BooleanField(blank=True, null=True)

    yuyu_tei = models.URLField(max_length=400, null=True, blank=True)
    suruga_ya = models.URLField(max_length=400, null=True, blank=True)
    amazon_jp = models.URLField(max_length=400, null=True, blank=True)
    ebay = models.URLField(max_length=400, null=True, blank=True)


    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.number


class Set(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(blank=True)
    slug = models.SlugField(null=True)
    release_date = models.DateField(blank=True, null=True)
    total_unique = models.IntegerField(blank=True, null=True)
    total_cards = models.IntegerField(blank=True, null=True)
    produc_image_1 = models.ImageField(blank=True)
    produc_image_2 = models.ImageField(blank=True)
    price_1 = models.CharField(max_length=255, blank=True, null=True)
    price_2 = models.CharField(max_length=255, blank=True, null=True)

    SETTYPES = [
        ('Deck', 'Deck'),
        ('Booster', 'Booster'),
        ('Promo', 'Promo'),
    ]
    set_type = models.CharField(choices=SETTYPES, max_length=20, default='Deck')

    def __str__(self):
        return self.title

class Digimon(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(blank=True)
    slug = models.SlugField(null=True)

    STAGES = [
        ('Mega', 'Mega'),
        ('Ultimate', 'Ultimate'),
        ('Champion', 'Champion'),
        ('Rookie', 'Rookie'),
        ('Baby', 'Baby'),
    ]
    stage = models.CharField(choices=STAGES, max_length=20, default='Rookie')
    attribute = models.CharField(max_length=100, blank=True, null=True)
    digimon_type = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title

class New(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    thumbnail = models.ImageField(blank=True, upload_to="news/")
    content = models.TextField(max_length=2255, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    releated_cards = models.ManyToManyField("Card", blank=True)
    
    def __str__(self):
        return self.title