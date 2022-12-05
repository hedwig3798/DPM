import math
import csv


class equip:

    # def __init__(self, name, part, level, main_stat, sub_stat_1, sub_stat_2, hp, atk, atk_p, atk_sub, main_stat_p,
    #              all_stat_p, upgrade,
    #              option, set_option, superior, gard_ignore, boss_dmg, cri_rate, cri_dmg):
    #     self.name = name  # string
    #     self.part = part  # string we: weapon ar: armor ac: accessories gl: glove
    #     self.level = level  # int
    #     self.main_stat = main_stat  # int
    #     self.sub_stat_1 = sub_stat_1  # int
    #     self.sub_stat_2 = sub_stat_2  # int
    #     self.hp = hp  # int
    #     self.atk = atk  # int
    #     self.atk_p = atk_p  # int
    #     self.atk_sub = atk_sub  # int
    #     self.main_stat_p = main_stat_p  # int
    #     self.all_stat_p = all_stat_p  # int
    #     self.upgrade = upgrade  # int
    #     self.option = option  # int
    #     self.set_option = set_option  # int
    #     self.superior = superior  # int
    #     self.gard_ignore = gard_ignore  # float
    #     self.boss_dmg = boss_dmg  # int
    #     self.cri_rate = cri_rate  # int
    #     self.cri_dmg = cri_dmg  # int
    #
    #     self.init_main_stat = main_stat  # int
    #     self.init_sub_stat_1 = sub_stat_1  # int
    #     self.init_sub_stat_2 = sub_stat_2  # int
    #     self.init_hp = hp  # int
    #     self.init_atk = atk  # int
    #     self.init_atk_sub = atk_sub  # int
    #     self.init_all_stat_p = all_stat_p  # int

    def __init__(self, ele_list):
        self.name = ele_list[0].strip()  # string
        self.part = ele_list[1].strip()   # string we: weapon ar: armor ac: accessories gl: glove
        self.level = int(ele_list[2])  # int
        self.main_stat = int(ele_list[3])  # int
        self.sub_stat_1 = int(ele_list[4])  # int
        self.sub_stat_2 = int(ele_list[5])  # int
        self.hp = int(ele_list[6])  # int
        self.atk = int(ele_list[7])  # int
        self.atk_p = int(ele_list[8])  # int
        self.atk_sub = int(ele_list[9])  # int
        self.main_stat_p = int(ele_list[10])  # int
        self.all_stat_p = int(ele_list[11])  # int
        self.upgrade = int(ele_list[12])  # int
        self.option = True if ele_list[13].strip() == "True" else False  # bool
        self.set_option = ele_list[14].strip()   # string
        self.superior = True if ele_list[15].strip() == "True" else False # bool
        self.gard_ignore = float(ele_list[16])  # float
        self.boss_dmg = int(ele_list[17])  # int
        self.cri_rate = int(ele_list[18])  # int
        self.cri_dmg = int(ele_list[19])  # int

        self.init_main_stat = int(ele_list[3])  # int
        self.init_sub_stat_1 = int(ele_list[4])  # int
        self.init_sub_stat_2 = int(ele_list[5])  # int
        self.init_hp = int(ele_list[6])  # int
        self.init_atk = int(ele_list[7])  # int
        self.init_atk_sub = int(ele_list[9])  # int
        self.init_all_stat_p = int(ele_list[11])  # int

    def add_main_stat(self, stat):
        self.main_stat += stat

    def add_all_stat(self, stat):
        self.main_stat += stat
        self.sub_stat_1 += stat
        self.sub_stat_2 += stat

    def add_atk(self, stat):
        self.atk += stat

    def add_all_atk(self, stat):
        self.atk += stat
        self.atk_sub += stat

    # 주문의 흔적 강화 (최고 단계 기준) (데벤져, 제논 제외)
    def scroll_upgrade(self):
        # 무기강화
        if self.part == "we":

            self.add_atk(self.upgrade * 9)
            self.add_main_stat(self.upgrade * 4)

        # 방어구 강화 (장갑제외)
        elif self.part == "ar":
            self.add_main_stat(self.upgrade * 7)
            if self.upgrade >= 4:
                self.add_atk(1)

        # 장신구 강화
        elif self.part == "ac":
            self.add_main_stat(self.upgrade * 5)

        # 장갑 강화
        elif self.part == "gl":
            self.add_atk(self.upgrade * 3)

    # 놀긍혼 (6 3 작 기준)
    def chaos_upgrade(self):
        self.add_atk(self.upgrade * 6)
        self.add_main_stat(self.upgrade * 3)

    # 에픽 9퍼 공10
    def epic_potential(self):
        if self.part != "we":
            self.main_stat_p += 9
            self.add_atk(10)

        elif self.part == "we":
            self.atk_p += 9
            self.add_atk(10)

    # 유니크 정옵 2줄 공 10
    def unique_potential(self):
        if self.part != "we":
            self.main_stat_p += 15
            self.add_atk(10)

        elif self.part == "we":
            self.atk_p += 15
            self.add_atk(10)

    # 방어구: 12 9 9 / 7 5 5
    # 무기, 장갑 별도 계산
    def legendary_potential(self):
        if self.part == "ar" or self.part == "ac":
            self.main_stat_p += 30 + 17

    # 스타포스 22성 적용
    def star_force(self):
        if self.superior:
            return
        if self.part == "ar" or self.part == "ac" or self.part == "gl":

            if self.level == 130:
                self.add_all_atk(45)
                self.add_all_stat(75)

            elif self.level == 140:
                self.add_all_atk(78)
                self.add_all_stat(103)

            elif self.level == 150:
                self.add_all_atk(85)
                self.add_all_stat(117)

            elif self.level == 160:
                self.add_all_atk(92)
                self.add_all_stat(131)

            elif self.level == 200:
                self.add_all_atk(106)
                self.add_all_stat(145)

            if self.part == "gl":
                self.add_atk(7)

        elif self.part == "we":

            for i in range(15):
                self.add_atk(self.atk//50 + 1)
                self.atk_sub += self.atk_sub//50 + 1

            if self.level == 130:
                self.add_all_atk(37)
                self.add_all_stat(75)

            elif self.level == 140:
                self.add_all_atk(65)
                self.add_all_stat(103)

            elif self.level == 150:
                self.add_all_atk(85)
                self.add_all_stat(117)

            elif self.level == 160:
                self.add_all_atk(78)
                self.add_all_stat(131)

            elif self.level == 200:
                self.add_all_atk(102)
                self.add_all_stat(145)

    # 탈벨 강화 12성
    def star_force_superior(self):
        self.add_all_atk(87)
        self.add_all_stat(115)

    def option_stat(self):
        if not self.option:
            return
        else:
            if self.part == "we":
                self.add_atk(math.ceil((self.init_atk/100) * (self.level//40 + 1) * 7 * (1.1 ** 4)))
                self.boss_dmg += 21
                self.all_stat_p += 7
            else:
                self.all_stat_p += 7
                self.add_main_stat((self.level//20 + 1) * 7)
                self.add_main_stat((self.level//40 + 1) * 7)
                self.add_all_stat((self.level//40 + 1) * 7)

    def total_upgrade(self):
        self.scroll_upgrade()
        self.star_force()
        self.option_stat()
        self.legendary_potential()

    def __repr__(self):
        result = ""
        result += f"이름: {self.name} \n"
        result += f"파츠: {self.part} \n"
        result += f"주스텟: {self.main_stat} {self.init_main_stat} {self.main_stat - self.init_main_stat}\n"
        result += f"부스텟 1: {self.sub_stat_1} {self.init_sub_stat_1} {self.sub_stat_1 - self.init_sub_stat_1}\n"
        result += f"부스텟 2: {self.sub_stat_2} {self.init_sub_stat_2} {self.sub_stat_2 - self.init_sub_stat_2} \n"
        result += f"HP: {self.hp} {self.init_hp} {self.hp - self.init_hp}\n"
        result += f"공: {self.atk} {self.init_atk} {self.atk - self.init_atk}\n"
        result += f"공퍼: {self.atk_p} \n"
        result += f"서브공: {self.atk_sub} {self.init_atk_sub} {self.atk_sub - self.init_atk_sub}\n"
        result += f"주스펫 퍼: {self.main_stat_p} \n"
        result += f"올스텟 퍼: {self.all_stat_p} {self.init_all_stat_p} \n"
        result += f"업횟: {self.upgrade} \n"
        result += f"추옵 가능: {self.option} \n"
        result += f"세트 옵션: {self.set_option} \n"
        result += f"슈페리얼: {self.superior} \n"
        return result


# name, part, level, main_stat, sub_stat_1, sub_stat_2, hp, atk, atk_p, atk_sub, main_stat_p, all_stat_p, upgrade,
# option, set_option, superior, gard_ignore, boss_dmg, cri_rate, cri_dmg
if __name__ == "__main__":
    f = open('item_data.csv', 'r', encoding='utf-8')
    rdr = csv.reader(f)

    # g_wand = equip("g_wand", "we", 200, 150, 150, 0, 0, 400, 237, 0, 0, 0, 8, True, "Lucky", False, 20, 30, 0, 0)
    # g_wand.total_upgrade()
    # print(g_wand)

    for i in rdr:
        if i[0] == "g_wand":
            g_wand_list = equip(i)
            print(g_wand_list)
            g_wand_list.total_upgrade()
            print(g_wand_list)
            break

    f.close()

