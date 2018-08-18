import importlib

from django.db import models

from alfheimproject.settings import CONFIG

core_models = importlib.import_module('core.{emu}.models'.format(emu=CONFIG['server']['conf']['emu_type']))


class CharBg(models.Model):
    char_id = models.OneToOneField(core_models.Char, on_delete=models.CASCADE, to_field='char_id',
                                   related_name='bg_char', primary_key=True, db_column='char_id')
    top_damage = models.IntegerField()
    damage_done = models.IntegerField()
    damage_received = models.IntegerField()
    skulls = models.IntegerField()
    ti_wins = models.IntegerField()
    ti_lost = models.IntegerField()
    ti_tie = models.IntegerField()
    eos_flags = models.IntegerField()
    eos_bases = models.IntegerField()
    eos_wins = models.IntegerField()
    eos_lost = models.IntegerField()
    eos_tie = models.IntegerField()
    boss_killed = models.IntegerField()
    boss_damage = models.IntegerField()
    boss_flags = models.IntegerField()
    boss_wins = models.IntegerField()
    boss_lost = models.IntegerField()
    boss_tie = models.IntegerField()
    dom_bases = models.IntegerField()
    dom_off_kills = models.IntegerField()
    dom_def_kills = models.IntegerField()
    dom_wins = models.IntegerField()
    dom_lost = models.IntegerField()
    dom_tie = models.IntegerField()
    td_kills = models.IntegerField()
    td_deaths = models.IntegerField()
    td_wins = models.IntegerField()
    td_lost = models.IntegerField()
    td_tie = models.IntegerField()
    sc_stole = models.IntegerField()
    sc_captured = models.IntegerField()
    sc_droped = models.IntegerField()
    sc_wins = models.IntegerField()
    sc_lost = models.IntegerField()
    sc_tie = models.IntegerField()
    ctf_taken = models.IntegerField()
    ctf_captured = models.IntegerField()
    ctf_droped = models.IntegerField()
    ctf_wins = models.IntegerField()
    ctf_lost = models.IntegerField()
    ctf_tie = models.IntegerField()
    emperium_kill = models.IntegerField()
    barricade_kill = models.IntegerField()
    gstone_kill = models.IntegerField()
    cq_wins = models.IntegerField()
    cq_lost = models.IntegerField()
    kill_count = models.IntegerField()
    death_count = models.IntegerField()
    win = models.IntegerField()
    lost = models.IntegerField()
    tie = models.IntegerField()
    leader_win = models.IntegerField()
    leader_lost = models.IntegerField()
    leader_tie = models.IntegerField()
    deserter = models.IntegerField()
    score = models.IntegerField()
    points = models.IntegerField()
    sp_heal_potions = models.IntegerField()
    hp_heal_potions = models.IntegerField()
    yellow_gemstones = models.IntegerField()
    red_gemstones = models.IntegerField()
    blue_gemstones = models.IntegerField()
    poison_bottles = models.IntegerField()
    acid_demostration = models.IntegerField()
    acid_demostration_fail = models.IntegerField()
    support_skills_used = models.IntegerField()
    healing_done = models.IntegerField()
    wrong_support_skills_used = models.IntegerField()
    wrong_healing_done = models.IntegerField()
    sp_used = models.IntegerField()
    zeny_used = models.IntegerField()
    spiritb_used = models.IntegerField()
    ammo_used = models.IntegerField()
    rank_points = models.IntegerField()
    rank_games = models.IntegerField()
    ru_captures = models.IntegerField()
    ru_wins = models.IntegerField()
    ru_lost = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'char_bg'

    def __str__(self):
        return self.char_id.name


class CharBgLog(models.Model):
    time = models.DateTimeField()
    killer = models.CharField(max_length=25)
    killer_id = models.ForeignKey(core_models.Char, on_delete=models.CASCADE, related_name='bg_killer')
    killed = models.CharField(max_length=25)
    killed_id = models.ForeignKey(core_models.Char, on_delete=models.CASCADE, related_name='bg_killed')
    map = models.CharField(max_length=11)
    skill = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'char_bg_log'


class CharWoeLog(models.Model):
    time = models.DateTimeField()
    killer = models.CharField(max_length=25)
    killer_id = models.ForeignKey(core_models.Char, on_delete=models.CASCADE, related_name='woe_killer')
    killed = models.CharField(max_length=25)
    killed_id = models.ForeignKey(core_models.Char, on_delete=models.CASCADE, related_name='woe_killed')
    map = models.CharField(max_length=11)
    skill = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'char_woe_log'


class CharWstats(models.Model):
    char_id = models.OneToOneField(core_models.Char, on_delete=models.CASCADE, to_field='char_id',
                                   related_name='woe_char', primary_key=True, db_column='char_id')
    kill_count = models.IntegerField()
    death_count = models.IntegerField()
    score = models.IntegerField()
    top_damage = models.IntegerField()
    damage_done = models.IntegerField()
    damage_received = models.IntegerField()
    emperium_damage = models.IntegerField()
    guardian_damage = models.IntegerField()
    barricade_damage = models.IntegerField()
    gstone_damage = models.IntegerField()
    emperium_kill = models.IntegerField()
    guardian_kill = models.IntegerField()
    barricade_kill = models.IntegerField()
    gstone_kill = models.IntegerField()
    sp_heal_potions = models.IntegerField()
    hp_heal_potions = models.IntegerField()
    yellow_gemstones = models.IntegerField()
    red_gemstones = models.IntegerField()
    blue_gemstones = models.IntegerField()
    poison_bottles = models.IntegerField()
    acid_demostration = models.IntegerField()
    acid_demostration_fail = models.IntegerField()
    support_skills_used = models.IntegerField()
    healing_done = models.IntegerField()
    wrong_support_skills_used = models.IntegerField()
    wrong_healing_done = models.IntegerField()
    sp_used = models.IntegerField()
    zeny_used = models.IntegerField()
    spiritb_used = models.IntegerField()
    ammo_used = models.IntegerField()
    woe_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'char_wstats'


class SkillCount(models.Model):
    char_id = models.OneToOneField(core_models.Char, on_delete=models.CASCADE, to_field='char_id',
                                   related_name='woe_skills', primary_key=True, db_column='char_id')
    skill_id = models.SmallIntegerField(db_column='id')
    count = models.IntegerField()
    woe_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'skill_count'


class BgSkillCount(models.Model):
    char_id = models.OneToOneField(core_models.Char, on_delete=models.CASCADE, to_field='char_id',
                                   related_name='bg_skills', primary_key=True, db_column='char_id')
    skill_id = models.SmallIntegerField(db_column='id')
    count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bg_skill_count'
