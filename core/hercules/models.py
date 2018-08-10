import hashlib

from django.db import models
from django.contrib.auth.models import User

from alfheimproject.settings import USE_MD5, DEFAULT_MAP, DEFAULT_X, DEFAULT_Y, CONFIG


class LoginManager(models.Manager):

    def create(self, **kwargs):
        if USE_MD5:
            kwargs['user_pass'] = hashlib.md5(kwargs['user_pass'].encode('utf-8')).hexdigest()
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
    master_account = models.ForeignKey(User, on_delete=models.CASCADE, related_name='game_accounts')

    class Meta:
        managed = False
        db_table = 'login'

    objects = LoginManager()


class Char(models.Model):
    char_id = models.AutoField(primary_key=True)
    account_id = models.ForeignKey(Login, on_delete=models.CASCADE, related_name='game_characters')
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


class CartInventory(models.Model):
    char_id = models.ForeignKey(Char, on_delete=models.CASCADE, related_name='cart')
    nameid = models.IntegerField()
    amount = models.IntegerField()
    equip = models.PositiveIntegerField()
    identify = models.SmallIntegerField()
    refine = models.PositiveIntegerField()
    attribute = models.IntegerField()
    card0 = models.SmallIntegerField()
    card1 = models.SmallIntegerField()
    card2 = models.SmallIntegerField()
    card3 = models.SmallIntegerField()
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


class Friends(models.Model):
    char_id = models.ForeignKey(Char, on_delete=models.CASCADE, related_name='friend_char_id')
    friend_account = models.IntegerField()
    friend_id = models.ForeignKey(Char, on_delete=models.CASCADE, related_name='friend_id')

    class Meta:
        managed = False
        db_table = 'friends'


class Guild(models.Model):
    guild_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=24)
    char_id = models.ForeignKey(Char, on_delete=models.CASCADE, related_name='guild')
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


class GuildAlliance(models.Model):
    guild_id = models.ForeignKey(Guild, on_delete=models.CASCADE, related_name='guild_alliance')
    opposition = models.PositiveIntegerField()
    alliance_id = models.PositiveIntegerField()
    name = models.CharField(max_length=24)

    class Meta:
        managed = False
        db_table = 'guild_alliance'
        unique_together = (('guild_id', 'alliance_id'),)


class GuildCastle(models.Model):
    castle_id = models.PositiveIntegerField(primary_key=True)
    guild_id = models.ForeignKey(Guild, on_delete=models.CASCADE, related_name='guild_castle')
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
    guild_id = models.ForeignKey(Guild, on_delete=models.CASCADE, related_name='guild_expulsion')
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


class GuildStorage(models.Model):
    guild_id = models.ForeignKey(Guild, on_delete=models.CASCADE, related_name='guild_storage')
    nameid = models.PositiveIntegerField()
    amount = models.PositiveIntegerField()
    equip = models.PositiveIntegerField()
    identify = models.PositiveSmallIntegerField()
    refine = models.PositiveIntegerField()
    attribute = models.PositiveIntegerField()
    card0 = models.SmallIntegerField()
    card1 = models.SmallIntegerField()
    card2 = models.SmallIntegerField()
    card3 = models.SmallIntegerField()
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
        db_table = 'guild_storage'


class Homunculus(models.Model):
    homun_id = models.AutoField(primary_key=True)
    char_id = models.ForeignKey(Char, on_delete=models.CASCADE, related_name='homunculus')
    class_field = models.PositiveIntegerField(db_column='class')
    prev_class = models.IntegerField()
    name = models.CharField(max_length=24)
    level = models.SmallIntegerField()
    exp = models.IntegerField()
    intimacy = models.IntegerField()
    hunger = models.SmallIntegerField()
    str = models.PositiveSmallIntegerField()
    agi = models.PositiveSmallIntegerField()
    vit = models.PositiveSmallIntegerField()
    int = models.PositiveSmallIntegerField(db_column='INT')  # Field name made lowercase.
    dex = models.PositiveSmallIntegerField()
    luk = models.PositiveSmallIntegerField()
    hp = models.IntegerField()
    max_hp = models.IntegerField()
    sp = models.IntegerField()
    max_sp = models.IntegerField()
    skill_point = models.PositiveSmallIntegerField()
    alive = models.IntegerField()
    rename_flag = models.IntegerField()
    vaporize = models.IntegerField()
    autofeed = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'homunculus'


class Inventory(models.Model):
    char_id = models.ForeignKey(Char, on_delete=models.CASCADE, related_name='inventory')
    nameid = models.PositiveIntegerField()
    amount = models.PositiveIntegerField()
    equip = models.PositiveIntegerField()
    identify = models.SmallIntegerField()
    refine = models.PositiveIntegerField()
    attribute = models.PositiveIntegerField()
    card0 = models.SmallIntegerField()
    card1 = models.SmallIntegerField()
    card2 = models.SmallIntegerField()
    card3 = models.SmallIntegerField()
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
    favorite = models.PositiveIntegerField()
    bound = models.PositiveIntegerField()
    unique_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'inventory'


class Party(models.Model):
    party_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=24)
    exp = models.PositiveIntegerField()
    item = models.PositiveIntegerField()
    leader_id = models.PositiveIntegerField()
    leader_char = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'party'


class Pet(models.Model):
    pet_id = models.AutoField(primary_key=True)
    class_field = models.PositiveIntegerField(db_column='class')
    name = models.CharField(max_length=24)
    account_id = models.PositiveIntegerField()
    char_id = models.PositiveIntegerField()
    level = models.PositiveSmallIntegerField()
    egg_id = models.PositiveSmallIntegerField()
    equip = models.PositiveIntegerField()
    intimate = models.PositiveSmallIntegerField()
    hungry = models.PositiveSmallIntegerField()
    rename_flag = models.PositiveIntegerField()
    incubate = models.PositiveIntegerField()
    autofeed = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'pet'


class Quest(models.Model):
    char_id = models.PositiveIntegerField(primary_key=True)
    quest_id = models.PositiveIntegerField()
    state = models.CharField(max_length=1)
    time = models.PositiveIntegerField()
    count1 = models.PositiveIntegerField()
    count2 = models.PositiveIntegerField()
    count3 = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'quest'
        unique_together = (('char_id', 'quest_id'),)


class Storage(models.Model):
    account_id = models.ForeignKey(Login, on_delete=models.CASCADE, related_name='storage')
    nameid = models.PositiveIntegerField()
    amount = models.PositiveSmallIntegerField()
    equip = models.PositiveIntegerField()
    identify = models.PositiveSmallIntegerField()
    refine = models.PositiveIntegerField()
    attribute = models.PositiveIntegerField()
    card0 = models.SmallIntegerField()
    card1 = models.SmallIntegerField()
    card2 = models.SmallIntegerField()
    card3 = models.SmallIntegerField()
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
        db_table = 'storage'
