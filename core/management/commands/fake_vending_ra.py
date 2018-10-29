import random
import datetime
import importlib

from django.core.management.base import BaseCommand
from alfheimproject.settings import CONFIG

models = importlib.import_module('core.{emu}.models'.format(emu=CONFIG['server']['conf']['emu_type']))


class Command(BaseCommand):
    help = 'This command will generate random vending data'

    def add_arguments(self, parser):
        parser.add_argument(
            '--num',
            help='How much data generate?',
            type=int
        )

    def handle(self, *args, **options):
        num = options.get('num', 1)
        for char in range(num):
            item_id = random.randint(501, 520)
            char_id = random.randint(1111, 9999)

            account = models.Login.objects.get(account_id=1)
            chr1 = models.Char.objects.create(
                char_id=char_id,
                name='Test{char}'.format(char=char_id),
                account_id=account,
                char_num=0,
                class_field=5,
                base_level=0,
                job_level=0,
                base_exp=0,
                job_exp=0,
                zeny=0,
                str=0,
                agi=0,
                int=0,
                vit=0,
                dex=0,
                luk=0,
                max_hp=0,
                hp=0,
                max_sp=0,
                sp=0,
                status_point=0,
                skill_point=0,
                option=0,
                karma=0,
                manner=0,
                party_id=0,
                guild_id=0,
                pet_id=0,
                homun_id=0,
                elemental_id=0,
                hair=0,
                hair_color=0,
                clothes_color=0,
                body=0,
                weapon=0,
                shield=0,
                head_top=0,
                head_mid=0,
                head_bottom=0,
                robe=0,
                last_map=0,
                last_x=0,
                last_y=0,
                save_map=0,
                save_x=0,
                save_y=0,
                partner_id=0,
                online=0,
                father=0,
                mother=0,
                child=0,
                fame=0,
                rename=0,
                delete_date=0,
                moves=0,
                unban_time=0,
                font=0,
                uniqueitem_counter=0,
                sex=0,
                hotkey_rowshift=0,
                clan_id=0,
                last_login=datetime.datetime.now(),
                title_id=0,
                show_equip=0,
            )
            itm = models.ItemDb.objects.get(id=item_id)
            cart = models.CartInventory.objects.create(
                char_id=char_id,
                nameid=itm,
                refine=random.randint(0, 10),
                amount=random.randint(0, 10),
                equip=0,
                identify=0,
                attribute=0,
                card0_id=0,
                card1_id=0,
                card2_id=0,
                card3_id=0,
                option_id0=0,
                option_val0=0,
                option_parm0=0,
                option_id1=0,
                option_val1=0,
                option_parm1=0,
                option_id2=0,
                option_val2=0,
                option_parm2=0,
                option_id3=0,
                option_val3=0,
                option_parm3=0,
                option_id4=0,
                option_val4=0,
                option_parm4=0,
                expire_time=0,
                bound=0,
                unique_id=0,
            )
            vend = models.Vendings.objects.create(
                id=random.randint(33, 99999),
                char_id=chr1,
                title='Random{char}'.format(char=char_id),
                account_id=account.account_id,
                sex=0,
                map=0,
                x=0,
                y=0,
                body_direction=0,
                head_direction=0,
                sit=0,
                autotrade=0,
            )
            for x in range(4):
                models.AutotradeData.objects.create(
                    vending_id=vend,
                    index=random.randint(1111, 9999),
                    item=cart,
                    amount=random.randint(1, 20),
                    price=random.randint(11, 999)
                )
