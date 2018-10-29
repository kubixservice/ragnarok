# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth import get_user_model

from core.hashers import hasher
from core.ragnarok import ragnarok
from alfheimproject.settings import CONFIG

User = get_user_model()


class LoginManager(models.Manager):

    def create(self, **kwargs):
        kwargs['user_pass'] = hasher.hash_password(kwargs['user_pass'])
        return super().create(**kwargs)


class Login(models.Model):
    account_id = models.AutoField(primary_key=True)
    userid = models.CharField(max_length=23)
    user_pass = models.CharField(max_length=32)
    sex = models.CharField(max_length=1)
    email = models.CharField(max_length=39)
    group_id = models.IntegerField()
    state = models.PositiveIntegerField()
    unban_time = models.PositiveIntegerField()
    expiration_time = models.PositiveIntegerField()
    logincount = models.PositiveIntegerField()
    lastlogin = models.DateTimeField(blank=True, null=True)
    last_ip = models.CharField(max_length=100)
    birthdate = models.DateField(blank=True, null=True)
    character_slots = models.PositiveIntegerField()
    pincode = models.CharField(max_length=4)
    pincode_change = models.PositiveIntegerField()
    vip_time = models.PositiveIntegerField()
    old_group = models.IntegerField()
    master_account = models.ForeignKey(User, on_delete=models.CASCADE, related_name='game_accounts')

    class Meta:
        managed = False
        db_table = 'login'

    def __str__(self):
        return self.account_id

    def check_password(self, password):
        # Simple check if password is correct
        return self.user_pass == hasher.hash_password(password)

    def set_password(self, password):
        self.user_pass = hasher.hash_password(password)

    objects = LoginManager()


class Char(models.Model):
    char_id = models.AutoField(primary_key=True)
    account_id = models.ForeignKey(Login, on_delete=models.CASCADE, to_field='account_id', db_column='account_id')
    char_num = models.IntegerField()
    name = models.CharField(unique=True, max_length=30)
    class_field = models.PositiveSmallIntegerField(db_column='class', verbose_name='class')
    base_level = models.PositiveSmallIntegerField()
    job_level = models.PositiveSmallIntegerField()
    base_exp = models.BigIntegerField()
    job_exp = models.BigIntegerField()
    zeny = models.PositiveIntegerField()
    str = models.PositiveSmallIntegerField()
    agi = models.PositiveSmallIntegerField()
    vit = models.PositiveSmallIntegerField()
    int = models.PositiveSmallIntegerField()
    dex = models.PositiveSmallIntegerField()
    luk = models.PositiveSmallIntegerField()
    max_hp = models.PositiveIntegerField()
    hp = models.PositiveIntegerField()
    max_sp = models.PositiveIntegerField()
    sp = models.PositiveIntegerField()
    status_point = models.PositiveIntegerField()
    skill_point = models.PositiveIntegerField()
    option = models.IntegerField()
    karma = models.IntegerField()
    manner = models.SmallIntegerField()
    party_id = models.PositiveIntegerField()
    guild_id = models.PositiveIntegerField()
    pet_id = models.PositiveIntegerField()
    homun_id = models.PositiveIntegerField()
    elemental_id = models.PositiveIntegerField()
    hair = models.PositiveIntegerField()
    hair_color = models.PositiveSmallIntegerField()
    clothes_color = models.PositiveSmallIntegerField()
    body = models.PositiveSmallIntegerField()
    weapon = models.PositiveSmallIntegerField()
    shield = models.PositiveSmallIntegerField()
    head_top = models.PositiveSmallIntegerField()
    head_mid = models.PositiveSmallIntegerField()
    head_bottom = models.PositiveSmallIntegerField()
    robe = models.PositiveSmallIntegerField()
    last_map = models.CharField(max_length=11)
    last_x = models.PositiveSmallIntegerField()
    last_y = models.PositiveSmallIntegerField()
    save_map = models.CharField(max_length=11)
    save_x = models.PositiveSmallIntegerField()
    save_y = models.PositiveSmallIntegerField()
    partner_id = models.PositiveIntegerField()
    online = models.IntegerField()
    father = models.PositiveIntegerField()
    mother = models.PositiveIntegerField()
    child = models.PositiveIntegerField()
    fame = models.PositiveIntegerField()
    rename = models.PositiveSmallIntegerField()
    delete_date = models.PositiveIntegerField()
    moves = models.PositiveIntegerField()
    unban_time = models.PositiveIntegerField()
    font = models.PositiveIntegerField()
    uniqueitem_counter = models.PositiveIntegerField()
    sex = models.CharField(max_length=1)
    hotkey_rowshift = models.PositiveIntegerField()
    clan_id = models.PositiveIntegerField()
    last_login = models.DateTimeField(blank=True, null=True)
    title_id = models.PositiveIntegerField()
    show_equip = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'char'

    def reset_position(self):
        self.last_map = CONFIG['server']['other']['default_map']
        self.last_x = CONFIG['server']['other']['default_x']
        self.last_y = CONFIG['server']['other']['default_y']
        self.save()

    def reset_look(self):
        self.clothes_color = 0
        self.hair = 0
        self.hair_color = 0
        self.head_bottom = 0
        self.head_top = 0
        self.head_mid = 0
        self.robe = 0
        self.save()

    def __str__(self):
        return self.name

    @property
    def class_name(self):
        return ragnarok.class_name(self.class_field)


class ItemDb(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    name_english = models.CharField(max_length=50)
    name_japanese = models.CharField(max_length=50)
    type = models.PositiveIntegerField()
    price_buy = models.PositiveIntegerField(blank=True, null=True)
    price_sell = models.PositiveIntegerField(blank=True, null=True)
    weight = models.PositiveSmallIntegerField()
    attack = models.PositiveSmallIntegerField(blank=True, null=True)
    defence = models.PositiveSmallIntegerField(blank=True, null=True)
    range = models.PositiveIntegerField(blank=True, null=True)
    slots = models.PositiveIntegerField(blank=True, null=True)
    equip_jobs = models.BigIntegerField(blank=True, null=True)
    equip_upper = models.PositiveIntegerField(blank=True, null=True)
    equip_genders = models.PositiveIntegerField(blank=True, null=True)
    equip_locations = models.PositiveIntegerField(blank=True, null=True)
    weapon_level = models.PositiveIntegerField(blank=True, null=True)
    equip_level = models.PositiveIntegerField(blank=True, null=True)
    refineable = models.PositiveIntegerField(blank=True, null=True)
    view = models.PositiveSmallIntegerField(blank=True, null=True)
    script = models.TextField(blank=True, null=True)
    equip_script = models.TextField(blank=True, null=True)
    unequip_script = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'item_db'

    def __str__(self):
        return self.name_japanese


class CartInventory(models.Model):
    char_id = models.IntegerField()
    nameid = models.ForeignKey(ItemDb, on_delete=models.DO_NOTHING, related_name='cart_inventory', db_column='nameid')
    amount = models.IntegerField()
    equip = models.PositiveIntegerField()
    identify = models.SmallIntegerField()
    refine = models.PositiveIntegerField()
    attribute = models.IntegerField()
    card0 = models.ForeignKey(ItemDb, on_delete=models.DO_NOTHING, related_name='card0', db_column='card0')
    card1 = models.ForeignKey(ItemDb, on_delete=models.DO_NOTHING, related_name='card1', db_column='card1')
    card2 = models.ForeignKey(ItemDb, on_delete=models.DO_NOTHING, related_name='card2', db_column='card2')
    card3 = models.ForeignKey(ItemDb, on_delete=models.DO_NOTHING, related_name='card3', db_column='card3')
    option_id0 = models.SmallIntegerField()
    option_val0 = models.SmallIntegerField()
    option_parm0 = models.IntegerField()
    option_id1 = models.SmallIntegerField()
    option_val1 = models.SmallIntegerField()
    option_parm1 = models.IntegerField()
    option_id2 = models.SmallIntegerField()
    option_val2 = models.SmallIntegerField()
    option_parm2 = models.IntegerField()
    option_id3 = models.SmallIntegerField()
    option_val3 = models.SmallIntegerField()
    option_parm3 = models.IntegerField()
    option_id4 = models.SmallIntegerField()
    option_val4 = models.SmallIntegerField()
    option_parm4 = models.IntegerField()
    expire_time = models.PositiveIntegerField()
    bound = models.PositiveIntegerField()
    unique_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'cart_inventory'


class Guild(models.Model):
    guild_id = models.IntegerField(unique=True, auto_created=True, primary_key=True)
    name = models.CharField(max_length=24)
    char_id = models.ForeignKey(Char, on_delete=models.CASCADE, to_field='char_id', db_column='char_id')
    master = models.CharField(max_length=24)
    guild_lv = models.PositiveIntegerField()
    connect_member = models.PositiveIntegerField()
    max_member = models.PositiveIntegerField()
    average_lv = models.PositiveSmallIntegerField()
    exp = models.BigIntegerField()
    next_exp = models.PositiveIntegerField()
    skill_point = models.PositiveIntegerField()
    mes1 = models.CharField(max_length=60)
    mes2 = models.CharField(max_length=120)
    emblem_len = models.PositiveIntegerField()
    emblem_id = models.PositiveIntegerField()
    emblem_data = models.TextField(blank=True, null=True)
    last_master_change = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guild'
        unique_together = (('guild_id', 'char_id'),)

    @property
    def emblem_url(self):
        return [self.guild_id, self.emblem_data]

    @property
    def get_members_count(self):
        members = GuildMember.objects.filter(guild_id=self.guild_id).count()
        return members


class GuildAlliance(models.Model):
    guild_id = models.PositiveIntegerField(primary_key=True)
    opposition = models.PositiveIntegerField()
    alliance_id = models.PositiveIntegerField()
    name = models.CharField(max_length=24)

    class Meta:
        managed = False
        db_table = 'guild_alliance'
        unique_together = (('guild_id', 'alliance_id'),)


class GuildCastle(models.Model):
    castle_id = models.PositiveIntegerField(primary_key=True)
    guild_id = models.ForeignKey(Guild, on_delete=models.CASCADE, name='guild_id', to_field='guild_id',
                                 db_column='guild_id')
    economy = models.PositiveIntegerField()
    defense = models.PositiveIntegerField()
    triggere = models.PositiveIntegerField(db_column='triggerE')  # Field name made lowercase.
    triggerd = models.PositiveIntegerField(db_column='triggerD')  # Field name made lowercase.
    nexttime = models.PositiveIntegerField(db_column='nextTime')  # Field name made lowercase.
    paytime = models.PositiveIntegerField(db_column='payTime')  # Field name made lowercase.
    createtime = models.PositiveIntegerField(db_column='createTime')  # Field name made lowercase.
    visiblec = models.PositiveIntegerField(db_column='visibleC')  # Field name made lowercase.
    visibleg0 = models.PositiveIntegerField(db_column='visibleG0')  # Field name made lowercase.
    visibleg1 = models.PositiveIntegerField(db_column='visibleG1')  # Field name made lowercase.
    visibleg2 = models.PositiveIntegerField(db_column='visibleG2')  # Field name made lowercase.
    visibleg3 = models.PositiveIntegerField(db_column='visibleG3')  # Field name made lowercase.
    visibleg4 = models.PositiveIntegerField(db_column='visibleG4')  # Field name made lowercase.
    visibleg5 = models.PositiveIntegerField(db_column='visibleG5')  # Field name made lowercase.
    visibleg6 = models.PositiveIntegerField(db_column='visibleG6')  # Field name made lowercase.
    visibleg7 = models.PositiveIntegerField(db_column='visibleG7')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'guild_castle'


class GuildExpulsion(models.Model):
    guild_id = models.PositiveIntegerField(primary_key=True)
    account_id = models.PositiveIntegerField()
    name = models.CharField(max_length=24)
    mes = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'guild_expulsion'
        unique_together = (('guild_id', 'name'),)


class GuildMember(models.Model):
    guild_id = models.PositiveIntegerField(primary_key=True)
    account_id = models.PositiveIntegerField()
    char_id = models.PositiveIntegerField()
    hair = models.PositiveIntegerField()
    hair_color = models.PositiveSmallIntegerField()
    gender = models.PositiveIntegerField()
    class_field = models.PositiveSmallIntegerField(
        db_column='class')  # Field renamed because it was a Python reserved word.
    lv = models.PositiveSmallIntegerField()
    exp = models.BigIntegerField()
    exp_payper = models.PositiveIntegerField()
    online = models.PositiveIntegerField()
    position = models.PositiveIntegerField()
    name = models.CharField(max_length=24)

    class Meta:
        managed = False
        db_table = 'guild_member'
        unique_together = (('guild_id', 'char_id'),)


class GuildPosition(models.Model):
    guild_id = models.PositiveIntegerField(primary_key=True)
    position = models.PositiveIntegerField()
    name = models.CharField(max_length=24)
    mode = models.PositiveSmallIntegerField()
    exp_mode = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'guild_position'
        unique_together = (('guild_id', 'position'),)


class GuildSkill(models.Model):
    guild_id = models.PositiveIntegerField(primary_key=True)
    id = models.PositiveSmallIntegerField()
    lv = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'guild_skill'
        unique_together = (('guild_id', 'id'),)


class Vendings(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    account_id = models.PositiveIntegerField()
    char_id = models.ForeignKey(Char, on_delete=models.CASCADE, to_field='char_id', db_column='char_id')
    sex = models.CharField(max_length=1)
    map = models.CharField(max_length=20)
    x = models.PositiveSmallIntegerField()
    y = models.PositiveSmallIntegerField()
    title = models.CharField(max_length=80)
    body_direction = models.CharField(max_length=1)
    head_direction = models.CharField(max_length=1)
    sit = models.CharField(max_length=1)
    autotrade = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'vendings'


class AutotradeData(models.Model):
    """VendingItems model. Renamed because of rAthena compatibility"""
    vending_id = models.ForeignKey(Vendings, on_delete=models.CASCADE, to_field='id', db_column='vending_id')
    index = models.PositiveSmallIntegerField(primary_key=True)
    itemkey = models.ForeignKey(CartInventory, on_delete=models.CASCADE, to_field='id', db_column='cartinventory_id',
                                related_name='item', name='item')
    amount = models.PositiveSmallIntegerField()
    price = models.PositiveIntegerField()

    @property
    def vending_title(self):
        return self.vending_id.title

    @property
    def character(self):
        return self.vending_id.char_id

    class Meta:
        managed = False
        db_table = 'vending_items'
