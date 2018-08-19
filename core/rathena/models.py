# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from random import randint
from django.db import models
from django.contrib.auth.models import User
from django.db.models.aggregates import Count

from core.hashers import hasher
from alfheimproject.settings import CONFIG


class AutotradeMerchantsManager(models.Manager):
    def get_random(self):
        count = self.aggregate(count=Count('id'))['count']
        random_index = randint(0, count - 1)
        return self.all()[random_index]


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
    group_id = models.IntegerField(default=0, null=True)
    state = models.IntegerField(default=0, null=True)
    unban_time = models.IntegerField(default=0, null=True)
    expiration_time = models.IntegerField(default=0, null=True)
    logincount = models.IntegerField(default=0, null=True)
    lastlogin = models.DateTimeField(blank=True, null=True, auto_now=True)
    last_ip = models.CharField(max_length=100, default='', null=True)
    birthdate = models.DateField(blank=True, null=True, auto_now=True)
    character_slots = models.IntegerField(default=0, null=True)
    pincode = models.CharField(max_length=4, default='', null=True)
    pincode_change = models.IntegerField(default=0, null=True)
    master_account = models.ForeignKey(User, on_delete=models.CASCADE, related_name='game_accounts')

    class Meta:
        managed = False
        db_table = 'login'

    def __str__(self):
        return self.account_id

    objects = LoginManager()


class Char(models.Model):
    char_id = models.AutoField(primary_key=True)
    account_id = models.ForeignKey(Login, on_delete=models.CASCADE, to_field='account_id', db_column='account_id')
    char_num = models.IntegerField()
    name = models.CharField(unique=True, max_length=30)
    class_field = models.SmallIntegerField(db_column='class')  # Field renamed because it was a Python reserved word.
    base_level = models.SmallIntegerField()
    job_level = models.SmallIntegerField()
    base_exp = models.BigIntegerField()
    job_exp = models.BigIntegerField()
    zeny = models.IntegerField()
    str = models.SmallIntegerField()
    agi = models.SmallIntegerField()
    vit = models.SmallIntegerField()
    int = models.SmallIntegerField()
    dex = models.SmallIntegerField()
    luk = models.SmallIntegerField()
    max_hp = models.IntegerField()
    hp = models.IntegerField()
    max_sp = models.IntegerField()
    sp = models.IntegerField()
    status_point = models.IntegerField()
    skill_point = models.IntegerField()
    option = models.IntegerField()
    karma = models.IntegerField()
    manner = models.SmallIntegerField()
    party_id = models.IntegerField()
    guild_id = models.IntegerField()
    pet_id = models.IntegerField()
    homun_id = models.IntegerField()
    elemental_id = models.IntegerField()
    hair = models.IntegerField()
    hair_color = models.SmallIntegerField()
    clothes_color = models.SmallIntegerField()
    weapon = models.SmallIntegerField()
    shield = models.SmallIntegerField()
    head_top = models.SmallIntegerField()
    head_mid = models.SmallIntegerField()
    head_bottom = models.SmallIntegerField()
    robe = models.SmallIntegerField()
    last_map = models.CharField(max_length=11)
    last_x = models.SmallIntegerField()
    last_y = models.SmallIntegerField()
    save_map = models.CharField(max_length=11)
    save_x = models.SmallIntegerField()
    save_y = models.SmallIntegerField()
    partner_id = models.IntegerField()
    online = models.IntegerField()
    father = models.IntegerField()
    mother = models.IntegerField()
    child = models.IntegerField()
    fame = models.IntegerField()
    rename = models.SmallIntegerField()
    delete_date = models.IntegerField()
    slotchange = models.SmallIntegerField()
    char_opt = models.IntegerField()
    font = models.IntegerField()
    unban_time = models.IntegerField()
    uniqueitem_counter = models.BigIntegerField()
    sex = models.CharField(max_length=1)
    hotkey_rowshift = models.IntegerField()

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


class ItemDb(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    name_english = models.CharField(max_length=50)
    name_japanese = models.CharField(max_length=50)
    type = models.IntegerField()
    price_buy = models.IntegerField(blank=True, null=True)
    price_sell = models.IntegerField(blank=True, null=True)
    weight = models.SmallIntegerField(blank=True, null=True)
    atk = models.SmallIntegerField(blank=True, null=True)
    matk = models.SmallIntegerField(blank=True, null=True)
    defence = models.SmallIntegerField(blank=True, null=True)
    range = models.IntegerField(blank=True, null=True)
    slots = models.IntegerField(blank=True, null=True)
    equip_jobs = models.BigIntegerField(blank=True, null=True)
    equip_upper = models.IntegerField(blank=True, null=True)
    equip_genders = models.IntegerField(blank=True, null=True)
    equip_locations = models.IntegerField(blank=True, null=True)
    weapon_level = models.IntegerField(blank=True, null=True)
    equip_level_min = models.SmallIntegerField(blank=True, null=True)
    equip_level_max = models.SmallIntegerField(blank=True, null=True)
    refineable = models.IntegerField(blank=True, null=True)
    disable_options = models.IntegerField(blank=True, null=True)
    view = models.SmallIntegerField(blank=True, null=True)
    bindonequip = models.IntegerField(blank=True, null=True)
    forceserial = models.IntegerField(blank=True, null=True)
    buyingstore = models.IntegerField(blank=True, null=True)
    delay = models.IntegerField(blank=True, null=True)
    trade_flag = models.SmallIntegerField(blank=True, null=True)
    trade_group = models.SmallIntegerField(blank=True, null=True)
    nouse_flag = models.SmallIntegerField(blank=True, null=True)
    nouse_group = models.SmallIntegerField(blank=True, null=True)
    stack_amount = models.IntegerField(blank=True, null=True)
    stack_flag = models.IntegerField(blank=True, null=True)
    sprite = models.IntegerField(blank=True, null=True)
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
    nameid = models.ForeignKey(ItemDb, on_delete=models.DO_NOTHING, related_name='cart_inventory')
    amount = models.IntegerField()
    equip = models.IntegerField()
    identify = models.SmallIntegerField()
    refine = models.IntegerField()
    attribute = models.IntegerField()
    card0 = models.ForeignKey(ItemDb, on_delete=models.DO_NOTHING, related_name='card0')
    card1 = models.ForeignKey(ItemDb, on_delete=models.DO_NOTHING, related_name='card1')
    card2 = models.ForeignKey(ItemDb, on_delete=models.DO_NOTHING, related_name='card2')
    card3 = models.ForeignKey(ItemDb, on_delete=models.DO_NOTHING, related_name='card3')
    opt_idx0 = models.SmallIntegerField()
    opt_val0 = models.SmallIntegerField()
    opt_idx1 = models.SmallIntegerField()
    opt_val1 = models.SmallIntegerField()
    opt_idx2 = models.SmallIntegerField()
    opt_val2 = models.SmallIntegerField()
    opt_idx3 = models.SmallIntegerField()
    opt_val3 = models.SmallIntegerField()
    opt_idx4 = models.SmallIntegerField()
    opt_val4 = models.SmallIntegerField()
    expire_time = models.IntegerField()
    bound = models.IntegerField()
    unique_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'cart_inventory'


class AccRegNumDb(models.Model):
    account_id = models.IntegerField(primary_key=True)
    key = models.CharField(max_length=32)
    index = models.IntegerField()
    value = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'acc_reg_num'
        unique_together = (('account_id', 'key', 'index'),)


class AccRegStrDb(models.Model):
    account_id = models.IntegerField(primary_key=True)
    key = models.CharField(max_length=32)
    index = models.IntegerField()
    value = models.CharField(max_length=254)

    class Meta:
        managed = False
        db_table = 'acc_reg_str'
        unique_together = (('account_id', 'key', 'index'),)


class AccountData(models.Model):
    account_id = models.IntegerField(primary_key=True)
    bank_vault = models.IntegerField()
    base_exp = models.SmallIntegerField()
    base_drop = models.SmallIntegerField()
    base_death = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'account_data'


class Atcommandlog(models.Model):
    atcommand_id = models.AutoField(primary_key=True)
    atcommand_date = models.DateTimeField(blank=True, null=True)
    account_id = models.IntegerField()
    char_id = models.IntegerField()
    char_name = models.CharField(max_length=25)
    map = models.CharField(max_length=11)
    command = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'atcommandlog'


class Auction(models.Model):
    auction_id = models.BigAutoField(primary_key=True)
    seller_id = models.IntegerField()
    seller_name = models.CharField(max_length=30)
    buyer_id = models.IntegerField()
    buyer_name = models.CharField(max_length=30)
    price = models.IntegerField()
    buynow = models.IntegerField()
    hours = models.SmallIntegerField()
    timestamp = models.IntegerField()
    nameid = models.IntegerField()
    item_name = models.CharField(max_length=50)
    type = models.SmallIntegerField()
    refine = models.IntegerField()
    attribute = models.IntegerField()
    card0 = models.SmallIntegerField()
    card1 = models.SmallIntegerField()
    card2 = models.SmallIntegerField()
    card3 = models.SmallIntegerField()
    opt_idx0 = models.SmallIntegerField()
    opt_val0 = models.SmallIntegerField()
    opt_idx1 = models.SmallIntegerField()
    opt_val1 = models.SmallIntegerField()
    opt_idx2 = models.SmallIntegerField()
    opt_val2 = models.SmallIntegerField()
    opt_idx3 = models.SmallIntegerField()
    opt_val3 = models.SmallIntegerField()
    opt_idx4 = models.SmallIntegerField()
    opt_val4 = models.SmallIntegerField()
    unique_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'auction'


class AutotradeData(models.Model):
    char_id = models.ForeignKey(Char, on_delete=models.CASCADE, to_field='char_id')
    itemkey = models.ForeignKey(CartInventory, on_delete=models.CASCADE)
    amount = models.IntegerField()
    price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'autotrade_data'
        unique_together = (('char_id', 'itemkey'),)


class AutotradeMerchants(models.Model):
    account_id = models.ForeignKey(Login, on_delete=models.CASCADE, to_field='account_id')
    char_id = models.ForeignKey(Char, on_delete=models.CASCADE, to_field='char_id')
    sex = models.IntegerField()
    title = models.CharField(max_length=80)

    class Meta:
        managed = False
        db_table = 'autotrade_merchants'
        unique_together = (('account_id', 'char_id'),)

    objects = AutotradeMerchantsManager()


class Branchlog(models.Model):
    branch_id = models.AutoField(primary_key=True)
    branch_date = models.DateTimeField(blank=True, null=True)
    account_id = models.IntegerField()
    char_id = models.IntegerField()
    char_name = models.CharField(max_length=25)
    map = models.CharField(max_length=11)

    class Meta:
        managed = False
        db_table = 'branchlog'


class CharRegNumDb(models.Model):
    char_id = models.IntegerField(primary_key=True)
    key = models.CharField(max_length=32)
    index = models.IntegerField()
    value = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'char_reg_num'
        unique_together = (('char_id', 'key', 'index'),)


class CharRegStrDb(models.Model):
    char_id = models.IntegerField(primary_key=True)
    key = models.CharField(max_length=32)
    index = models.IntegerField()
    value = models.CharField(max_length=254)

    class Meta:
        managed = False
        db_table = 'char_reg_str'
        unique_together = (('char_id', 'key', 'index'),)


class Charlog(models.Model):
    time = models.DateTimeField(blank=True, null=True)
    char_msg = models.CharField(max_length=255)
    account_id = models.IntegerField()
    char_id = models.IntegerField()
    char_num = models.IntegerField()
    class_field = models.IntegerField(db_column='class')  # Field renamed because it was a Python reserved word.
    name = models.CharField(max_length=23)
    str = models.IntegerField()
    agi = models.IntegerField()
    vit = models.IntegerField()
    int = models.IntegerField(db_column='INT')  # Field name made lowercase.
    dex = models.IntegerField()
    luk = models.IntegerField()
    hair = models.IntegerField()
    hair_color = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'charlog'


class Chatlog(models.Model):
    id = models.BigAutoField(primary_key=True)
    time = models.DateTimeField(blank=True, null=True)
    type = models.CharField(max_length=1)
    type_id = models.IntegerField()
    src_charid = models.IntegerField()
    src_accountid = models.IntegerField()
    src_map = models.CharField(max_length=11)
    src_map_x = models.SmallIntegerField()
    src_map_y = models.SmallIntegerField()
    dst_charname = models.CharField(max_length=25)
    message = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'chatlog'


class Elemental(models.Model):
    ele_id = models.AutoField(primary_key=True)
    char_id = models.IntegerField()
    class_field = models.IntegerField(db_column='class')  # Field renamed because it was a Python reserved word.
    mode = models.IntegerField()
    hp = models.IntegerField()
    sp = models.IntegerField()
    max_hp = models.IntegerField()
    max_sp = models.IntegerField()
    atk1 = models.IntegerField()
    atk2 = models.IntegerField()
    matk = models.IntegerField()
    aspd = models.SmallIntegerField()
    def_field = models.SmallIntegerField(db_column='def')  # Field renamed because it was a Python reserved word.
    mdef = models.SmallIntegerField()
    flee = models.SmallIntegerField()
    hit = models.SmallIntegerField()
    life_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'elemental'


class Friends(models.Model):
    char_id = models.IntegerField()
    friend_account = models.IntegerField()
    friend_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'friends'


class GlobalAccRegNumDb(models.Model):
    account_id = models.IntegerField(primary_key=True)
    key = models.CharField(max_length=32)
    index = models.IntegerField()
    value = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'global_acc_reg_num'
        unique_together = (('account_id', 'key', 'index'),)


class GlobalAccRegStrDb(models.Model):
    account_id = models.IntegerField(primary_key=True)
    key = models.CharField(max_length=32)
    index = models.IntegerField()
    value = models.CharField(max_length=254)

    class Meta:
        managed = False
        db_table = 'global_acc_reg_str'
        unique_together = (('account_id', 'key', 'index'),)


class Guild(models.Model):
    guild_id = models.IntegerField(unique=True, auto_created=True, primary_key=True)
    guild_name = models.CharField(max_length=24, db_column='name')
    char_id = models.ForeignKey(Char, on_delete=models.CASCADE, to_field='char_id', db_column='char_id')
    master = models.CharField(max_length=24)
    guild_lv = models.IntegerField()
    connect_member = models.IntegerField()
    max_member = models.IntegerField()
    average_lv = models.SmallIntegerField()
    exp = models.BigIntegerField()
    next_exp = models.IntegerField()
    skill_point = models.IntegerField()
    mes1 = models.CharField(max_length=60)
    mes2 = models.CharField(max_length=120)
    emblem_len = models.IntegerField()
    emblem_id = models.IntegerField()
    emblem_data = models.TextField(blank=True, null=True)

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
    guild_id = models.IntegerField(primary_key=True)
    opposition = models.IntegerField()
    alliance_id = models.IntegerField()
    name = models.CharField(max_length=24)

    class Meta:
        managed = False
        db_table = 'guild_alliance'
        unique_together = (('guild_id', 'alliance_id'),)


class GuildCastle(models.Model):
    castle_id = models.IntegerField(primary_key=True)
    guild_id = models.ForeignKey(Guild, on_delete=models.CASCADE, name='guild_id', to_field='guild_id',
                                 db_column='guild_id')
    economy = models.IntegerField()
    defense = models.IntegerField()
    triggere = models.IntegerField(db_column='triggerE')  # Field name made lowercase.
    triggerd = models.IntegerField(db_column='triggerD')  # Field name made lowercase.
    nexttime = models.IntegerField(db_column='nextTime')  # Field name made lowercase.
    paytime = models.IntegerField(db_column='payTime')  # Field name made lowercase.
    createtime = models.IntegerField(db_column='createTime')  # Field name made lowercase.
    visiblec = models.IntegerField(db_column='visibleC')  # Field name made lowercase.
    visibleg0 = models.IntegerField(db_column='visibleG0')  # Field name made lowercase.
    visibleg1 = models.IntegerField(db_column='visibleG1')  # Field name made lowercase.
    visibleg2 = models.IntegerField(db_column='visibleG2')  # Field name made lowercase.
    visibleg3 = models.IntegerField(db_column='visibleG3')  # Field name made lowercase.
    visibleg4 = models.IntegerField(db_column='visibleG4')  # Field name made lowercase.
    visibleg5 = models.IntegerField(db_column='visibleG5')  # Field name made lowercase.
    visibleg6 = models.IntegerField(db_column='visibleG6')  # Field name made lowercase.
    visibleg7 = models.IntegerField(db_column='visibleG7')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'guild_castle'


class GuildExpulsion(models.Model):
    guild_id = models.IntegerField(primary_key=True)
    account_id = models.IntegerField()
    name = models.CharField(max_length=24)
    mes = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'guild_expulsion'
        unique_together = (('guild_id', 'name'),)


class GuildMember(models.Model):
    guild_id = models.IntegerField(primary_key=True)
    account_id = models.IntegerField()
    char_id = models.IntegerField()
    hair = models.IntegerField()
    hair_color = models.SmallIntegerField()
    gender = models.IntegerField()
    class_field = models.SmallIntegerField(db_column='class')  # Field renamed because it was a Python reserved word.
    lv = models.SmallIntegerField()
    exp = models.BigIntegerField()
    exp_payper = models.IntegerField()
    online = models.IntegerField()
    position = models.IntegerField()
    name = models.CharField(max_length=24)

    class Meta:
        managed = False
        db_table = 'guild_member'
        unique_together = (('guild_id', 'char_id'),)


class GuildPosition(models.Model):
    guild_id = models.IntegerField(primary_key=True)
    position = models.IntegerField()
    name = models.CharField(max_length=24)
    mode = models.IntegerField()
    exp_mode = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'guild_position'
        unique_together = (('guild_id', 'position'),)


class GuildSkill(models.Model):
    guild_id = models.IntegerField(primary_key=True)
    id = models.SmallIntegerField()
    lv = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'guild_skill'
        unique_together = (('guild_id', 'id'),)


class GuildStorage(models.Model):
    guild_id = models.IntegerField()
    nameid = models.IntegerField()
    amount = models.IntegerField()
    equip = models.IntegerField()
    identify = models.SmallIntegerField()
    refine = models.IntegerField()
    attribute = models.IntegerField()
    card0 = models.SmallIntegerField()
    card1 = models.SmallIntegerField()
    card2 = models.SmallIntegerField()
    card3 = models.SmallIntegerField()
    opt_idx0 = models.SmallIntegerField()
    opt_val0 = models.SmallIntegerField()
    opt_idx1 = models.SmallIntegerField()
    opt_val1 = models.SmallIntegerField()
    opt_idx2 = models.SmallIntegerField()
    opt_val2 = models.SmallIntegerField()
    opt_idx3 = models.SmallIntegerField()
    opt_val3 = models.SmallIntegerField()
    opt_idx4 = models.SmallIntegerField()
    opt_val4 = models.SmallIntegerField()
    expire_time = models.IntegerField()
    bound = models.IntegerField()
    unique_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'guild_storage'


class Homunculus(models.Model):
    homun_id = models.AutoField(primary_key=True)
    char_id = models.IntegerField()
    class_field = models.IntegerField(db_column='class')  # Field renamed because it was a Python reserved word.
    prev_class = models.IntegerField()
    name = models.CharField(max_length=24)
    level = models.SmallIntegerField()
    exp = models.IntegerField()
    intimacy = models.IntegerField()
    hunger = models.SmallIntegerField()
    str = models.SmallIntegerField()
    agi = models.SmallIntegerField()
    vit = models.SmallIntegerField()
    int = models.SmallIntegerField(db_column='INT')  # Field name made lowercase.
    dex = models.SmallIntegerField()
    luk = models.SmallIntegerField()
    hp = models.IntegerField()
    max_hp = models.IntegerField()
    sp = models.IntegerField()
    max_sp = models.IntegerField()
    skill_point = models.SmallIntegerField()
    alive = models.IntegerField()
    rename_flag = models.IntegerField()
    vaporize = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'homunculus'


class Hotkey(models.Model):
    char_id = models.IntegerField(primary_key=True)
    hotkey = models.IntegerField()
    type = models.IntegerField()
    itemskill_id = models.IntegerField()
    skill_lvl = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'hotkey'
        unique_together = (('char_id', 'hotkey'),)


class Interlog(models.Model):
    time = models.DateTimeField(blank=True, null=True)
    log = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'interlog'


class Inventory(models.Model):
    char_id = models.IntegerField()
    nameid = models.IntegerField()
    amount = models.IntegerField()
    equip = models.IntegerField()
    identify = models.SmallIntegerField()
    refine = models.IntegerField()
    attribute = models.IntegerField()
    card0 = models.SmallIntegerField()
    card1 = models.SmallIntegerField()
    card2 = models.SmallIntegerField()
    card3 = models.SmallIntegerField()
    opt_idx0 = models.SmallIntegerField()
    opt_val0 = models.SmallIntegerField()
    opt_idx1 = models.SmallIntegerField()
    opt_val1 = models.SmallIntegerField()
    opt_idx2 = models.SmallIntegerField()
    opt_val2 = models.SmallIntegerField()
    opt_idx3 = models.SmallIntegerField()
    opt_val3 = models.SmallIntegerField()
    opt_idx4 = models.SmallIntegerField()
    opt_val4 = models.SmallIntegerField()
    expire_time = models.IntegerField()
    favorite = models.IntegerField()
    bound = models.IntegerField()
    unique_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'inventory'


class Ipbanlist(models.Model):
    list = models.CharField(max_length=255)
    btime = models.DateTimeField(blank=True, null=True)
    rtime = models.DateTimeField(blank=True, null=True)
    reason = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ipbanlist'


class ItemDb2(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    name_english = models.CharField(max_length=50)
    name_japanese = models.CharField(max_length=50)
    type = models.IntegerField()
    price_buy = models.IntegerField(blank=True, null=True)
    price_sell = models.IntegerField(blank=True, null=True)
    weight = models.SmallIntegerField(blank=True, null=True)
    atk = models.SmallIntegerField(blank=True, null=True)
    matk = models.SmallIntegerField(blank=True, null=True)
    defence = models.SmallIntegerField(blank=True, null=True)
    range = models.IntegerField(blank=True, null=True)
    slots = models.IntegerField(blank=True, null=True)
    equip_jobs = models.BigIntegerField(blank=True, null=True)
    equip_upper = models.IntegerField(blank=True, null=True)
    equip_genders = models.IntegerField(blank=True, null=True)
    equip_locations = models.IntegerField(blank=True, null=True)
    weapon_level = models.IntegerField(blank=True, null=True)
    equip_level_min = models.SmallIntegerField(blank=True, null=True)
    equip_level_max = models.SmallIntegerField(blank=True, null=True)
    refineable = models.IntegerField(blank=True, null=True)
    disable_options = models.IntegerField(blank=True, null=True)
    view = models.SmallIntegerField(blank=True, null=True)
    bindonequip = models.IntegerField(blank=True, null=True)
    forceserial = models.IntegerField(blank=True, null=True)
    buyingstore = models.IntegerField(blank=True, null=True)
    delay = models.IntegerField(blank=True, null=True)
    trade_flag = models.SmallIntegerField(blank=True, null=True)
    trade_group = models.SmallIntegerField(blank=True, null=True)
    nouse_flag = models.SmallIntegerField(blank=True, null=True)
    nouse_group = models.SmallIntegerField(blank=True, null=True)
    stack_amount = models.IntegerField(blank=True, null=True)
    stack_flag = models.IntegerField(blank=True, null=True)
    sprite = models.IntegerField(blank=True, null=True)
    script = models.TextField(blank=True, null=True)
    equip_script = models.TextField(blank=True, null=True)
    unequip_script = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'item_db2'


class Loginlog(models.Model):
    time = models.DateTimeField(blank=True, null=True)
    ip = models.CharField(max_length=15)
    user = models.CharField(max_length=23)
    rcode = models.IntegerField()
    log = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'loginlog'


class Mail(models.Model):
    id = models.BigAutoField(primary_key=True)
    send_name = models.CharField(max_length=30)
    send_id = models.IntegerField()
    dest_name = models.CharField(max_length=30)
    dest_id = models.IntegerField()
    title = models.CharField(max_length=45)
    message = models.CharField(max_length=255)
    time = models.IntegerField()
    status = models.IntegerField()
    zeny = models.IntegerField()
    nameid = models.IntegerField()
    amount = models.IntegerField()
    refine = models.IntegerField()
    attribute = models.IntegerField()
    identify = models.SmallIntegerField()
    card0 = models.SmallIntegerField()
    card1 = models.SmallIntegerField()
    card2 = models.SmallIntegerField()
    card3 = models.SmallIntegerField()
    opt_idx0 = models.SmallIntegerField()
    opt_val0 = models.SmallIntegerField()
    opt_idx1 = models.SmallIntegerField()
    opt_val1 = models.SmallIntegerField()
    opt_idx2 = models.SmallIntegerField()
    opt_val2 = models.SmallIntegerField()
    opt_idx3 = models.SmallIntegerField()
    opt_val3 = models.SmallIntegerField()
    opt_idx4 = models.SmallIntegerField()
    opt_val4 = models.SmallIntegerField()
    unique_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mail'


class Mapreg(models.Model):
    varname = models.CharField(primary_key=True, max_length=32)
    index = models.IntegerField()
    value = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'mapreg'
        unique_together = (('varname', 'index'),)


class Memo(models.Model):
    memo_id = models.AutoField(primary_key=True)
    char_id = models.IntegerField()
    map = models.CharField(max_length=11)
    x = models.SmallIntegerField()
    y = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'memo'


class Mercenary(models.Model):
    mer_id = models.AutoField(primary_key=True)
    char_id = models.IntegerField()
    class_field = models.IntegerField(db_column='class')  # Field renamed because it was a Python reserved word.
    hp = models.IntegerField()
    sp = models.IntegerField()
    kill_counter = models.IntegerField()
    life_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mercenary'


class MercenaryOwner(models.Model):
    char_id = models.IntegerField(primary_key=True)
    merc_id = models.IntegerField()
    arch_calls = models.IntegerField()
    arch_faith = models.IntegerField()
    spear_calls = models.IntegerField()
    spear_faith = models.IntegerField()
    sword_calls = models.IntegerField()
    sword_faith = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mercenary_owner'


class MvpRating(models.Model):
    char_id = models.ForeignKey(Char, on_delete=models.CASCADE, to_field='char_id', db_column='char_id')
    mvp_amount = models.IntegerField()
    score = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mvp_rating'


class MobDb(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    sprite = models.TextField(db_column='Sprite')  # Field name made lowercase.
    kname = models.TextField(db_column='kName')  # Field name made lowercase.
    iname = models.TextField(db_column='iName')  # Field name made lowercase.
    lv = models.IntegerField(db_column='LV')  # Field name made lowercase.
    hp = models.IntegerField(db_column='HP')  # Field name made lowercase.
    sp = models.IntegerField(db_column='SP')  # Field name made lowercase.
    exp = models.IntegerField(db_column='EXP')  # Field name made lowercase.
    jexp = models.IntegerField(db_column='JEXP')  # Field name made lowercase.
    range1 = models.IntegerField(db_column='Range1')  # Field name made lowercase.
    atk1 = models.SmallIntegerField(db_column='ATK1')  # Field name made lowercase.
    atk2 = models.SmallIntegerField(db_column='ATK2')  # Field name made lowercase.
    def_field = models.SmallIntegerField(
        db_column='DEF')  # Field name made lowercase. Field renamed because it was a Python reserved word.
    mdef = models.SmallIntegerField(db_column='MDEF')  # Field name made lowercase.
    str = models.SmallIntegerField(db_column='STR')  # Field name made lowercase.
    agi = models.SmallIntegerField(db_column='AGI')  # Field name made lowercase.
    vit = models.SmallIntegerField(db_column='VIT')  # Field name made lowercase.
    int = models.SmallIntegerField(db_column='INT')  # Field name made lowercase.
    dex = models.SmallIntegerField(db_column='DEX')  # Field name made lowercase.
    luk = models.SmallIntegerField(db_column='LUK')  # Field name made lowercase.
    range2 = models.IntegerField(db_column='Range2')  # Field name made lowercase.
    range3 = models.IntegerField(db_column='Range3')  # Field name made lowercase.
    scale = models.IntegerField(db_column='Scale')  # Field name made lowercase.
    race = models.IntegerField(db_column='Race')  # Field name made lowercase.
    element = models.IntegerField(db_column='Element')  # Field name made lowercase.
    mode = models.IntegerField(db_column='Mode')  # Field name made lowercase.
    speed = models.SmallIntegerField(db_column='Speed')  # Field name made lowercase.
    adelay = models.SmallIntegerField(db_column='aDelay')  # Field name made lowercase.
    amotion = models.SmallIntegerField(db_column='aMotion')  # Field name made lowercase.
    dmotion = models.SmallIntegerField(db_column='dMotion')  # Field name made lowercase.
    mexp = models.IntegerField(db_column='MEXP')  # Field name made lowercase.
    mvp1id = models.SmallIntegerField(db_column='MVP1id')  # Field name made lowercase.
    mvp1per = models.SmallIntegerField(db_column='MVP1per')  # Field name made lowercase.
    mvp2id = models.SmallIntegerField(db_column='MVP2id')  # Field name made lowercase.
    mvp2per = models.SmallIntegerField(db_column='MVP2per')  # Field name made lowercase.
    mvp3id = models.SmallIntegerField(db_column='MVP3id')  # Field name made lowercase.
    mvp3per = models.SmallIntegerField(db_column='MVP3per')  # Field name made lowercase.
    drop1id = models.SmallIntegerField(db_column='Drop1id')  # Field name made lowercase.
    drop1per = models.SmallIntegerField(db_column='Drop1per')  # Field name made lowercase.
    drop2id = models.SmallIntegerField(db_column='Drop2id')  # Field name made lowercase.
    drop2per = models.SmallIntegerField(db_column='Drop2per')  # Field name made lowercase.
    drop3id = models.SmallIntegerField(db_column='Drop3id')  # Field name made lowercase.
    drop3per = models.SmallIntegerField(db_column='Drop3per')  # Field name made lowercase.
    drop4id = models.SmallIntegerField(db_column='Drop4id')  # Field name made lowercase.
    drop4per = models.SmallIntegerField(db_column='Drop4per')  # Field name made lowercase.
    drop5id = models.SmallIntegerField(db_column='Drop5id')  # Field name made lowercase.
    drop5per = models.SmallIntegerField(db_column='Drop5per')  # Field name made lowercase.
    drop6id = models.SmallIntegerField(db_column='Drop6id')  # Field name made lowercase.
    drop6per = models.SmallIntegerField(db_column='Drop6per')  # Field name made lowercase.
    drop7id = models.SmallIntegerField(db_column='Drop7id')  # Field name made lowercase.
    drop7per = models.SmallIntegerField(db_column='Drop7per')  # Field name made lowercase.
    drop8id = models.SmallIntegerField(db_column='Drop8id')  # Field name made lowercase.
    drop8per = models.SmallIntegerField(db_column='Drop8per')  # Field name made lowercase.
    drop9id = models.SmallIntegerField(db_column='Drop9id')  # Field name made lowercase.
    drop9per = models.SmallIntegerField(db_column='Drop9per')  # Field name made lowercase.
    dropcardid = models.SmallIntegerField(db_column='DropCardid')  # Field name made lowercase.
    dropcardper = models.SmallIntegerField(db_column='DropCardper')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mob_db'


class MobDb2(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    sprite = models.TextField(db_column='Sprite')  # Field name made lowercase.
    kname = models.TextField(db_column='kName')  # Field name made lowercase.
    iname = models.TextField(db_column='iName')  # Field name made lowercase.
    lv = models.IntegerField(db_column='LV')  # Field name made lowercase.
    hp = models.IntegerField(db_column='HP')  # Field name made lowercase.
    sp = models.IntegerField(db_column='SP')  # Field name made lowercase.
    exp = models.IntegerField(db_column='EXP')  # Field name made lowercase.
    jexp = models.IntegerField(db_column='JEXP')  # Field name made lowercase.
    range1 = models.IntegerField(db_column='Range1')  # Field name made lowercase.
    atk1 = models.SmallIntegerField(db_column='ATK1')  # Field name made lowercase.
    atk2 = models.SmallIntegerField(db_column='ATK2')  # Field name made lowercase.
    def_field = models.SmallIntegerField(
        db_column='DEF')  # Field name made lowercase. Field renamed because it was a Python reserved word.
    mdef = models.SmallIntegerField(db_column='MDEF')  # Field name made lowercase.
    str = models.SmallIntegerField(db_column='STR')  # Field name made lowercase.
    agi = models.SmallIntegerField(db_column='AGI')  # Field name made lowercase.
    vit = models.SmallIntegerField(db_column='VIT')  # Field name made lowercase.
    int = models.SmallIntegerField(db_column='INT')  # Field name made lowercase.
    dex = models.SmallIntegerField(db_column='DEX')  # Field name made lowercase.
    luk = models.SmallIntegerField(db_column='LUK')  # Field name made lowercase.
    range2 = models.IntegerField(db_column='Range2')  # Field name made lowercase.
    range3 = models.IntegerField(db_column='Range3')  # Field name made lowercase.
    scale = models.IntegerField(db_column='Scale')  # Field name made lowercase.
    race = models.IntegerField(db_column='Race')  # Field name made lowercase.
    element = models.IntegerField(db_column='Element')  # Field name made lowercase.
    mode = models.IntegerField(db_column='Mode')  # Field name made lowercase.
    speed = models.SmallIntegerField(db_column='Speed')  # Field name made lowercase.
    adelay = models.SmallIntegerField(db_column='aDelay')  # Field name made lowercase.
    amotion = models.SmallIntegerField(db_column='aMotion')  # Field name made lowercase.
    dmotion = models.SmallIntegerField(db_column='dMotion')  # Field name made lowercase.
    mexp = models.IntegerField(db_column='MEXP')  # Field name made lowercase.
    mvp1id = models.SmallIntegerField(db_column='MVP1id')  # Field name made lowercase.
    mvp1per = models.SmallIntegerField(db_column='MVP1per')  # Field name made lowercase.
    mvp2id = models.SmallIntegerField(db_column='MVP2id')  # Field name made lowercase.
    mvp2per = models.SmallIntegerField(db_column='MVP2per')  # Field name made lowercase.
    mvp3id = models.SmallIntegerField(db_column='MVP3id')  # Field name made lowercase.
    mvp3per = models.SmallIntegerField(db_column='MVP3per')  # Field name made lowercase.
    drop1id = models.SmallIntegerField(db_column='Drop1id')  # Field name made lowercase.
    drop1per = models.SmallIntegerField(db_column='Drop1per')  # Field name made lowercase.
    drop2id = models.SmallIntegerField(db_column='Drop2id')  # Field name made lowercase.
    drop2per = models.SmallIntegerField(db_column='Drop2per')  # Field name made lowercase.
    drop3id = models.SmallIntegerField(db_column='Drop3id')  # Field name made lowercase.
    drop3per = models.SmallIntegerField(db_column='Drop3per')  # Field name made lowercase.
    drop4id = models.SmallIntegerField(db_column='Drop4id')  # Field name made lowercase.
    drop4per = models.SmallIntegerField(db_column='Drop4per')  # Field name made lowercase.
    drop5id = models.SmallIntegerField(db_column='Drop5id')  # Field name made lowercase.
    drop5per = models.SmallIntegerField(db_column='Drop5per')  # Field name made lowercase.
    drop6id = models.SmallIntegerField(db_column='Drop6id')  # Field name made lowercase.
    drop6per = models.SmallIntegerField(db_column='Drop6per')  # Field name made lowercase.
    drop7id = models.SmallIntegerField(db_column='Drop7id')  # Field name made lowercase.
    drop7per = models.SmallIntegerField(db_column='Drop7per')  # Field name made lowercase.
    drop8id = models.SmallIntegerField(db_column='Drop8id')  # Field name made lowercase.
    drop8per = models.SmallIntegerField(db_column='Drop8per')  # Field name made lowercase.
    drop9id = models.SmallIntegerField(db_column='Drop9id')  # Field name made lowercase.
    drop9per = models.SmallIntegerField(db_column='Drop9per')  # Field name made lowercase.
    dropcardid = models.SmallIntegerField(db_column='DropCardid')  # Field name made lowercase.
    dropcardper = models.SmallIntegerField(db_column='DropCardper')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mob_db2'


class MobSkillDb(models.Model):
    mob_id = models.SmallIntegerField(db_column='MOB_ID')  # Field name made lowercase.
    info = models.TextField(db_column='INFO')  # Field name made lowercase.
    state = models.TextField(db_column='STATE')  # Field name made lowercase.
    skill_id = models.SmallIntegerField(db_column='SKILL_ID')  # Field name made lowercase.
    skill_lv = models.IntegerField(db_column='SKILL_LV')  # Field name made lowercase.
    rate = models.SmallIntegerField(db_column='RATE')  # Field name made lowercase.
    casttime = models.IntegerField(db_column='CASTTIME')  # Field name made lowercase.
    delay = models.IntegerField(db_column='DELAY')  # Field name made lowercase.
    cancelable = models.TextField(db_column='CANCELABLE')  # Field name made lowercase.
    target = models.TextField(db_column='TARGET')  # Field name made lowercase.
    condition = models.TextField(db_column='CONDITION')  # Field name made lowercase.
    condition_value = models.TextField(db_column='CONDITION_VALUE', blank=True, null=True)  # Field name made lowercase.
    val1 = models.IntegerField(db_column='VAL1', blank=True, null=True)  # Field name made lowercase.
    val2 = models.IntegerField(db_column='VAL2', blank=True, null=True)  # Field name made lowercase.
    val3 = models.IntegerField(db_column='VAL3', blank=True, null=True)  # Field name made lowercase.
    val4 = models.IntegerField(db_column='VAL4', blank=True, null=True)  # Field name made lowercase.
    val5 = models.IntegerField(db_column='VAL5', blank=True, null=True)  # Field name made lowercase.
    emotion = models.TextField(db_column='EMOTION', blank=True, null=True)  # Field name made lowercase.
    chat = models.TextField(db_column='CHAT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mob_skill_db'


class MobSkillDb2(models.Model):
    mob_id = models.SmallIntegerField(db_column='MOB_ID')  # Field name made lowercase.
    info = models.TextField(db_column='INFO')  # Field name made lowercase.
    state = models.TextField(db_column='STATE')  # Field name made lowercase.
    skill_id = models.SmallIntegerField(db_column='SKILL_ID')  # Field name made lowercase.
    skill_lv = models.IntegerField(db_column='SKILL_LV')  # Field name made lowercase.
    rate = models.SmallIntegerField(db_column='RATE')  # Field name made lowercase.
    casttime = models.IntegerField(db_column='CASTTIME')  # Field name made lowercase.
    delay = models.IntegerField(db_column='DELAY')  # Field name made lowercase.
    cancelable = models.TextField(db_column='CANCELABLE')  # Field name made lowercase.
    target = models.TextField(db_column='TARGET')  # Field name made lowercase.
    condition = models.TextField(db_column='CONDITION')  # Field name made lowercase.
    condition_value = models.TextField(db_column='CONDITION_VALUE', blank=True, null=True)  # Field name made lowercase.
    val1 = models.IntegerField(db_column='VAL1', blank=True, null=True)  # Field name made lowercase.
    val2 = models.IntegerField(db_column='VAL2', blank=True, null=True)  # Field name made lowercase.
    val3 = models.IntegerField(db_column='VAL3', blank=True, null=True)  # Field name made lowercase.
    val4 = models.IntegerField(db_column='VAL4', blank=True, null=True)  # Field name made lowercase.
    val5 = models.IntegerField(db_column='VAL5', blank=True, null=True)  # Field name made lowercase.
    emotion = models.TextField(db_column='EMOTION', blank=True, null=True)  # Field name made lowercase.
    chat = models.TextField(db_column='CHAT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mob_skill_db2'


class Mvplog(models.Model):
    mvp_id = models.AutoField(primary_key=True)
    mvp_date = models.DateTimeField(blank=True, null=True)
    kill_char_id = models.IntegerField()
    monster_id = models.SmallIntegerField()
    prize = models.IntegerField()
    mvpexp = models.IntegerField()
    map = models.CharField(max_length=11)

    class Meta:
        managed = False
        db_table = 'mvplog'


class NpcMarketData(models.Model):
    name = models.CharField(primary_key=True, max_length=24)
    itemid = models.IntegerField()
    amount = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'npc_market_data'
        unique_together = (('name', 'itemid'),)


class Npclog(models.Model):
    npc_id = models.AutoField(primary_key=True)
    npc_date = models.DateTimeField(blank=True, null=True)
    account_id = models.IntegerField()
    char_id = models.IntegerField()
    char_name = models.CharField(max_length=25)
    map = models.CharField(max_length=11)
    mes = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'npclog'


class Party(models.Model):
    party_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=24)
    exp = models.IntegerField()
    item = models.IntegerField()
    leader_id = models.IntegerField()
    leader_char = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'party'


class Pet(models.Model):
    pet_id = models.AutoField(primary_key=True)
    class_field = models.IntegerField(db_column='class')  # Field renamed because it was a Python reserved word.
    name = models.CharField(max_length=24)
    account_id = models.IntegerField()
    char_id = models.IntegerField()
    level = models.SmallIntegerField()
    egg_id = models.SmallIntegerField()
    equip = models.IntegerField()
    intimate = models.SmallIntegerField()
    hungry = models.SmallIntegerField()
    rename_flag = models.IntegerField()
    incubate = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pet'


class Picklog(models.Model):
    time = models.DateTimeField(blank=True, null=True)
    char_id = models.IntegerField()
    type = models.CharField(max_length=1)
    nameid = models.IntegerField()
    amount = models.IntegerField()
    refine = models.IntegerField()
    card0 = models.IntegerField()
    card1 = models.IntegerField()
    card2 = models.IntegerField()
    card3 = models.IntegerField()
    opt_idx0 = models.SmallIntegerField()
    opt_val0 = models.SmallIntegerField()
    opt_idx1 = models.SmallIntegerField()
    opt_val1 = models.SmallIntegerField()
    opt_idx2 = models.SmallIntegerField()
    opt_val2 = models.SmallIntegerField()
    opt_idx3 = models.SmallIntegerField()
    opt_val3 = models.SmallIntegerField()
    opt_idx4 = models.SmallIntegerField()
    opt_val4 = models.SmallIntegerField()
    unique_id = models.BigIntegerField()
    map = models.CharField(max_length=11)

    class Meta:
        managed = False
        db_table = 'picklog'


class Quest(models.Model):
    char_id = models.IntegerField(primary_key=True)
    quest_id = models.IntegerField()
    state = models.CharField(max_length=1)
    time = models.IntegerField()
    count1 = models.IntegerField()
    count2 = models.IntegerField()
    count3 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'quest'
        unique_together = (('char_id', 'quest_id'),)


class Ragsrvinfo(models.Model):
    index = models.IntegerField()
    name = models.CharField(max_length=255)
    exp = models.IntegerField()
    jexp = models.IntegerField()
    drop = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ragsrvinfo'


class ScData(models.Model):
    account_id = models.IntegerField(primary_key=True)
    char_id = models.IntegerField()
    type = models.SmallIntegerField()
    tick = models.IntegerField()
    val1 = models.IntegerField()
    val2 = models.IntegerField()
    val3 = models.IntegerField()
    val4 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sc_data'
        unique_together = (('account_id', 'char_id', 'type'),)


class Skill(models.Model):
    char_id = models.IntegerField(primary_key=True)
    id = models.SmallIntegerField()
    lv = models.IntegerField()
    flag = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'skill'
        unique_together = (('char_id', 'id'),)


class SkillHomunculus(models.Model):
    homun_id = models.IntegerField(primary_key=True)
    id = models.IntegerField()
    lv = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'skill_homunculus'
        unique_together = (('homun_id', 'id'),)


class SqlUpdates(models.Model):
    timestamp = models.IntegerField(primary_key=True)
    ignored = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'sql_updates'


class Storage(models.Model):
    account_id = models.IntegerField()
    nameid = models.IntegerField()
    amount = models.SmallIntegerField()
    equip = models.IntegerField()
    identify = models.SmallIntegerField()
    refine = models.IntegerField()
    attribute = models.IntegerField()
    card0 = models.SmallIntegerField()
    card1 = models.SmallIntegerField()
    card2 = models.SmallIntegerField()
    card3 = models.SmallIntegerField()
    opt_idx0 = models.SmallIntegerField()
    opt_val0 = models.SmallIntegerField()
    opt_idx1 = models.SmallIntegerField()
    opt_val1 = models.SmallIntegerField()
    opt_idx2 = models.SmallIntegerField()
    opt_val2 = models.SmallIntegerField()
    opt_idx3 = models.SmallIntegerField()
    opt_val3 = models.SmallIntegerField()
    opt_idx4 = models.SmallIntegerField()
    opt_val4 = models.SmallIntegerField()
    expire_time = models.IntegerField()
    bound = models.IntegerField()
    unique_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'storage'


class Vendings(models.Model):
    id = models.IntegerField(primary_key=True)
    account_id = models.IntegerField()
    char_id = models.ForeignKey(Char, on_delete=models.CASCADE, to_field='char_id', db_column='char_id')
    sex = models.CharField(max_length=1)
    map = models.CharField(max_length=20)
    x = models.SmallIntegerField()
    y = models.SmallIntegerField()
    title = models.CharField(max_length=80)
    body_direction = models.CharField(max_length=1)
    head_direction = models.CharField(max_length=1)
    sit = models.CharField(max_length=1)
    autotrade = models.IntegerField()
    vend_coin = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'vendings'


class VendingItems(models.Model):
    vending_id = models.ForeignKey(Vendings, on_delete=models.CASCADE, to_field='id', db_column='vending_id')
    index = models.SmallIntegerField()
    cartinventory_id = models.ForeignKey(CartInventory, on_delete=models.CASCADE, to_field='id',
                                         db_column='cartinventory_id')
    amount = models.SmallIntegerField()
    price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'vending_items'


class Zenylog(models.Model):
    time = models.DateTimeField(blank=True, null=True)
    char_id = models.IntegerField()
    src_id = models.IntegerField()
    type = models.CharField(max_length=1)
    amount = models.IntegerField()
    map = models.CharField(max_length=11)

    class Meta:
        managed = False
        db_table = 'zenylog'


