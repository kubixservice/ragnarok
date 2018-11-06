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
    account_id = models.AutoField(primary_key=True, auto_created=True)
    userid = models.CharField(max_length=23)
    user_pass = models.CharField(max_length=32)
    sex = models.CharField(max_length=1)
    email = models.CharField(max_length=39)
    group_id = models.IntegerField(default=0)
    state = models.PositiveIntegerField(default=0)
    unban_time = models.PositiveIntegerField(default=0)
    expiration_time = models.PositiveIntegerField(default=0)
    logincount = models.PositiveIntegerField(default=0)
    lastlogin = models.DateTimeField(blank=True, null=True)
    last_ip = models.CharField(max_length=100, null=True, default='')
    birthdate = models.DateField(blank=True, null=True)
    character_slots = models.PositiveIntegerField(default=0)
    pincode = models.CharField(max_length=4, default='')
    pincode_change = models.PositiveIntegerField(null=True, default=0)
    master_account = models.ForeignKey(User, on_delete=models.CASCADE, related_name='game_accounts', default=1,
                                       null=True, blank=True)

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
    class_field = models.PositiveSmallIntegerField(db_column='class')
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
    clan_id = models.PositiveIntegerField()
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
    last_login = models.BigIntegerField(blank=True, null=True)
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
    slotchange = models.PositiveSmallIntegerField()
    char_opt = models.PositiveIntegerField()
    font = models.PositiveIntegerField()
    unban_time = models.PositiveIntegerField()
    uniqueitem_counter = models.BigIntegerField()
    sex = models.CharField(max_length=1)
    hotkey_rowshift = models.PositiveIntegerField()
    attendance_count = models.PositiveIntegerField()
    attendance_timer = models.BigIntegerField(blank=True, null=True)
    title_id = models.PositiveIntegerField()

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
    id = models.PositiveIntegerField(primary_key=True)
    name_english = models.CharField(max_length=50)
    name_japanese = models.CharField(max_length=50)
    type = models.PositiveIntegerField()
    subtype = models.PositiveIntegerField(blank=True, null=True)
    price_buy = models.IntegerField(blank=True, null=True)
    price_sell = models.IntegerField(blank=True, null=True)
    weight = models.PositiveSmallIntegerField(blank=True, null=True)
    atk = models.PositiveSmallIntegerField(blank=True, null=True)
    matk = models.PositiveSmallIntegerField(blank=True, null=True)
    defence = models.PositiveSmallIntegerField(blank=True, null=True)
    range = models.PositiveIntegerField(blank=True, null=True)
    slots = models.PositiveIntegerField(blank=True, null=True)
    equip_jobs = models.BigIntegerField(blank=True, null=True)
    equip_upper = models.PositiveIntegerField(blank=True, null=True)
    equip_genders = models.PositiveIntegerField(blank=True, null=True)
    equip_locations = models.PositiveIntegerField(blank=True, null=True)
    weapon_level = models.PositiveIntegerField(blank=True, null=True)
    equip_level_min = models.PositiveSmallIntegerField(blank=True, null=True)
    equip_level_max = models.PositiveSmallIntegerField(blank=True, null=True)
    refineable = models.PositiveIntegerField(blank=True, null=True)
    disable_options = models.PositiveIntegerField(blank=True, null=True)
    view_sprite = models.PositiveSmallIntegerField(blank=True, null=True)
    bindonequip = models.PositiveIntegerField(blank=True, null=True)
    forceserial = models.PositiveIntegerField(blank=True, null=True)
    buyingstore = models.PositiveIntegerField(blank=True, null=True)
    delay = models.PositiveIntegerField(blank=True, null=True)
    trade_flag = models.PositiveSmallIntegerField(blank=True, null=True)
    trade_group = models.PositiveSmallIntegerField(blank=True, null=True)
    nouse_flag = models.PositiveSmallIntegerField(blank=True, null=True)
    nouse_group = models.PositiveSmallIntegerField(blank=True, null=True)
    stack_amount = models.PositiveIntegerField(blank=True, null=True)
    stack_flag = models.PositiveIntegerField(blank=True, null=True)
    sprite = models.PositiveIntegerField(blank=True, null=True)
    script = models.TextField(blank=True, null=True)
    equip_script = models.TextField(blank=True, null=True)
    unequip_script = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'item_db'


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
    opt_idx0 = models.PositiveSmallIntegerField()
    opt_val0 = models.SmallIntegerField()
    opt_idx1 = models.PositiveSmallIntegerField()
    opt_val1 = models.SmallIntegerField()
    opt_idx2 = models.PositiveSmallIntegerField()
    opt_val2 = models.SmallIntegerField()
    opt_idx3 = models.PositiveSmallIntegerField()
    opt_val3 = models.SmallIntegerField()
    opt_idx4 = models.PositiveSmallIntegerField()
    opt_val4 = models.SmallIntegerField()
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
    class_field = models.PositiveSmallIntegerField(db_column='class')
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
    mode = models.PositiveIntegerField()
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


class AutotradeData(models.Model):
    char_id = models.OneToOneField(Char, on_delete=models.CASCADE, to_field='char_id', primary_key=True,
                                   db_column='char_id', related_name='character', name='character')
    itemkey = models.ForeignKey(CartInventory, on_delete=models.CASCADE, db_column='itemkey', related_name='item',
                                name='item')
    amount = models.IntegerField()
    price = models.IntegerField()

    @property
    def vending_title(self):
        return self.merchant.title

    @property
    def current_map(self):
        # self.character because [self.char_id > name = character]
        return [self.character.last_map, self.character.last_x, self.character.last_y]

    class Meta:
        managed = False
        db_table = 'autotrade_data'
        unique_together = (('character', 'item'),)


class AutotradeMerchants(models.Model):
    account_id = models.ForeignKey(Login, on_delete=models.CASCADE, to_field='account_id', db_column='account_id')
    char_id = models.OneToOneField(AutotradeData, on_delete=models.CASCADE, to_field='character', primary_key=True,
                                   db_column='char_id', related_name='merchant')
    sex = models.IntegerField()
    title = models.CharField(max_length=80)

    class Meta:
        managed = False
        db_table = 'autotrade_merchants'
        unique_together = (('account_id', 'char_id'),)
