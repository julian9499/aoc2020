from pull import AocInteraction

STEPS = 32


class BluePrint:

    def __init__(self, id, oreBot, clayBot, obsBot, geoBot):
        self.id = id
        self.oreBot = oreBot
        self.clayBot = clayBot
        self.obsBot = obsBot
        self.geoBot = geoBot
        self.max_ore = max(oreBot, clayBot, obsBot[0], geoBot[0])

    def __repr__(self):
        return f"{self.id} {self.oreBot} {self.clayBot} {self.obsBot} {self.geoBot}"


#  https://adventofcode.com/2022/day/19

def part_1(advent_of_code, file_as_string_array):
    bluePrints = []

    for line in file_as_string_array:
        splitted = line.replace(":", "").split(" ")
        id = int(splitted[1])
        oreBot = int(splitted[6])
        clayBot = int(splitted[12])
        obsBot = [int(splitted[18]), int(splitted[21])] # ore, clay
        geoBot = [int(splitted[27]), int(splitted[30])] # ore, obs
        bluePrints.append(BluePrint(id, oreBot, clayBot, obsBot, geoBot))

    ans = []
    ans2 = 1

    for b in bluePrints:
        cache = {}
        t_max={i:0 for i in range(STEPS)}
        answer = qual(cache,t_max, b, 0, 0, 0, 0, 1, 0, 0, 0, 0)
        print(b, "->", answer)
        ans.append(answer * b.id)
        ans2 = ans2 * answer

    # print(sum(ans))
    
    # advent_of_code.answer(1, sum(ans))
    advent_of_code.answer(2, ans2)

def qual(cache, t_max, bluePrint, ore_cnt, clay_cnt, obs_cnt, geo_cnt, ore_bot, clay_bot, obs_bot, geo_bot, t):
    assert max(ore_bot, clay_bot, obs_bot, geo_bot) < 32
    assert max(ore_cnt, clay_cnt, obs_cnt) < 512
    assert geo_cnt < 128
    code = (t | ore_bot << 6 | (clay_bot << 11) | (obs_bot << 16) | (geo_bot << 21) |
            (ore_cnt << 26) | (clay_cnt << 35) | (obs_cnt << 44) | (geo_cnt << 53))
    if code in cache:
        return cache[code]
    if t == STEPS:
        return geo_cnt

    if geo_cnt < t_max[t] * 8 // 10:
        return -1

    t_max[t] = max(t_max[t], geo_cnt)

    n_ore_cnt = ore_cnt + ore_bot
    n_clay_cnt = clay_cnt + clay_bot
    n_obs_cnt = obs_cnt + obs_bot
    n_geo_cnt = geo_cnt + geo_bot

    maxg = 0

    if ore_cnt >= bluePrint.oreBot and ore_bot < bluePrint.max_ore:
        maxg = max(maxg, qual(cache, t_max, bluePrint, n_ore_cnt-bluePrint.oreBot, n_clay_cnt, n_obs_cnt, n_geo_cnt, ore_bot + 1, clay_bot, obs_bot, geo_bot, t+1))

    if ore_cnt >= bluePrint.clayBot and clay_bot < bluePrint.obsBot[1]:
        maxg = max(maxg, qual(cache, t_max, bluePrint, n_ore_cnt-bluePrint.clayBot, n_clay_cnt, n_obs_cnt, n_geo_cnt, ore_bot, clay_bot + 1, obs_bot, geo_bot, t+1))

    if ore_cnt >= bluePrint.obsBot[0] and clay_cnt >= bluePrint.obsBot[1] and obs_bot < bluePrint.geoBot[1]:
        maxg = max(maxg, qual(cache, t_max, bluePrint, n_ore_cnt-bluePrint.obsBot[0], n_clay_cnt-bluePrint.obsBot[1], n_obs_cnt, n_geo_cnt, ore_bot, clay_bot, obs_bot + 1, geo_bot, t+1))

    if ore_cnt >= bluePrint.geoBot[0] and obs_cnt >= bluePrint.geoBot[1]:
        maxg = max(maxg, qual(cache, t_max, bluePrint, n_ore_cnt-bluePrint.geoBot[0], n_clay_cnt, n_obs_cnt-bluePrint.geoBot[1], n_geo_cnt, ore_bot, clay_bot, obs_bot, geo_bot + 1, t+1))

    maxg = max(maxg, qual(cache, t_max, bluePrint, n_ore_cnt, n_clay_cnt, n_obs_cnt, n_geo_cnt, ore_bot, clay_bot, obs_bot, geo_bot, t+1))

    cache[code] = maxg
    return maxg

def part_2(advent_of_code, file_as_string_array):
    
    advent_of_code.answer(2, None)


if __name__ == "__main__":
    aoc_interaction = AocInteraction()
    file_as_string_array = [x.strip() for x in open('input.txt', 'r').readlines()]
    part_1(aoc_interaction, file_as_string_array)
    part_2(aoc_interaction, file_as_string_array)
