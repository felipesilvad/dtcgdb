from django.db import models

class Card(models.Model):
    title = models.CharField(max_length=100, null=True)
    title_jp = models.CharField(max_length=100, null=True)
    slug = models.SlugField(null=True)
    image_jp = models.ImageField(blank=True, upload_to="jp/")
    image_en = models.ImageField(blank=True, upload_to="en/")
    translated = models.BooleanField(null=True, blank=True, default='False')
    artist = models.CharField(max_length=100, null=True, blank=True)
    image_parallel_jp = models.ImageField(blank=True, upload_to="parallel-jp/")
    image_parallel_en = models.ImageField(blank=True, upload_to="parallel-en/")
    artist_parallel = models.CharField(max_length=100, null=True, blank=True)
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

    effect = models.ManyToManyField("Effect", blank=True)

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

class Effect(models.Model):
    EFFECT_TYPES = [
        ('Main', 'Main'),
        ('Inheritable', 'Inheritable'),
    ]
    effect_type = models.CharField(choices=EFFECT_TYPES, max_length=100, blank=True, null=True)
    BLUE_EFFECTS = [
        ("Main", "Main"),
        ("Security", "Security"),
        ("Your Turn", "Your Turn"),
        ("On Play", "On Play"),
        ("When Attacking", "When Attacking"),
        ("When Digivolving", "When Digivolving"),
        ("Start of Your Turn", "Start of Your Turn"),
        ("Opponent's Turn", "Opponent's Turn"),
        ("On Deletion", "On Deletion"),
        ("End of Attack", "End of Attack"),
        ("All Turns", "All Turns"),
        ("End of Opponent's Turn", "End of Opponent's Turn"),
        ("Both Turns", "Both Turns"),
    ]
    effect_blue = models.CharField(choices=BLUE_EFFECTS, max_length=100, blank=True, null=True)
    PURPLE_EFFECTS = [
        ("Once Per Turn", "Once Per Turn"),
        ("Twice Per Turn", "Twice Per Turn"),
    ]
    effect_purple = models.CharField(choices=PURPLE_EFFECTS, max_length=100, blank=True, null=True)
    effect_txt = models.TextField(blank=True, null=True)
    effect_keyword = models.ForeignKey("EffectKeyword", blank=True, null=True, on_delete=models.CASCADE)
    effect_keyword_int = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.effect_type} - {self.effect_blue} - {self.effect_purple}'

class EffectKeyword(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    desc = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

class Set(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to="sets/")
    slug = models.SlugField(null=True)
    release_date = models.DateField(blank=True, null=True)
    total_unique = models.IntegerField(blank=True, null=True)
    total_cards = models.IntegerField(blank=True, null=True)
    produc_image_1 = models.ImageField(blank=True, upload_to="sets/")
    produc_image_2 = models.ImageField(blank=True, upload_to="sets/")
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
    image = models.ImageField(blank=True, upload_to="digimon-icons/")
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