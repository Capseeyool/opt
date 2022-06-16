import os
import requests
import sqlite3
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ['API_KEY']
TOKEN = os.environ['TOKEN']

def insert_pool(tournament, ids, mods=[6, 3, 3, 4, 3, 0, 0, 1]):
    mods = [f'{i[0]}{j}' for i in [i for i in list(zip(['NM', 'HD', 'HR', 'DT', 'FM', 'EZ', 'HT', 'TB'], mods))] for j in range(1, i[1] + 1)]
    for i in zip(mods, ids):
        try:
            r = requests.get(f'https://osu.ppy.sh/api/get_beatmaps?k={API_KEY}&b={i[1]}&m=0').json()[0]
            cur.execute(f'''INSERT INTO db VALUES (
                \'{tournament}\',
                \'{i[0]}\',
                {i[1]},
                \'{r["artist"].replace("'", "''")}\',
                \'{r["title"].replace("'", "''")}\',
                \'{r["version"].replace("'", "''")}\',
                {round(float(r["difficultyrating"]), 2)},
                {r["total_length"]},
                {r["max_combo"]},
                {r["bpm"]},
                {r["diff_size"]},
                {r["diff_approach"]},
                {r["diff_overall"]},
                {r["beatmapset_id"]}
            )''')
        except Exception as e:
            print(e)

if __name__ == '__main__':
    start = datetime.now()

    if os.path.exists('db.db'):
        os.remove('db.db')

    con = sqlite3.connect('db.db')
    cur = con.cursor()

    cur.execute('''CREATE TABLE db (
        tournament VARCHAR(255) NOT NULL,
        mod VARCHAR(3) NOT NULL,
        ID INT NOT NULL,
        artist VARCHAR(255),
        title VARCHAR(255),
        diff VARCHAR(255),
        SR FLOAT,
        length INT,
        combo INT,
        BPM INT,
        CS FLOAT,
        AR FLOAT,
        OD FLOAT,
        beatmapsetID INT,
        PRIMARY KEY(tournament, mod)
    )''')

    insert_pool('OWC 2021 GF',
    [3333705, 3333669, 3333699, 3333703, 3333700, 3333701, 3145691, 3333793, 3333706, 3081546, 3331199, 3333660, 3333570, 3333586, 3333770, 3333734, 3333729, 3333760, 3333738, 3333745])
    insert_pool('OWC 2021 Finals',
    [2675756, 3322513, 3322521, 3322526, 3322566, 3322093, 2856086, 3322576, 2633747, 438187, 2947341, 3322603, 3320894, 3322598, 859667, 3322610, 3322611, 2643166, 3322445, 3322616])
    insert_pool('OWC 2021 SF',
    [3311170, 3310526, 3311309, 3311337, 3311312, 3311313, 3311238, 3311073, 2267887, 861381, 3311344, 3311036, 2643135, 3311366, 277274, 3311356, 3311891, 3311383, 3311376, 3311391])
    insert_pool('OWC 2021 QF',
    [3299389, 3299406, 3299411, 1722011, 3297498, 3299412, 1843575, 2623967, 546944, 2633812, 3298820, 2229381, 546514, 3299371, 3155184, 53340, 3299353, 3299402, 3299463, 3299464])
    insert_pool('OWC 2021 RO16',
    [3287700, 3287781, 3287483, 3287875, 3287485, 3287712, 3287656, 990396, 3287751, 3287743, 3287252, 3142329, 2819029, 3287758, 3287767],
    [5, 2, 2, 3, 2, 0, 0, 1])
    insert_pool('OWC 2021 RO32',
    [3276259, 3276724, 2692632, 3276740, 2613076, 3276559, 3276441, 240689, 3099848, 3276673, 3276823, 3276774, 3276444, 2791506, 3276769],
    [5, 2, 2, 3, 2, 0, 0, 1])
    insert_pool('OWC 2021 QL',
    [3263082, 3263098, 3263248, 3263131, 3263097, 3263174, 3262706, 3263175, 3263112, 3263028],
    [4, 2, 2, 2, 0, 0, 0, 0])

    insert_pool('OWC 2020 GF',
    [2719302, 2719284, 2651784, 2719485, 2719305, 2719326, 2742940, 2719334, 2719328, 3197547, 2719372, 665149, 2719411, 2719893, 2719407, 2603690, 2719427, 2719439, 2719437, 2719462])
    insert_pool('OWC 2020 Finals',
    [2708955 ,2708949, 2708946, 2708970, 2708952, 2708983, 2708985, 2709014,2708997, 2709040, 2709049, 2709056, 2709059, 2709164, 2594991, 2709076, 2709094, 2709080, 2709083, 2709097])
    insert_pool('OWC 2020 SF',
    [2699190, 2699196, 2699135, 2699240, 2699219, 2699221, 2699222, 2699419, 1522554, 2699247, 1863224, 2699245, 975036, 2699262, 2699264, 2699269, 2699274, 3387202, 2699289, 2699308])
    insert_pool('OWC 2020 QF',
    [2689633, 2689713, 2633136, 2689434, 2689459, 2689460, 2689510, 2689473, 2689478, 1964722, 2067296, 2689525, 1121089, 2689570, 2553146, 2042994, 2689672, 2191964, 2176407, 2556233])
    insert_pool('OWC 2020 RO16',
    [2450295, 2680248, 2680283, 2680328, 2680247, 2680271, 2405667, 2196278, 2680257, 2399771, 2680274, 2680273, 2680275, 2680522, 2680280],
    [5, 2, 2, 3, 2, 0, 0, 1])
    insert_pool('OWC 2020 RO32',
    [2667881, 2670759, 2465287, 2670817, 2670818, 1789641, 2670774, 2458108, 501755, 1577780, 1097552, 344619, 2291881, 2317907, 3351879],
    [5, 2, 2, 3, 2, 0, 0, 1])
    insert_pool('OWC 2020 QL',
    [2659377, 2826730, 2659349, 2659353, 2659351, 2659367, 2659364, 2659376, 2659374, 2659360],
    [4, 2, 2, 2, 0, 0, 0, 0])

    insert_pool('Corsace Closed 2022 SF',
    [3622209, 3178933, 2893305, 3014360, 3622207, 3622269, 3621504, 2868857, 3621995, 3622233, 3622294, 3622267, 3622085, 1950890, 3622277, 3241848],
    [6, 3, 3, 3, 0, 0, 0, 1])
    insert_pool('Corsace Closed 2022 QF',
    [3230638, 3612033, 3612220, 3580580, 3611958, 3612092, 3252165, 3612221, 2502505, 360345, 3612284, 3612219, 3612240, 3322624, 3611592, 3547292],
    [6, 3, 3, 3, 0, 0, 0, 1])
    insert_pool('Corsace Closed 2022 RO16',
    [3159026, 2948446, 3601681, 3179910, 3227911, 3183708, 3601518, 1618445, 2528621, 1189905, 3602515, 2990275, 1384674, 3602516, 3602578, 3602497],
    [6, 3, 3, 3, 0, 0, 0, 1])
    insert_pool('Corsace Closed 2022 QL',
    [3243028, 3591637, 3591639, 3591993, 2592033, 3591641, 3591652, 1411709, 2169831, 66820],
    [4, 2, 2, 2, 0, 0, 0, 0])

    insert_pool('Corsace Closed 2021 GF',
    [3081764, 3081743, 3082062, 3081747, 3081735, 3081766, 3081768, 3081776, 2132924, 1331610, 2902513, 3081814, 3081816, 2739798, 3081820, 3082938, 478605, 3081873, 3081825],
    [6, 4, 4, 4, 0, 0, 0, 1])
    insert_pool('Corsace Closed 2021 Finals',
    [2174412, 3073476, 3073509, 2745135, 2739265, 3073484, 3074303, 2494801, 3073604, 2983785, 3073990, 2797986, 2613160, 3069073, 3073475, 3073481, 1855988, 3073557, 3073499],
    [6, 4, 4, 4, 0, 0, 0, 1])
    insert_pool('Corsace Closed 2021 SF',
    [3059148, 3059190, 2921554, 3059194, 2495226, 3059430, 3059613, 3059189, 3059218, 2423209, 2371971, 3059216, 2176783, 2371744, 1465149, 2540771],
    [6, 3, 3, 3, 0, 0, 0, 1])
    insert_pool('Corsace Closed 2021 QF',
    [3048911, 2719284, 3048737, 2295195, 2431442, 580699, 2258598, 2458659, 2568326, 2615377, 2414318, 3048727, 2073439, 2648002, 34859, 2500241],
    [6, 3, 3, 3, 0, 0, 0, 1])
    insert_pool('Corsace Closed 2021 RO16',
    [2407999, 1932489, 2520179, 2432451, 2603850, 451764, 2728951, 2588430, 2295392, 2238810, 2463731, 1759822, 290581, 139981, 2716181, 3035067],
    [6, 3, 3, 3, 0, 0, 0, 1])
    insert_pool('Corsace Closed 2021 Play-In',
    [1474012, 1184335, 1972166, 2067859, 2454944, 2831889, 2259267, 2184234, 2731544, 2280640, 2385598, 703176, 548641, 380475, 3021093, 1251769],
    [6, 3, 3, 3, 0, 0, 0, 1])
    insert_pool('Corsace Closed 2021 QL',
    [2217317, 927672, 2294521, 2133938, 2250760, 2403253, 2756612, 2267424, 1017899, 91462],
    [4, 2, 2, 2, 0, 0, 0, 1])

    insert_pool('Corsace Open 2021 GF',
    [3229006, 3229017, 3229021, 3229024, 3228585, 3229041, 3229042, 3229109, 3228864, 3229047, 3229058, 3229063, 3228865, 3228972, 3228871, 3229013, 3229007, 3229078, 3229080, 3229091])
    insert_pool('Corsace Open 2021 Finals',
    [3216821, 3216822, 3216836, 3216805, 3216854, 3216882, 3216424, 3216888, 3216899, 3216900, 3216417, 3216902, 3216668, 3216909, 3216912, 3216914, 3216819, 3216930, 3216936, 3223735])
    insert_pool('Corsace Open 2021 SF',
    [3205755, 3205101, 3205720, 3205635, 3205527, 3205640, 3205642, 3205646, 3204597, 3205649, 3205657, 3205652, 3205099, 3205317, 3205479, 3205506, 3205629, 3205682, 3205537, 3205692])
    insert_pool('Corsace Open 2021 QF',
    [3193043, 3192865, 3193011, 3193021, 3193038, 3193040, 3193044, 3192834, 3193055, 3192918, 3193150, 3192828, 3193205, 3192292, 3191336, 3193194, 3193093, 3191344, 3193066, 3191655])
    insert_pool('Corsace Open 2021 RO16',
    [3181298, 3181702, 3181309, 3181310, 3181311, 3181223, 3181303, 3180979, 3181355, 3181167, 3181307, 3181344, 3181503, 3181150, 3181360, 3179916, 3181379, 3181385, 3181228, 3181394])
    insert_pool('Corsace Open 2021 RO32',
    [3167229, 3168048, 3168793, 3168353, 3168762, 3168789, 3165704, 3168773, 3167107, 3168788, 3168621, 3168758, 3168808, 3167276, 3167236, 3168616, 3168036, 3168752, 3168820, 3168834])
    insert_pool('Corsace Open 2021 RO64',
    [3155409, 3155574, 3155269, 3153693, 3155328, 3154009, 3155281, 3155237, 3155576, 3155008, 3155531, 3156684, 3155766, 3155989, 3155519, 3155518, 3155182, 3155247, 3155970, 3155585])
    insert_pool('Corsace Open 2021 QL',
    [3142494, 3141960, 3142496, 3142502, 3142389, 3141635, 3142708, 3142520, 3142522, 3140773],
    [4, 2, 2, 2, 0, 0, 0, 0])

    insert_pool('Perennial 2022 QF',
    [3502280, 2970030, 3634631, 3228591, 3227911, 3634730, 264369, 3046747, 1597253, 3256946, 2415770, 3321542, 3634662, 3040257, 3634801, 2709076, 3485307, 2662619, 3540482, 3099626])
    insert_pool('Perennial 2022 RO16',
    [3622063, 2918146, 3193021, 3622090, 3071701, 2819481, 3617014, 1588369, 3074035, 3373281, 2719431, 2709016, 2180986, 167997, 2699308],
    [5, 2, 2, 3, 2, 0, 0, 1])
    insert_pool('Perennial 2022 RO32',
    [2230996, 3180049, 3359370, 3215025, 3204875, 3176483, 3129973, 1018247, 3393953, 3424921, 2096920, 2666657, 3180732, 3160662, 1034570],
    [5, 2, 2, 3, 2, 0, 0, 1])
    insert_pool('Perennial 2022 QL',
    [3068492, 3192005, 3603350, 3603353, 3600519, 3500303, 3321959, 2114008, 3603367, 3322598],
    [4, 2, 2, 2, 0, 0, 0, 0])

    insert_pool('Yuki Aim GF',
    [2962206, 1380717, 2309006, 3003419, 1566379, 1754266, 172662, 1883277, 2762163, 3087146, 2651915, 1165848, 1491800, 3276707, 804164, 2110050, 1184958, 1385941, 2332088],
    [6, 4, 4, 4, 0, 0, 0, 1])
    insert_pool('Yuki Aim Finals',
    [3085953, 2020385, 1412281, 2395150, 2642757, 1236211, 2012763, 2651838, 2719427, 2930403, 930307, 2352372, 2194972, 866192, 2492022, 1228840, 1046977, 1971416, 2994583],
    [6, 4, 4, 4, 0, 0, 0, 1])
    insert_pool('Yuki Aim SF',
    [2327276, 3082675, 2527867, 2438517, 2643124, 2658757, 2942890, 2676099, 2916573, 2675756, 1915426, 490910, 2150750, 1207948, 1356688, 2512118, 2224972, 1036107],
    [5, 4, 4, 4, 0, 0, 0, 1])
    insert_pool('Yuki Aim QF',
    [2526166, 2541684, 2072475, 2376713, 1532151, 3158000, 2487840, 2719328, 2560589, 1046293, 1588845, 2520179, 1658362, 1353404, 434536, 1883681, 641809, 1591935],
    [5, 4, 4, 4, 0, 0, 0, 1])
    insert_pool('Yuki Aim RO16',
    [319493, 260155, 257557, 156445, 197567, 249505, 319549, 182525, 88131, 296055, 157982, 124789, 165350, 156021, 1279343],
    [5, 3, 3, 3, 0, 0, 0, 1])
    insert_pool('Yuki Aim RO32',
    [2808923, 2467744, 1958623, 2196768, 2515473, 2270502, 2588430, 1050214, 1744742, 2003510, 2123641, 766560, 131147, 2210623, 3121734],
    [5, 3, 3, 3, 0, 0, 0, 1])
    insert_pool('Yuki Aim RO64',
    [3024505, 2872154, 2989093, 2542628, 2800493, 2811634, 1725155, 3181967, 1931138, 1025587, 2146372, 969420, 1438458, 2440455, 412288],
    [5, 3, 3, 3, 0, 0, 0, 1])
    insert_pool('Yuki Aim QL',
    [823710, 1722835, 2681263, 1417513, 2449759, 2734813, 2180369, 2922816, 546514, 49067],
    [4, 2, 2, 2, 0, 0, 0, 0])

    insert_pool('Quarterly Cup 1 QF',
    [2905151, 3355394, 3144020, 2670817, 3482929, 3452738, 3064464, 3376899, 3428216, 3259994, 3282876, 2993246, 3362294, 3457575, 2921152, 3195063, 3265479, 3318980, 3326071, 3472890, 2270749, 2774775],
    [6, 3, 3, 4, 3, 0, 0, 3])
    insert_pool('Quarterly Cup 1 RO16',
    [3329838, 2527018, 3283617, 3151748, 3292028, 3287109, 2536441, 3036398, 3179992, 3278008, 3312640, 3411754, 2796075, 3047030, 3127522, 3142373, 3098550],
    [5, 2, 2, 3, 2, 0, 0, 3])
    insert_pool('Quarterly Cup 1 RO32',
    [3408258, 3495347, 3110178, 3277004, 3113527, 2731307, 3356349, 3053630, 2888271, 3380580, 3489573, 3335242, 3296885, 3454166, 3370175, 3289033, 2596314],
    [5, 2, 2, 3, 2, 0, 0, 3])
    insert_pool('Quarterly Cup 1 RO64',
    [3118813, 642163, 2668905, 3455788, 3336632, 2828826, 3505833, 3343490, 3423661, 2974697, 3034527, 3409877, 2628802, 3407910, 3384040, 3422381, 2722682],
    [5, 2, 2, 3, 2, 0, 0, 3])
    insert_pool('Quarterly Cup 1 QL',
    [3329210, 3169485, 3423785, 3377399, 3373331, 3355800, 3375519, 2966540, 2259080, 2855311],
    [4, 2, 2, 2, 0, 0, 0, 0])

    insert_pool('SGWT GF',
    [3360158, 2680248, 2952884, 3113565, 2643167, 3195490, 2584895, 137303, 2677222, 3197547, 1502636, 3375590, 3557075, 3181360, 2701648, 1831280, 2556492, 3112111, 2680522, 3557110])
    insert_pool('SGWT Finals',
    [3192918, 3215610, 3365041, 1382561, 1593690, 3206741, 1100091, 3106078, 2483949, 1068860, 103102, 3543498, 812721, 2624225, 3140773, 818655, 2755564, 2359580, 1936561, 2626920])
    insert_pool('SGWT SF',
    [1653723, 2510533, 2465287, 684970, 2650676, 2218160, 3076066, 89362, 2662928, 2660175, 605717, 1569283, 1676390, 2813113, 3106294, 58627, 2782643, 3081707, 2418106, 860019])
    insert_pool('SGWT QF',
    [2061599, 2067141, 3316856, 1743693, 309903, 2474203, 3050698, 2407774, 3346178, 282251, 3031685, 2719431, 3253613, 2714747, 850729, 65855, 908947, 28148, 509610, 2881112])
    insert_pool('SGWT RO16',
    [2944895, 2171716, 2588702, 495541, 2223742, 2875108, 104701, 3276441, 2251927, 3471076, 2594990, 103221, 155632, 26436, 734339],
    [5, 2, 2, 3, 2, 0, 0, 1])
    insert_pool('SGWT RO32',
    [2538080, 529358, 3009647, 2034488, 2331568, 2744108, 2872861, 984299, 2619929, 2052458, 2057222, 1781691, 3314594, 2643263, 1924634],
    [5, 2, 2, 3, 2, 0, 0, 1])
    insert_pool('SGWT QL',
    [2880145, 3335664, 2306852, 2265852, 2581938, 88633, 217651, 2136291, 3283045, 2766955],
    [4, 2, 2, 2, 0, 0, 0, 0])

    insert_pool('5DCT3 RO16',
    [3340977, 2766489, 670501, 1631406, 3448872, 1914227, 84911, 2843307, 3446299, 2034979, 3234400, 772067, 3631489, 1455080, 1407811],
    [5, 3, 3, 3, 0, 0, 0, 1])
    insert_pool('5DCT3 RO32',
    [2715288, 432839, 2828902, 3226426, 1176292, 2183201, 105978, 1599053, 2521368, 2643263, 3045507, 833485, 2565653, 2645722, 3542674],
    [5, 3, 3, 3, 0, 0, 0, 1])
    insert_pool('5DCT3 RO64',
    [1809691, 3160793, 2476072, 1515987, 2773389, 3279036, 1546428, 2459722, 2168319, 2433048, 1756217, 1900304, 1707909, 1936116, 924668],
    [5, 3, 3, 3, 0, 0, 0, 1])
    insert_pool('5DCT3 QL',
    [2479386, 2021526, 815857, 2603702, 2588362, 2938091, 859696, 2138306, 2369074, 2041171],
    [4, 2, 2, 2, 0, 0, 0, 0])

    insert_pool('YWSC QL',
    [1174117, 484890, 2647186, 2541404, 1403276, 153988, 2061024, 2314637, 2603488, 3092726],
    [4, 2, 2, 2, 0, 0, 0, 0])

    insert_pool('MonkeCup 2022 SF',
    [2476304, 2893329, 2680283, 3081313, 3158738, 1789641, 2699675, 3168752, 2094186, 2130349, 3494393, 2202288, 268080, 3117877, 48689, 687668, 64996, 1606045, 2008482],
    [5, 3, 3, 4, 3, 0, 0, 1])
    insert_pool('MonkeCup 2022 QF',
    [3403371, 3045585, 2603689, 3156597, 2540064, 3182984, 1957037, 339959, 438732, 923254, 2781761, 2942900, 2004985, 46996, 3205645, 1878931],
    [5, 2, 2, 3, 3, 0, 0, 1])
    insert_pool('MonkeCup 2022 RO16',
    [1820338, 1452809, 2785532, 2707715, 3525649, 2259769, 2743822, 2588363, 2204492, 1826208, 97338, 2925240, 2655698, 49822, 1093605],
    [5, 2, 2, 3, 2, 0, 0, 1])
    insert_pool('MonkeCup 2022 RO32',
    [1800218, 2807987, 2506968, 3503279, 1084171, 2885207, 2778749, 33736, 157856, 3234308, 2815970, 1517665, 2162331, 1660992],
    [4, 2, 2, 3, 2, 0, 0, 1])
    insert_pool('MonkeCup 2022 QL',
    [2415690, 1917144, 3009647, 2503006, 231390, 3505833, 1184098, 2433048, 732932, 2106719],
    [4, 2, 2, 2, 0, 0, 0, 0])

    insert_pool('SSKC1 Tier A',
    [1966553, 153066, 2028973, 2480417, 1187506, 2588430, 1086956, 272454, 487250, 2142039, 2285780],
    [4, 2, 2, 2, 0, 0, 0, 1])
    insert_pool('SSKC1 Tier B',
    [942561, 3262368, 2112706, 923384, 2932532, 85075, 3050746, 1021024, 1486212, 870740, 2834820],
    [4, 2, 2, 2, 0, 0, 0, 1])

    insert_pool('SSKC2 Tier A',
    [980313, 3169485, 2908767, 1754868, 2178004, 65233, 1760024, 2623949, 2569702, 2255706, 3158333],
    [4, 2, 2, 2, 0, 0, 0, 1])
    insert_pool('SSKC2 Tier B',
    [2197486, 2606880, 890811, 2617306, 1971493, 2131582, 1971633, 2467479, 2090356, 2601595, 1968436],
    [4, 2, 2, 2, 0, 0, 0, 1])

    insert_pool('SSKC4 Tier S',
    [2540371, 3227634, 2856086, 2137778, 2361457, 3241847, 2930796, 2659376, 2739530, 3363306, 2399771, 2116494],
    [4, 2, 2, 3, 0, 0, 0, 1])
    insert_pool('SSKC4 Tier A',
    [2086666, 3391964, 2880794, 1769262, 2545390, 3141635, 657509, 1600778, 974653, 3057427, 1437794, 2389485],
    [4, 2, 2, 3, 0, 0, 0, 1])
    insert_pool('SSKC4 Tier B',
    [2267030, 3169485, 2028973, 2977897, 1506823, 2574379, 1402509, 110628, 643607, 1125982, 1907218, 1478218],
    [4, 2, 2, 3, 0, 0, 0, 1])

    con.commit()

    end = datetime.now()

    print(end - start)