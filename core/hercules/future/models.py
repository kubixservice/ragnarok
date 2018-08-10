from django.db import models

"""
    CURRENT MODELS NOT USED RIGHT NOW
    BUT WILL BE USED IN FUTURE
"""


class CharAchievements(models.Model):
    char_id = models.PositiveIntegerField(primary_key=True)
    ach_id = models.PositiveIntegerField()
    completed_at = models.PositiveIntegerField()
    rewarded_at = models.PositiveIntegerField()
    obj_0 = models.PositiveIntegerField()
    obj_1 = models.PositiveIntegerField()
    obj_2 = models.PositiveIntegerField()
    obj_3 = models.PositiveIntegerField()
    obj_4 = models.PositiveIntegerField()
    obj_5 = models.PositiveIntegerField()
    obj_6 = models.PositiveIntegerField()
    obj_7 = models.PositiveIntegerField()
    obj_8 = models.PositiveIntegerField()
    obj_9 = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'char_achievements'
        unique_together = (('char_id', 'ach_id'),)


class AutotradeData(models.Model):
    char_id = models.IntegerField(primary_key=True)
    itemkey = models.IntegerField()
    amount = models.IntegerField()
    price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'autotrade_data'
        unique_together = (('char_id', 'itemkey'),)


class AutotradeMerchants(models.Model):
    account_id = models.IntegerField(primary_key=True)
    char_id = models.IntegerField()
    sex = models.IntegerField()
    title = models.CharField(max_length=80)

    class Meta:
        managed = False
        db_table = 'autotrade_merchants'
        unique_together = (('account_id', 'char_id'),)


class AccRegNumDb(models.Model):
    account_id = models.PositiveIntegerField(primary_key=True)
    key = models.CharField(max_length=32)
    index = models.PositiveIntegerField()
    value = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'acc_reg_num_db'
        unique_together = (('account_id', 'key', 'index'),)


class AccRegStrDb(models.Model):
    account_id = models.PositiveIntegerField(primary_key=True)
    key = models.CharField(max_length=32)
    index = models.PositiveIntegerField()
    value = models.CharField(max_length=254)

    class Meta:
        managed = False
        db_table = 'acc_reg_str_db'
        unique_together = (('account_id', 'key', 'index'),)


class AccountData(models.Model):
    account_id = models.PositiveIntegerField(primary_key=True)
    bank_vault = models.PositiveIntegerField()
    base_exp = models.PositiveSmallIntegerField()
    base_drop = models.PositiveSmallIntegerField()
    base_death = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'account_data'


class Auction(models.Model):
    auction_id = models.BigAutoField(primary_key=True)
    seller_id = models.PositiveIntegerField()
    seller_name = models.CharField(max_length=30)
    buyer_id = models.PositiveIntegerField()
    buyer_name = models.CharField(max_length=30)
    price = models.PositiveIntegerField()
    buynow = models.PositiveIntegerField()
    hours = models.SmallIntegerField()
    timestamp = models.PositiveIntegerField()
    nameid = models.PositiveIntegerField()
    item_name = models.CharField(max_length=50)
    type = models.SmallIntegerField()
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
    unique_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'auction'


class CharRegNumDb(models.Model):
    char_id = models.PositiveIntegerField(primary_key=True)
    key = models.CharField(max_length=32)
    index = models.PositiveIntegerField()
    value = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'char_reg_num_db'
        unique_together = (('char_id', 'key', 'index'),)


class CharRegStrDb(models.Model):
    char_id = models.PositiveIntegerField(primary_key=True)
    key = models.CharField(max_length=32)
    index = models.PositiveIntegerField()
    value = models.CharField(max_length=254)

    class Meta:
        managed = False
        db_table = 'char_reg_str_db'
        unique_together = (('char_id', 'key', 'index'),)


class Charlog(models.Model):
    time = models.DateTimeField(blank=True, null=True)
    char_msg = models.CharField(max_length=255)
    account_id = models.IntegerField()
    char_id = models.PositiveIntegerField()
    char_num = models.IntegerField()
    class_field = models.IntegerField(db_column='class')  # Field renamed because it was a Python reserved word.
    name = models.CharField(max_length=23)
    str = models.PositiveIntegerField()
    agi = models.PositiveIntegerField()
    vit = models.PositiveIntegerField()
    int = models.PositiveIntegerField(db_column='INT')  # Field name made lowercase.
    dex = models.PositiveIntegerField()
    luk = models.PositiveIntegerField()
    hair = models.IntegerField()
    hair_color = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'charlog'


class Elemental(models.Model):
    ele_id = models.AutoField(primary_key=True)
    char_id = models.IntegerField()
    class_field = models.PositiveIntegerField(db_column='class')  # Field renamed because it was a Python reserved word.
    mode = models.PositiveIntegerField()
    hp = models.IntegerField()
    sp = models.IntegerField()
    max_hp = models.PositiveIntegerField()
    max_sp = models.PositiveIntegerField()
    atk1 = models.PositiveIntegerField()
    atk2 = models.PositiveIntegerField()
    matk = models.PositiveIntegerField()
    aspd = models.PositiveSmallIntegerField()
    def_field = models.PositiveSmallIntegerField(
        db_column='def')  # Field renamed because it was a Python reserved word.
    mdef = models.PositiveSmallIntegerField()
    flee = models.PositiveSmallIntegerField()
    hit = models.PositiveSmallIntegerField()
    life_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'elemental'


class GlobalAccRegNumDb(models.Model):
    account_id = models.PositiveIntegerField(primary_key=True)
    key = models.CharField(max_length=32)
    index = models.PositiveIntegerField()
    value = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'global_acc_reg_num_db'
        unique_together = (('account_id', 'key', 'index'),)


class GlobalAccRegStrDb(models.Model):
    account_id = models.PositiveIntegerField(primary_key=True)
    key = models.CharField(max_length=32)
    index = models.PositiveIntegerField()
    value = models.CharField(max_length=254)

    class Meta:
        managed = False
        db_table = 'global_acc_reg_str_db'
        unique_together = (('account_id', 'key', 'index'),)


class Hotkey(models.Model):
    char_id = models.IntegerField(primary_key=True)
    hotkey = models.PositiveIntegerField()
    type = models.PositiveIntegerField()
    itemskill_id = models.PositiveIntegerField()
    skill_lvl = models.PositiveIntegerField()

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


class Ipbanlist(models.Model):
    list = models.CharField(max_length=100)
    btime = models.DateTimeField(blank=True, null=True)
    rtime = models.DateTimeField(blank=True, null=True)
    reason = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ipbanlist'


class Mail(models.Model):
    id = models.BigAutoField(primary_key=True)
    send_name = models.CharField(max_length=30)
    send_id = models.PositiveIntegerField()
    dest_name = models.CharField(max_length=30)
    dest_id = models.PositiveIntegerField()
    title = models.CharField(max_length=45)
    message = models.CharField(max_length=255)
    time = models.PositiveIntegerField()
    status = models.IntegerField()
    zeny = models.PositiveIntegerField()
    nameid = models.PositiveIntegerField()
    amount = models.PositiveIntegerField()
    refine = models.PositiveIntegerField()
    attribute = models.PositiveIntegerField()
    identify = models.SmallIntegerField()
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
    unique_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mail'


class Mapreg(models.Model):
    varname = models.CharField(primary_key=True, max_length=32)
    index = models.PositiveIntegerField()
    value = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'mapreg'
        unique_together = (('varname', 'index'),)


class Memo(models.Model):
    memo_id = models.AutoField(primary_key=True)
    char_id = models.PositiveIntegerField()
    map = models.CharField(max_length=11)
    x = models.PositiveSmallIntegerField()
    y = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'memo'


class Mercenary(models.Model):
    mer_id = models.AutoField(primary_key=True)
    char_id = models.IntegerField()
    class_field = models.PositiveIntegerField(db_column='class')
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


class NpcMarketData(models.Model):
    name = models.CharField(primary_key=True, max_length=24)
    itemid = models.PositiveIntegerField()
    amount = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'npc_market_data'
        unique_together = (('name', 'itemid'),)


class Ragsrvinfo(models.Model):
    index = models.IntegerField()
    name = models.CharField(max_length=255)
    exp = models.PositiveIntegerField()
    jexp = models.PositiveIntegerField()
    drop = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ragsrvinfo'


class RodexItems(models.Model):
    mail_id = models.BigIntegerField()
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
        db_table = 'rodex_items'


class RodexMail(models.Model):
    mail_id = models.BigAutoField(primary_key=True)
    sender_name = models.CharField(max_length=30)
    sender_id = models.IntegerField()
    receiver_name = models.CharField(max_length=30)
    receiver_id = models.IntegerField()
    receiver_accountid = models.IntegerField()
    title = models.CharField(max_length=50)
    body = models.CharField(max_length=510)
    zeny = models.BigIntegerField()
    type = models.PositiveIntegerField()
    is_read = models.IntegerField()
    sender_read = models.IntegerField()
    send_date = models.IntegerField()
    expire_date = models.IntegerField()
    weight = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'rodex_mail'


class ScData(models.Model):
    account_id = models.PositiveIntegerField(primary_key=True)
    char_id = models.PositiveIntegerField()
    type = models.PositiveSmallIntegerField()
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
    char_id = models.PositiveIntegerField(primary_key=True)
    id = models.PositiveSmallIntegerField()
    lv = models.PositiveIntegerField()
    flag = models.PositiveIntegerField()

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
    timestamp = models.PositiveIntegerField(primary_key=True)
    ignored = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'sql_updates'
