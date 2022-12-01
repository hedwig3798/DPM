class spec:
    def __init__(self):
        self.data = {
            "MAIN_STAT": 0,
            "SUB_STAT_1": 0,
            "SUB_STAT_2": 0,
            "HP": 0,
            "MP": 0,
            "FINAL_DMG": 100,
            "DMG": 0,
            "IGR": 0,
            "CRI_CMG": 0,
            "CRI_RATE": 0,
            "MAIN_STAT_P": 0,
            "ALL_STAT_P": 0,
        }

    def __add__(self, other):
        result = spec()
        for i in result.data.keys():
            if i == "IGR":
                result.data[i] = self.data[i] + ((100 - self.data[i]) * (other.data[i] * 0.01))
            elif i == "FINAL_DMG":
                result.data[i] = ((self.data[i] * 0.01) * ((100 + other.data[i]) * 0.01)) * 100
            else:
                result.data[i] = self.data[i] + other.data[i]
        return result


if __name__ == "__main__":
    # spec a + b

    a = spec()
    a.data["ATK"] = 10
    a.data["IGR"] = 50
    a.data["FINAL_DMG"] = 50

    b = spec()
    b.data["ATK"] = 10
    b.data["FINAL_DMG"] = 50
    b.data["IGR"] = 50

    c = a + b

    for i in c.data.keys():
        print(i + ": " + str(c.data[i]))
