import math
import csv


class equip:

    # 아이템 만들고 강화까지 하게 함
    def __init__(self, name):

        self.main_stat = list(0 for _ in range(4))  # int
        self.sub_stat_1 = list(0 for _ in range(4))  # int
        self.sub_stat_2 = list(0 for _ in range(4))  # int
        self.hp = list(0 for _ in range(4))  # int
        self.atk = list(0 for _ in range(4))  # int
        self.atk_p = list(0 for _ in range(4))  # int
        self.atk_sub = list(0 for _ in range(4))  # int
        self.main_stat_p = list(0 for _ in range(4))  # int
        self.all_stat_p = list(0 for _ in range(4))  # int
        self.gard_ignore = list(0.0 for _ in range(4))  # float
        self.boss_dmg = list(0 for _ in range(4))  # int
        self.cri_rate = list(0 for _ in range(4))  # int
        self.cri_dmg = list(0 for _ in range(4))  # int

        ele_list = []
        f = open('item_data.csv', 'r', encoding='utf-8')
        rdr = csv.reader(f)
        for item in rdr:
            if item[0] == name:
                ele_list = item
                break
        f.close()

        self.name = ele_list[0].strip()  # string
        self.part = ele_list[1].strip()     # string we: weapon ar: armor ac: accessories gl: glove
        self.level = int(ele_list[2])  # int
        self.main_stat[0] = int(ele_list[3])  # int
        self.sub_stat_1[0] = int(ele_list[4])  # int
        self.sub_stat_2[0] = int(ele_list[5])  # int
        self.hp[0] = int(ele_list[6])  # int
        self.atk[0] = int(ele_list[7])  # int
        self.atk_p[0] = int(ele_list[8])  # int
        self.atk_sub[0] = int(ele_list[9])  # int
        self.main_stat_p[0] = int(ele_list[10])  # int
        self.all_stat_p[0] = int(ele_list[11])  # int
        self.upgrade = int(ele_list[12])  # int
        self.option = True if ele_list[13].strip() == "True" else False  # bool
        self.set_option = ele_list[14].strip()   # string
        self.superior = True if ele_list[15].strip() == "True" else False # bool
        self.gard_ignore[0] = float(ele_list[16])  # float
        self.boss_dmg[0] = int(ele_list[17])  # int
        self.cri_rate[0] = int(ele_list[18])  # int
        self.cri_dmg[0] = int(ele_list[19])  # int
        self.total_upgrade()

    # 주문의 흔적 강화 (최고 단계 기준) (데벤져, 제논 제외)
    def scroll_upgrade(self):
        # 무기강화
        if self.part == "we":
            self.atk[1] += self.upgrade * 9
            self.main_stat[1] += self.upgrade * 4

        # 방어구 강화 (장갑제외)
        elif self.part == "ar":
            self.main_stat[1] += self.upgrade * 7
            if self.upgrade >= 4:
                self.atk[1] += 1

        # 장신구 강화
        elif self.part == "ac":
            self.main_stat[1] += self.upgrade * 5

        # 장갑 강화
        elif self.part == "gl":
            self.atk[1] += self.upgrade * 3

    # 놀긍혼 (6 3 작 기준)
    def chaos_upgrade(self):
        self.atk[1] += self.upgrade * 6
        self.main_stat[1] += self.upgrade * 3

    # 에픽 9퍼 공10
    def epic_potential(self):
        if self.part != "we":
            self.main_stat_p[3] += 9
            self.atk[3] += 10

        elif self.part == "we":
            self.atk_p[3] += 9
            self.atk[3] += 10

    # 유니크 정옵 2줄 공 10
    def unique_potential(self):
        if self.part != "we":
            self.main_stat_p[3] += 15
            self.atk[3] += 10

        elif self.part == "we":
            self.atk_p[3] += 15
            self.atk[3] += 10

    # 방어구: 12 9 9 / 7 5 5
    # 무기, 장갑 별도 계산
    def legendary_potential(self):
        if self.part == "ar" or self.part == "ac":
            self.main_stat_p[3] += 30 + 17

    # 스타포스 22성 적용
    def star_force(self):
        if self.superior:
            return
        if self.part == "ar" or self.part == "ac" or self.part == "gl":

            if self.level == 130:
                self.atk[1] += 45
                self.atk_sub[1] += 45
                self.main_stat[1] += 75
                self.sub_stat_1[1] += 75
                self.sub_stat_2[1] += 75

            elif self.level == 140:
                self.atk[1] += 78
                self.atk_sub[1] += 78
                self.main_stat[1] += 103
                self.sub_stat_1[1] += 103
                self.sub_stat_2[1] += 103

            elif self.level == 150:
                self.atk[1] += 85
                self.atk_sub[1] += 85
                self.main_stat[1] += 117
                self.sub_stat_1[1] += 117
                self.sub_stat_2[1] += 117

            elif self.level == 160:
                self.atk[1] += 92
                self.atk_sub[1] += 92
                self.main_stat[1] += 131
                self.sub_stat_1[1] += 131
                self.sub_stat_2[1] += 131

            elif self.level == 200:
                self.atk[1] += 106
                self.atk_sub[1] += 106
                self.main_stat[1] += 145
                self.sub_stat_1[1] += 145
                self.sub_stat_2[1] += 145

            if self.part == "gl":
                self.atk[1] += 7

        elif self.part == "we":

            for i in range(15):
                self.atk[1] += sum(self.atk)//50 + 1
                self.atk_sub[1] += sum(self.atk_sub)//50 + 1

            if self.level == 130:
                self.atk[1] += 37
                self.atk_sub[1] += 37
                self.main_stat[1] += 75
                self.sub_stat_1[1] += 75
                self.sub_stat_2[1] += 75

            elif self.level == 140:
                self.atk[1] += 65
                self.atk_sub[1] += 65
                self.main_stat[1] += 103
                self.sub_stat_1[1] += 103
                self.sub_stat_2[1] += 103

            elif self.level == 150:
                self.atk[1] += 85
                self.atk_sub[1] += 85
                self.main_stat[1] += 117
                self.sub_stat_1[1] += 117
                self.sub_stat_2[1] += 117

            elif self.level == 160:
                self.atk[1] += 78
                self.atk_sub[1] += 78
                self.main_stat[1] += 131
                self.sub_stat_1[1] += 131
                self.sub_stat_2[1] += 131

            elif self.level == 200:
                self.atk[1] += 102
                self.atk_sub[1] += 102
                self.main_stat[1] += 145
                self.sub_stat_1[1] += 145
                self.sub_stat_2[1] += 145

    # 탈벨 강화 12성
    def star_force_superior(self):
        self.atk[1] += 87
        self.atk_sub[1] += 87
        self.main_stat[1] += 115
        self.sub_stat_1[1] += 115
        self.sub_stat_2[1] += 115

    def option_stat(self):
        if not self.option:
            return
        else:
            if self.part == "we":
                self.atk[2] += (math.ceil((self.atk[0]/100) * (self.level//40 + 1) * 7 * (1.1 ** 4)))
                self.boss_dmg[2] += 21
                self.all_stat_p[2] += 7
            else:
                self.all_stat_p[2] += 7
                self.main_stat[2] += ((self.level//20 + 1) * 7)
                self.main_stat[2] += ((self.level//40 + 1) * 7)
                self.sub_stat_1[2] += ((self.level//40 + 1) * 7)
                self.sub_stat_2[2] += ((self.level // 40 + 1) * 7)

    def total_upgrade(self):
        if self.part == "we":
            self.scroll_upgrade()
        else:
            self.chaos_upgrade()
        self.star_force()
        self.option_stat()
        self.legendary_potential()

    def __repr__(self):
        result = ""
        result += f"이름: {self.name} \n"
        result += f"파츠: {self.part} \n"
        result += f"주스텟: {sum(self.main_stat)} {self.main_stat} \n"
        result += f"부스텟 1: {sum(self.sub_stat_1)} {self.sub_stat_1}\n"
        result += f"부스텟 2: {sum(self.sub_stat_2)} {self.sub_stat_2}\n"
        result += f"HP: {sum(self.hp)} {self.hp}\n"
        result += f"공: {sum(self.atk)} {self.atk}\n"
        result += f"공퍼: {sum(self.atk_p)} {self.atk_p}\n"
        result += f"서브공: {sum(self.atk_sub)} {self.atk_sub}\n"
        result += f"주스펫 퍼: {sum(self.main_stat_p)} {self.main_stat_p}\n"
        result += f"올스텟 퍼: {sum(self.all_stat_p)} {self.all_stat_p}\n"
        result += f"보공: {sum(self.boss_dmg)} {self.boss_dmg}\n"
        result += f"방무: {sum(self.gard_ignore)} {self.gard_ignore}\n"
        result += f"업횟: {self.upgrade} \n"
        result += f"추옵 가능: {self.option} \n"
        result += f"세트 옵션: {self.set_option} \n"
        result += f"슈페리얼: {self.superior} \n"
        return result


# name, part, level, main_stat, sub_stat_1, sub_stat_2, hp, atk, atk_p, atk_sub, main_stat_p, all_stat_p, upgrade,
# option, set_option, superior, gard_ignore, boss_dmg, cri_rate, cri_dmg
if __name__ == "__main__":
    g_wand = equip("maister_ring")
    print(g_wand)



