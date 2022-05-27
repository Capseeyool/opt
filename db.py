import os
import sqlite3

def insert_pool(tournament, ids, mods=[6, 3, 3, 4, 3, 0, 0, 1]):
    mods = [f'{i[0]}{j}' for i in [i for i in list(zip(['NM', 'HR', 'HD', 'DT', 'FM', 'EZ', 'HT', 'TB'], mods))] for j in range(1, i[1] + 1)]
    for i in zip(mods, ids):
        cur.execute(f'INSERT INTO db (tournament, mod, ID) VALUES (\'{tournament}\', \'{i[0]}\', {i[1]})')

if os.path.exists('db.db'):
    os.remove('db.db')

con = sqlite3.connect('db.db')
cur = con.cursor()

cur.execute('''CREATE TABLE db (
tournament VARCHAR(255) NOT NULL,
mod VARCHAR(3) NOT NULL,
ID INT NOT NULL,
FOREIGN KEY (ID) REFERENCES maps(ID)
)''')

insert_pool('OWC 2021 GF',
[3333705, 3333669, 3333699, 3333703, 3333700, 3333701, 3145691, 3333793, 3333706, 3081546, 3331199, 3333660, 3333570, 3333586, 3333770, 3333734, 3333729, 3333760, 3333738, 3333745])
insert_pool('OWC 2021 Finals',
[2675756, 3322513, 3322521, 3322526, 3322566, 3322093, 2856086, 3322576, 2633747, 438187, 2947341, 3322603, 3320894, 3322598, 859667, 3322610, 3322611, 2643166, 3322445, 3322616])
insert_pool('OWC 2021 SF',
[3311170, 3310526, 3311309, 3311337, 3311312, 3311313, 3311238, 3311073, 2267887, 861381, 3311344, 3311036, 2643135, 3311366, 277274, 3311356, 3311891, 3311383, 3311376, 3311391])
insert_pool('OWC 2021 QF',
[3299389, 3299406, 3299411, 1722011, 3297498, 3299412, 1843575, 2623967, 546944, 2633812, 3298820, 2229381, 546514, 3299371, 3155184, 53340, 3299353, 3299402, 3299463, 3299464])

insert_pool('SGWT QL',
[2880145, 3335664, 2306852, 2265852, 2581938, 88633, 217651, 2136291, 3283045, 2766955],
[4, 2, 2, 2, 0, 0, 0, 0])
insert_pool('SGWT RO32',
[2538080, 529358, 3009647, 2034488, 2331568, 2744108, 2872861, 984299, 2619929, 2052458, 2057222, 1781691, 3314594, 2643263, 1924634],
[5, 2, 2, 3, 2, 0, 0, 1])
insert_pool('SGWT RO16',
[2944895, 2171716, 2588702, 495541, 2223742, 2875108, 104701, 3276441, 2251927, 3471076, 2594990, 103221, 155632, 26436, 734339],
[5, 2, 2, 3, 2, 0, 0, 1])
insert_pool('SGWT QF',
[2061599, 2067141, 3316856, 1743693, 309903, 2474203, 3050698, 2407774, 3346178, 282251, 3031685, 2719431, 3253613, 2714747, 850729, 65855, 908947, 28148, 509610, 2881112])
insert_pool('SGWT SF',
[1653723, 2510533, 2465287, 684970, 2650676, 2218160, 3076066, 89362, 2662928, 2660175, 605717, 1569283, 1676390, 2813113, 3106294, 58627, 2782643, 3081707, 2418106, 860019])
insert_pool('SGWT Finals',
[3192918, 3215610, 3365041, 1382561, 1593690, 3206741, 1100091, 3106078, 2483949, 1068860, 103102, 3543498, 812721, 2624225, 3140773, 818655, 2755564, 2359580, 1936561, 2626920])
insert_pool('SGWT GF',
[3360158, 2680248, 2952884, 3113565, 2643167, 3195490, 2584895, 137303, 2677222, 3197547, 1502636, 3375590, 3557075, 3181360, 2701648, 1831280, 2556492, 3112111, 2680522, 3557110])

insert_pool('Quarterly Cup 1 QL',
[3329210, 3169485, 3423785, 3377399, 3373331, 3355800, 3375519, 2966540, 2259080, 2855311])
insert_pool('Quarterly Cup 1 RO64',
[3118813, 642163, 2668905, 3455788, 3336632, 2828826, 3505833, 3343490, 3423661, 2974697, 3034527, 3409877, 2628802, 3407910, 3384040, 3422381, 2722682],
[5, 2, 2, 3, 2, 0, 0, 3])
insert_pool('Quarterly Cup 1 RO32',
[3408258, 3495347, 3110178, 3277004, 3113527, 2731307, 3356349, 3053630, 2888271, 3380580, 3489573, 3335242, 3296885, 3454166, 3370175, 3289033, 2596314],
[5, 2, 2, 3, 2, 0, 0, 3])
insert_pool('Quarterly Cup 1 RO16',
[3329838, 2527018, 3283617, 3151748, 3292028, 3287109, 2536441, 3036398, 3179992, 3278008, 3312640, 3411754, 2796075, 3047030, 3127522, 3142373, 3098550],
[5, 2, 2, 3, 2, 0, 0, 3])
insert_pool('Quarterly Cup 1 QF',
[2905151, 3355394, 3144020, 2670817, 3482929, 3452738, 3064464, 3376899, 3428216, 3259994, 3282876, 2993246, 3362294, 3457575, 2921152, 3195063, 3265479, 3318980, 3326071, 3472890, 2270749, 2774775],
[6, 3, 3, 4, 3, 0, 0, 3])

con.commit()