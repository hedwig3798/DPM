from math import trunc, ceil


class spec:

    # 캐릭터의 스펙을 저장하는 곳 ( 스텟 창 기중 )
    def __init__(self):
        self.level = 0  # 정수
        self.pure_stat = 0  # 정수
        self.hp = 0  # 정수
        self.mp = 0  # 정수

        self.final_dmg = 0  # 퍼센트
        self.dmg = 0  # 퍼센트
        self.boss_dmg = 0  # 퍼센트
        self.igr = 0  # 퍼센트
        self.cri_dmg = 0  # 퍼센트
        self.cri_rate = 0  # 퍼센트
        self.main_stat_p = 0  # 퍼센트
        self.all_stat_p = 0  # 퍼센트
        self.mystery = 0
        self.atk = 0
        self.atk_p = 0
        self.atk_sub = 0

        self.display_stat_atk = 0
        self.boss_stat_atk = 0
        self.main_stat = 0  # 정수
        self.sub_stat_1 = 4  # 정수
        self.sub_stat_2 = 4  # 정수

        self.add_main_stat = 0
        self.add_sub_stat_1 = 0
        self.add_sub_stat_2 = 0

        self.weapon_ab = 0
        self.job_ab = 0

    def set_level(self, num):
        self.level = num
        self.pure_stat = 14 + (num * 5)

    def add_final_dmg(self, num):
        temp = self.final_dmg + 1
        temp *= 1 + num
        self.final_dmg = temp - 1
        # self.final_dmg = round(self.final_dmg, 4)

    def add_igr(self, num):
        self.igr += (1 - self.igr) * num

    def sub_final_dmg(self, num):
        temp = self.final_dmg + 1
        temp /= 1 + num
        self.final_dmg = temp - 1
        # self.final_dmg = round(self.final_dmg, 4)

    def sub_igr(self, num):
        self.igr = (1 - self.igr) / num

    def change_stat_atk(self):
        cal_stat = ((self.pure_stat + self.main_stat) * (1 + self.main_stat_p + self.all_stat_p)) + self.add_main_stat
        cal_stat *= 0.01
        cal_stat = trunc(cal_stat)

        self.display_stat_atk = cal_stat * self.atk * (1 + self.atk_p) * self.weapon_ab * self.job_ab * (1 + self.dmg) * (1 + self.final_dmg)

    def __repr__(self):
        result = ""
        result += f"레벨: {self.level} \n"
        result += f"순스텟: {self.pure_stat} \n"
        result += f"주스텟: {self.main_stat}\n"
        result += f"주스텟( %미적용 ): {self.add_main_stat}\n"
        result += f"부스텟 1: {self.sub_stat_1}\n"
        result += f"부스텟 2: {self.sub_stat_2}\n"
        result += f"HP: {self.hp}\n"
        result += f"공: {self.atk}\n"
        result += f"공퍼: {self.atk_p} \n"
        result += f"서브공: {self.atk_sub}\n"
        result += f"주스펫 퍼: {self.main_stat_p} \n"
        result += f"올스텟 퍼: {self.all_stat_p}\n"
        result += f"방무: {self.igr} \n"
        result += f"보공: {self.boss_dmg} \n"
        result += f"데미지: {self.dmg} \n"
        result += f"최종뎀: {self.final_dmg} \n"
        result += f"뒷스공: {self.display_stat_atk} \n"
        return result


if __name__ == "__main__":
    a = spec()
    a.set_level(270)
    print(a)

