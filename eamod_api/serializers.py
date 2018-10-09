from rest_framework import serializers

from . import models

from main_api import serializers as main_serializers


class CharWoeSkillCountSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SkillCount
        fields = ('char_id', 'skill_id', 'count', 'woe_date')


class CharBattlegroundsSkillCountSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BgSkillCount
        fields = ('char_id', 'skill_id', 'count')


class CharBattlegroundsSerializer(serializers.ModelSerializer):
    char_id = main_serializers.RankingCharacterSerializer()

    class Meta:
        model = models.CharBg
        fields = ('char_id', 'top_damage', 'damage_done', 'damage_received', 'skulls', 'ti_wins', 'ti_lost', 'ti_tie',
                  'eos_flags', 'eos_bases', 'eos_wins', 'eos_lost', 'eos_tie', 'boss_killed', 'boss_damage',
                  'boss_flags', 'boss_wins', 'boss_lost', 'boss_tie', 'dom_bases', 'dom_off_kills', 'dom_def_kills',
                  'dom_wins', 'dom_lost', 'dom_tie', 'td_kills', 'td_deaths', 'td_wins', 'td_lost', 'td_tie',
                  'sc_stole', 'sc_captured', 'sc_droped', 'sc_wins', 'sc_lost', 'sc_tie', 'ctf_taken', 'ctf_captured',
                  'ctf_droped', 'ctf_wins', 'ctf_lost', 'ctf_tie', 'emperium_kill', 'barricade_kill', 'gstone_kill',
                  'cq_wins', 'cq_lost', 'kill_count', 'death_count', 'win', 'lost', 'tie', 'leader_win', 'leader_lost',
                  'leader_tie', 'deserter', 'score', 'points', 'sp_heal_potions', 'hp_heal_potions', 'yellow_gemstones',
                  'red_gemstones', 'blue_gemstones', 'poison_bottles', 'acid_demostration', 'acid_demostration_fail',
                  'support_skills_used', 'healing_done', 'wrong_support_skills_used', 'wrong_healing_done', 'sp_used',
                  'zeny_used', 'spiritb_used', 'ammo_used', 'rank_points', 'rank_games', 'ru_captures', 'ru_wins',
                  'ru_lost')


class CharWoeSerializer(serializers.ModelSerializer):
    char_id = main_serializers.RankingCharacterSerializer()

    class Meta:
        model = models.CharWstats
        fields = ('char_id', 'kill_count', 'death_count', 'score', 'top_damage', 'damage_done', 'damage_received',
                  'emperium_damage', 'guardian_damage', 'barricade_damage', 'gstone_damage', 'emperium_kill',
                  'guardian_kill', 'barricade_kill', 'gstone_kill', 'sp_heal_potions', 'hp_heal_potions',
                  'yellow_gemstones', 'red_gemstones', 'blue_gemstones', 'poison_bottles', 'acid_demostration',
                  'acid_demostration_fail', 'support_skills_used', 'healing_done', 'wrong_support_skills_used',
                  'wrong_healing_done', 'sp_used', 'zeny_used', 'spiritb_used', 'ammo_used', 'woe_date')
