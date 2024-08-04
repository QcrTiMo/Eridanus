# -*- coding: gbk -*-
import os.path
import random

from PIL import Image

tarot = [['愚者 (The Fool)',
          '从零开始; 好赌运; 不墨守成规; 追求新奇的梦想; 冒险; 放浪形骸; 艺术家的气质; 异于常人; 直攻要害、盲点; 爱情狩猎者; 爱情历经沧桑; 不拘形式的自由恋爱',
          '不安定; 孤注一掷会失败; 缺乏责任感; 损失; 脚跟站不稳; 堕落; 没发展; 没计划; 走错路; 行为乖张; 轻浮的恋情; 感情忽冷忽热; 不安定的爱情之旅',
          'The Fool.jpg'],
         ['魔术师 (The Magician)',
          '好的开始; 具独创性; 有发展的; 新计划成功; 想像力丰富或有好点子; 有恋情发生; 拥有默契良好的伴侣; 有新恋人出现; 值得效仿的对象出现',
          '失败; 优柔寡断; 才能平庸; 有被欺诈的危险; 技术不足; 过于消极; 没有判断力; 缺乏创造力; 爱情没有进展',
          'The Magician.jpg'],
         ['女祭司 (The High Priestess)',
          '知性、优秀的判断力; 具洞察力及先见之明; 强大的战斗意志; 冷静的统率力; 学问、研究等精神方面幸运; 独立自主的女性; 柏拉图式的爱情; 有心灵上交往至深的友人; 冷淡的恋情',
          '无知、缺乏理解力; 研究不足; 不理性的态度; 自我封闭; 神经质; 洁癖; 与女性朋友柒争执; 对人冷淡; 晚婚或独身主义; 没有结果的单相思; 气色不好; 不孕',
          'The High Priestess.jpg'],
         ['皇帝 (The Emperor)',
          '以坚强的意志力及手腕获致成功; 富裕和力量; 有责任感; 良好的处理能力; 具领导能力; 男性的思考; 坚持到底; 虽有点专制却值得信赖; 条件诱人的提亲; 与年长者恋爱',
          '不成熟; 意志薄弱; 虚有其表; 看不清现实; 欠缺实务能力; 因傲慢而招人反感; 工作过度; 固执; 没有经济基础; 没有好对象; 苦恋结束; 勉强的感情',
          'The Emperor.jpg'],
         ['教皇 (The Hierophant)',
          '受人信赖; 有贵人相助; 贡献; 受上司重视; 能胜任工作; 拥有一颗温柔的心; 受惠于有益的建言; 接触宗教的事物大吉; 与年长的异性有缘; 良缘; 深情宽大的爱; 有结良缘的机会',
          '没信用; 没有贵人相助; 孤立无援; 不受欢迎的好意; 依赖心是最大的敌人; 太罗嗦而讨人厌; 碍于私情而无法成功; 心胸狭窄; 得不到亲人的谅解的恋情; 彼此过于关心; 缘分浅薄的恋情',
          'The Hierophant.jpg'],
         ['恋人 (The Lovers)',
          '幸运的结合; 有希望的将来; 有共同做事的伙伴; 与人合作或社团活动; 敏感决定前进之路的好时机; 有意气相投的朋友; 爱情机会将到来; 罗曼蒂克的恋情; 爱的预感',
          '分离; 消解; 不合作的态度; 眼花缭乱; 没有满意的成果; 无法持续; 退休; 妨碍; 血气方刚; 多情的人; 分手; 冷漠的爱; 背信; 逃避爱情; 短暂的恋情',
          'The Lovers.jpg'],
         ['战车 (The Chariot)',
          '前进必胜; 先下手为强; 独立; 起程; 在颠簸中仍有好成绩; 活泼; 有野心; 以速度取胜; 有开拓精神; 握有指挥权; 战胜敌手; 富行动力的恋情; 恋爱的胜利者',
          '失败; 丧失战斗意志; 状态不佳; 挫折; 性子过急为失败之因; 不感兴趣; 效率不佳; 资金运转困难; 无奋斗精神; 有强劲敌手进入; 被拒绝; 因怯懦而使恋情不顺',
          'The Chariot.jpg'],
         ['力量 (Strength)',
          '不屈不挠的精神; 将不可能化为可能的意志力; 全力以赴; 突破难关; 坚强的信念和努力; 挑战已知危险的勇气; 神秘的力量; 旺盛的斗志; 轰轰烈烈的恋情; 克服困难的真实爱情',
          '疑心病; 犹豫不决; 实力不足; 无忍耐力; 危险的赌注; 勉强为之而适得其反; 丧失自信; 喜欢故弄玄虚; 体力不足; 自大自负; 误用力气',
          'Strength.jpg'],
         ['隐士 (The Hermit)',
          '智能与卓越见解; 不断地追求更高层次的东西; 思虑周密; 冷静沉着; 不多言; 接触知性事物吉; 正中核心的建言; 活动慢慢进行较有成果; 出局; 追求柏拉图式的爱情; 暗中的爱情',
          '一视同仁; 不够通融; 不专心易生错误; 过分警戒，无法顺利进行; 秘密泄漏; 过于固执不听别人的意见; 孤独; 动机不单纯; 因怨言及偏见招人嫌; 轻浮的爱情; 怀疑爱情',
          'The Hermit.jpg'],
         ['命运之轮 (The Wheel of Fortune)',
          '机会到来; 随机应变能力佳; 好运; 转换期; 意想不到的幸运; 升迁有望; 变化丰富; 好时机; 宿命的相逢; 一见钟情; 幸运的婚姻; 富贵的身份',
          '低潮期; 时机未到; 评估易出错; 时机不好; 没有头绪; 处于劣势; 生活艰苦; 情况恶化; 计划停滞需要再等待; 失恋; 短暂的恋情; 易错失良机; 不敌诱惑; 爱情无法持久',
          'The Wheel of Fortune.jpg'],
         ['正义 (Justice)',
          '公正; 严正的意见; 良好的均衡关系; 严守中立立场; 凡事合理化; 身兼两种工作; 协调者; 与裁判、法律相关者; 表里一致的公正人物; 以诚实之心光明正大地交往; 彼此能获得协调',
          '不公正; 不平衡; 不利的条件; 偏颇; 先入为主的观念; 偏见与独断; 纷争、诉讼; 问心有愧; 无法两全; 天平两边无法平衡; 性格不一致; 无视于社会道德观的恋情; 偏爱',
          'Justice.jpg'],
         ['倒吊人 (The Hanged Man)',
          '接受考验; 无法动弹; 被牺牲; 有失必有得; 从痛苦的体验中获得教训; 过度期; 不贪图眼前利益; 浴火重生; 多方学习; 奉献的爱; 明知辛苦但全力以赴',
          '无谓的牺牲; 折断骨头; 有噩运、居于劣势; 任性妄为; 不努力; 变得没有耐性; 利己主义者; 受到惩罚; 无偿的爱; 缺乏共同奋斗的伙伴',
          'The Hanged Man.jpg'],
         ['死神 (Death)',
          '失败; 毁灭之日将近; 损害继续延续; 失业; 进展停滞; 交易停止; 为时已晚; 停滞状态; 生病或意外的暗示; 味如嚼蜡的生活; 不幸的恋情; 恋情终止; 彼此间有很深的鸿沟; 别离',
          '起死回生的机会; 脱离低迷期; 改变印象; 回心转意再出发; 挽回名誉; 奇迹似地康复; 突然改变方针; 已经死心的事有了转机; 斩断情丝，重新出发',
          'Death.jpg'],
         ['节欲 (Temperance)',
          '单纯化; 顺畅; 交往平顺; 两者相融顺畅; 调整; 彼此交换有利条件; 平凡中也有重要的契机; 平顺的心境; 纯爱; 从好感转为爱意; 深爱',
          '消耗; 每节制的损耗，对身心产生不好的影响; 疲劳; 不定性的工作; 缺乏调整能力; 下降; 浪费; 不要与人 合作; 不融洽; 爱情的配合度不佳',
          'Temperance.jpg'],
         ['恶魔 (The Devil)',
          '被束缚; 堕落; 恶魔的私语; 卑躬屈膝; 欲望的俘虏; 荒废的生活; 举债度日; 病魔入侵; 夜游过多; 不可告人的事; 恶意; 不可抗拒的诱惑; 私密恋情; 沉溺于感官刺激之下',
          '逃离拘束; 长期的苦恼获得解放; 斩断前缘; 越过难关; 暂时停止; 拒绝诱惑; 舍弃私欲; 治愈长期病痛; 别离   时刻; 如深陷泥沼爱恨交加的恋情',
          'The Devil.jpg'],
         ['塔 (The Tower)',
          '致命的打击; 纷争; 纠纷不断; 与周遭事物对立，情况恶化; 意想不到的事情; 急病; 受牵连; 急剧的大变动; 信念奔溃; 逆境; 破产; 没有预警，突然分离; 破灭的爱; 玩火自焚',
          '紧迫的状态; 险恶的气氛; 内讧; 即将破灭; 急需解决的问题; 承受震撼; 背水一战; 注意刑事问题; 因骄傲自大将付出惨痛的代价; 状况不佳; 困境; 爱情危机; 分离的预感',
          'The Tower.jpg'],
         ['星辰 (The Star)',
          '愿望达成; 前途光明; 充满希望的未来; 美好的生活; 曙光出现; 大胆的幻想; 水准提高; 新的创造力; 想像力; 理想的对象; 美好的恋情; 爱苗滋生',
          '挫折、失败; 理想过高; 缺乏想像力; 异想天开; 事与愿违; 失望; 从事不喜欢的工作; 好高骛远; 情况悲观; 不可期待的对象; 没 有爱的生活; 秘密恋情; 仓皇失措',
          'The Star.jpg'],
         ['月亮 (The Moon)',
          '不安与动摇; 心中不平静; 谎言; 暧昧不明; 鬼迷心窍; 暗藏动乱; 欺骗; 终止; 不安的爱; 三角关系',
          '从危险的骗局中逃脱; 状况稍为好转; 误会冰释; 破除迷惘; 时间能解决一切; 眼光要长远; 静观等待; 早期发现早期治疗有效; 事前察知危险; 对虚情假意的恋情已不在乎',
          'The Moon.jpg'],
         ['太阳 (The Sun)',
          '丰富的生命力; 巨大的成就感; 人际关系非常好; 爱情美满; 内心充满了热情和力量; 一定能够实现的约定; 飞黄腾达; 无忧无虑',
          '情绪低落; 事情失败; 朋友的离去和人际关系的恶化; 无法安定内心; 忧郁孤单寂寞; 爱情不顺 利; 取消的计划; 工作上困难重重',
          'The Sun.jpg'],
         ['审判 (Judgement)',
          '复活的喜悦; 开运; 公开; 改革期; 危机解除; 决断; 荣升; 崭露头角; 好消息; 爱的使者; 恢复健康; 坦白; 复苏的爱; 再会; 爱的奇迹',
          ' 一败不起; 幻灭; 离复苏还有很长的时间; 不利的决定; 不被采用; 还未开始就结束了; 坏消息; 延期; 无法决定; 虽重新开始，却又恢复原状; 分离、消除; 恋恋不舍',
          'Judgement.jpg'],
         ['世界 (The World)',
          '完成; 成功; 拥有毕生的志业; 达成目标; 永续不断; 最盛期; 完美无缺; 接触异国，将获得幸运; 到达标准; 精神亢奋; 快乐的结束; 模范情侣',
          '未完成; 无法达到计划中的成就; 因准备不足而失败; 中途无法在进行; 不完全燃烧; 一时不顺利; 饱和状态; 烦恼延续; 精神松弛; 个人惯用的表现方式; 因不成熟而 使情感受挫; 合谋; 态度不够圆融',
          'The World.jpg']]


def tarotChoice():
    ints = random.randint(0, 1)
    if ints == 0:
        tarots = random.choice(tarot)
        txt = tarots[0] + '\n' + '正位' + '\n' + tarots[1]
        img = 'data/pictures/tarot/TarotImages/' + tarots[3]
        return txt, img
    if ints == 1:
        tarots = random.choice(tarot)
        txt = tarots[0] + '\n' + '逆位' + '\n' + tarots[2]
        img1 = 'data/pictures/tarot/TarotSide/' + tarots[3]
        if os.path.exists(img1):
            return txt, img1
        else:
            # 打开图像
            img = Image.open('data/pictures/tarot/TarotImages/' + tarots[3])

            # 旋转180度
            rotated_img = img.rotate(180)

            # 保存旋转后的图像
            rotated_img.save('data/pictures/tarot/TarotSide/' + tarots[3])
            return txt, img1

lucky = [
    "——中吉——\n天上有云飘过的日子，天气令人十分舒畅。\n工作非常顺利，连午睡时也会想到好点子。\n突然发现，与老朋友还有其他的共同话题…\n——每一天，每一天都要积极开朗地度过——",
    "——中吉——\n十年磨一剑，今朝示霜刃。\n恶运已销，身临否极泰来之时。\n苦练多年未能一显身手的才能，\n现今有了大展身手的极好机会。\n若是遇到阻碍之事，亦不必迷惘，\n大胆地拔剑，痛快地战斗一番吧。",
    "——大吉——\n会起风的日子，无论干什么都会很顺利的一天。\n周围的人心情也非常愉快，绝对不会发生冲突，\n还可以吃到一直想吃，但没机会吃的美味佳肴。\n无论是工作，还是旅行，都一定会十分顺利吧。\n那么，应当在这样的好时辰里，一鼓作气前进…",
    "——大吉——\n宝剑出匣来，无往不利。出匣之光，亦能照亮他人。\n今日能一箭射中空中的猎物，能一击命中守卫要害。\n若没有目标，不妨四处转转，说不定会有意外之喜。\n同时，也不要忘记和倒霉的同伴分享一下好运气哦。",
    "——大吉——\n失而复得的一天。\n原本以为石沉大海的事情有了好的回应，\n原本分道扬镳的朋友或许可以再度和好，\n不经意间想起了原本已经忘记了的事情。\n世界上没有什么是永远无法挽回的，\n今天就是能够挽回失去事物的日子。",
    "——大吉——\n浮云散尽月当空，逢此签者皆为上吉。\n明镜在心清如许，所求之事心想则成。\n合适顺心而为的一天，不管是想做的事情，\n还是想见的人，现在是行动起来的好时机。",
    "——吉——\n明明没有什么特别的事情，却感到心情轻快的日子。\n在没注意过的角落可以找到本以为丢失已久的东西。\n食物比平时更加鲜美，路上的风景也令人眼前一亮。\n——这个世界上充满了新奇的美好事物——",
    "——吉——\n枯木逢春，正当万物复苏之时。\n陷入困境时，能得到解决办法。\n举棋不定时，会有贵人来相助。\n可以整顿一番心情，清理一番家装，\n说不定能发现意外之财。",
    "——吉——\n一如既往的一天。身体和心灵都适应了的日常。\n出现了能替代弄丢的东西的物品，令人很舒心。\n和常常遇见的人关系会变好，可能会成为朋友。\n——无论是多寻常的日子，都能成为宝贵的回忆——",
    "——末吉——\n云遮月半边，雾起更迷离。\n抬头即是浮云遮月，低头则是浓雾漫漫。\n虽然一时前路迷惘，但也会有一切明了的时刻。\n现下不如趁此机会磨炼自我，等待拨云见皎月。",
    "——末吉——\n空中的云层偏低，并且仍有堆积之势，\n不知何时雷雨会骤然从头顶倾盆而下。\n但是等雷雨过后，还会有彩虹在等着。\n宜循于旧，守于静，若妄为则难成之。",
    "——末吉——\n平稳安详的一天。没有什么令人难过的事情会发生。\n适合和久未联系的朋友聊聊过去的事情，一同欢笑。\n吃东西的时候会尝到很久以前体验过的过去的味道。\n——要珍惜身边的人与事——",
    "——末吉——\n气压稍微有点低，是会令人想到遥远的过去的日子。\n早已过往的年轻岁月，与再没联系过的故友的回忆，\n会让人感到一丝平淡的怀念，又稍微有一点点感伤。\n——偶尔怀念过去也很好。放松心情面对未来吧——",
    "——凶——\n珍惜的东西可能会遗失，需要小心。\n如果身体有不适，一定要注意休息。\n在做出决定之前，一定要再三思考。",
    "——凶——\n隐约感觉会下雨的一天。可能会遇到不顺心的事情。\n应该的褒奖迟迟没有到来，服务生也可能会上错菜。\n明明没什么大不了的事，却总感觉有些心烦的日子。\n——难免有这样的日子——",
    "——大凶——\n内心空落落的一天。可能会陷入深深的无力感之中。\n很多事情都无法理清头绪，过于钻牛角尖则易生病。\n虽然一切皆陷于低潮谷底中，但也不必因此而气馁。\n若能撑过一时困境，他日必另有一番作为。"
]

item = [
    "\n\n今天的幸运物是：色泽艳丽的「堇瓜」。\n人们常说表里如一是美德，\n但堇瓜明艳的外貌下隐藏着的是谦卑而甘甜的内在。",
    "\n\n今天的幸运物是：生长多年的「海灵芝」。\n弱小的海灵芝虫经历多年的风风雨雨，才能结成海灵芝。\n为目标而努力前行的人们，最终也必将拥有胜利的果实。",
    "\n\n今天的幸运物是：茁壮成长的「鸣草」。\n许多人或许不知道，鸣草是能预报雷暴的植物。\n向往着雷神大人的青睐，只在稻妻列岛上生长。\n摘下鸣草时酥酥麻麻的触感，据说和幸福的滋味很像。",
    "\n\n今天的幸运物是：难得一见的「马尾」。\n马尾随大片荻草生长，但却更为挺拔。\n与傲然挺立于此世的你一定很是相配。",
    "\n\n今天的幸运物是：活蹦乱跳的「鬼兜虫」。\n鬼兜虫是爱好和平、不愿意争斗的小生物。\n这份追求平和的心一定能为你带来幸福吧。",
    "\n\n今天的幸运物是：不断发热的「烈焰花花蕊」。\n烈焰花的炙热来自于火辣辣的花心。\n万事顺利是因为心中自有一条明路。",
    "\n\n今天的幸运物是：散发暖意的「鸟蛋」。\n鸟蛋孕育着无限的可能性，是未来之种。\n反过来，这个世界对鸟蛋中的生命而言，\n也充满了令其兴奋的未知事物吧。\n要温柔对待鸟蛋喔。",
    "\n\n今天的幸运物是：节节高升的「竹笋」。\n竹笋拥有着无限的潜力，\n没有人知道一颗竹笋，到底能长成多高的竹子。\n看着竹笋，会让人不由自主期待起未来吧。",
    "\n\n今天的幸运物是：闪闪发亮的「晶核」。\n晶蝶是凝聚天地间的元素，而长成的细小生物。\n而元素是这个世界许以天地当中的人们的祝福。",
    "\n\n今天的幸运物是：暗中发亮的「发光髓」。\n发光髓努力地发出微弱的光芒。\n虽然比不过其他光源，但看清前路也够用了。",
    "\n\n今天的幸运物是：树上掉落的「松果」。\n并不是所有的松果都能长成高大的松树，\n成长需要适宜的环境，更需要一点运气。\n所以不用给自己过多压力，耐心等待彩虹吧。",
    "\n\n今天的幸运物是：酥酥麻麻的「电气水晶」。\n电气水晶蕴含着无限的能量。\n如果能够好好导引这股能量，说不定就能成就什么事业。",
    "\n\n今天的幸运物是：清新怡人的「薄荷」。\n只要有草木生长的空间，就一定有薄荷。\n这么看来，薄荷是世界上最强韧的生灵。\n据说连蒙德的雪山上也长着薄荷呢。",
    "\n\n今天的幸运物是：冰凉冰凉的「冰雾花」。\n冰雾花散发着「生人勿进」的寒气。\n但有时冰冷的气质，也能让人的心情与头脑冷静下来。\n据此采取正确的判断，明智地行动。",
    "\n\n今天的幸运物是：随波摇曳的「海草」。\n海草是相当温柔而坚强的植物，\n即使在苦涩的海水中，也不愿改变自己。\n即使在逆境中，也不要放弃温柔的心灵。",
    "\n\n今天的幸运物是：弯弯曲曲的「蜥蜴尾巴」\n蜥蜴遇到潜在的危险时，大多数会断尾求生。\n若是遇到无法整理的情绪，那么该断则断吧。"
]
qianc = {
    "浅草百签": [
        "第一大吉\n七宝浮图塔\n高峯顶上安\n众人皆仰望\n莫作等闲看\n愿望：会充分地实现吧\n疾病：会治愈吧\n盼望的人：会出现吧\n遗失物：变得迟迟地才找到吧\n盖新居、搬家、嫁娶、旅行、交往等：全部很好吧\n万事行为谨慎粗心大意行事的话，就会发生意想之外的灾害吧",
        "第二小吉\n月被浮云翳\n立事自昏迷\n幸乞阴公佑\n何虑不开眉\n愿望：因为持续不断地努力，必定会实现\n疾病：虽然拖长，但是之后可以康复吧\n盼望的人：迟迟地才出现吧\n遗失物：不能找出来吧\n交往：要节制吧\n盖新居、搬家：都不坏吧\n结亲缘、旅行：顺利进行吧",
        "第三凶\n愁恼损忠良\n青宵一炷香\n虽然防小过\n闲虑觉时长\n愿望：难实现吧\n疾病：虽然拖长，但是会治好吧\n遗失物：难以找到吧\n盼望的人：要花很久的时间吧\n旅行：因为很坏，放弃吧\n盖新居搬家：勉勉强强地算好吧\n结婚交往：要节制吧",
        "第四吉\n累有兴云志\n君恩禄未封\n若逢侯手印\n好事始总总\n愿望：能实现吧\n如果这样的话，终生幸福吧\n疾病：变得迟迟地才会治好吧\n遗失物：迟迟地才找到吧\n盼望的人：会出现吧\n旅行：途中要忍耐各式各样的困难吧\n盖新居、搬家、结亲缘、交往：万事都好吧",
        "第五凶\n家道未能昌\n危危保祸殃\n暗云侵月桂\n佳人一炷香\n愿望：难以实现吧\n疾病：难治好吧\n遗失物：难找到吧\n盼望的人：不会出现吧\n盖新居、搬家：先放弃，暂时观察情况再说吧\n结亲缘、旅行、交往：因为万事凶恶，请诸行为慎重行事",
        "第六末吉\n宅墓鬼凶多\n人事有爻讹\n伤财防损失\n祈福始中和\n愿望：难以实现吧\n疾病：康复很花时间吧\n遗失物：难找到吧\n盼望的人：迟迟地才出现吧\n盖新居、搬家：好吧\n旅行：好吧\n结亲缘、交往：坏吧",
        "第七凶\n登舟待便风\n月色暗蒙眬\n遇碾香轮去\n高山千万重\n愿望：难以实现吧\n疾病：难以治愈吧\n遗失物：难以找到吧\n盼望的人：不会出现吧\n盖新居、搬家：换时间吧\n结亲缘、喜庆祝贺、旅行、交往：不好吧",
        "第八大吉\n勿头中见尾\n文华须得理\n禾刀自偶然\n当遇非常喜\n愿望：会实现吧\n疾病：会治好请注意养生吧\n遗失物：可以找到吧\n盼望的人：会出现吧\n盖新居、搬家、交往：是好事吧\n旅行：途中请不要粗心大意吧\n结亲缘：全都是好的吧",
        "第九大吉\n有名须得遇\n三望一朝迁\n贵人来指处\n华菓应时鲜\n愿望：会实现吧\n疾病：会治好吧\n遗失物：会找到吧\n盼望的人：会出现吧\n盖新居、搬家：好吧\n结亲缘、交往：全都好吧\n旅行：没问题吧",
        "第十大吉\n旧用多成破\n新更始见财\n改求云外望\n枯木遇春开\n愿望：会实现吧\n疾病：会治好吧\n遗失物：立刻会找到吧\n盼望的人：会出现吧\n盖新居、搬家：会变为好结果吧\n结亲缘、旅行、交往：全部变为好结果吧",
        "第十一大吉\n有禄兴家业\n文华达帝都\n云中乘好箭\n兼得贵人扶\n愿望：会充分地实现吧\n疾病：会治好吧\n遗失物：会找到吧\n盼望的人：会出现吧\n盖新居、搬家：好吧\n旅行：没问题吧\n结婚、交往：全部都能得到好结果吧",
        "第十二大吉\n杨柳遇春时\n残花发旧枝\n重重霜雪里\n黄金色更辉\n愿望：会实现吧\n疾病：会变好吧\n遗失物：会回来吧\n盼望的人：晚出现吧\n盖新居、搬家：会成为好结果吧\n旅行：没有阻碍吧\n结婚、交往：全都适当吧",
        "第十三大吉\n手把大阳辉\n东君发旧枝\n稼苗方欲秀\n犹更上云梯\n愿望：会实现吧\n疾病：会治好吧\n遗失物：立刻找就能找到吧\n盼望的人：会出现吧\n盖新居、搬家：好吧\n旅行：在春天和夏天好吧\n结婚、交往：全部都好吧",
        "第十四末吉\n玉石未分时\n忧心转更悲\n前途通大道\n花发应残枝\n愿望：很花时间但会实现吧\n疾病：会拖长吧，但是不会影响性命吧\n遗失物：难出现吧\n盼望的人：似乎会变得迟吧\n盖新居、搬家：不太好吧\n结婚：现在要节制，如果往后的话好吧\n旅行、交往：避开吧",
        "第十五凶\n年乖数亦孤\n久病未能苏\n岸危舟未发\n龙卧失明珠\n愿望：难以实现吧\n疾病：危险吧\n遗失物：难找回吧\n盼望的人：不会出现吧\n盖新居、搬家：都不好吧\n旅行、结亲缘：坏吧",
        "第十六吉\n破改重成望\n前途喜亦宁\n贵人相助处\n禄马照前程\n愿望：能被实现吧\n疾病：会康复吧\n遗失物：会出现吧\n盼望的人：会来吧\n盖新居、搬家：会有好结果吧\n旅行：好吧\n结亲缘、交往：全部会变成好结果吧",
        "第十七凶\n怪异防忧恼\n人宅见分离\n惜华还值雨\n杯酒惹闲非\n愿望：难实现吧\n疾病：康复需要长时间吧\n遗失物：不会出现吧\n盼望的人：不会出现吧\n盖新居、搬家：先放弃，暂时观察情况再说吧\n旅行：似乎引起坏的结果吧\n婚事、交往：全部不好吧",
        "第十八吉\n离暗出明时\n麻衣变绿衣\n旧忧终是退\n遇禄应交辉\n愿望：会实践吧\n疾病：会治好吧\n遗失物：会出现吧\n盼望的人：会出现吧\n盖新居、搬家：好吧\n旅行：好吧\n结亲缘、交往：全部变为好结果吧",
        "第十九末小吉\n家道生荆棘\n儿孙防虎威\n香前祈福厚\n方得免分离\n愿望：能实现一半吧\n疾病：虽然长期得病，但是不会危及性命吧\n遗失物：大概找回不来了吧\n盼望的人：变成迟迟地出现吧\n盖新居、搬家：不好也不坏吧\n旅行：节制比较好吧\n结婚：不会到达好的结果吧\n交往：节制吧",
        "第二十吉\n月出渐分明\n家财每每兴\n何言先有滞\n更变立功名\n愿望：能被实现吧\n疾病：会治好吧\n遗失物：会出现吧\n盼望的人：会来吧\n盖新居、搬家：好吧\n结婚、交往：全部都得到好结果吧\n旅行：好吧",
        "第二十一吉\n洗出经年否\n光华得再清\n所求终吉利\n重日照前程\n愿望：能被实现吧\n疾病：虽然会恢复但是切忌粗心大意\n遗失物：会出现吧\n盼望的人：会出现吧\n盖新居、搬家：好吧\n结婚：会得到好结果吧\n旅行、交往：全部好吧",
        "第二十二吉\n渐渐浓云散\n看看月再明\n逢春华菓秀\n雨过竹重青\n愿望：虽然能被实现，但是变得比较晚吧\n疾病：因为会治好，耐心等待康复吧\n遗失物：虽然会出现但很迟吧\n盼望的人：会出现吧\n盖新居、搬家：好吧\n结婚、旅行、交往：全都好吧",
        "第二十三吉\n红云随步起\n一箭中青霄\n鹿行千里远\n争知去路遥\n【争知】就是现代用语的『怎知』之意\n愿望：虽然会实现，但是要考虑能力吧\n疾病：难以康复吧\n遗失物：难以找到吧\n盼望的人：不能出现吧\n盖新居、搬家：好吧\n结婚、交往：好吧\n旅行：没问题吧",
        "第二十四凶\n三女莫相逢\n盟言说未通\n门里心肝挂\n缟素子重重\n（三女的意思是奸字）\n愿望：不会实现吧\n疾病：虽然拖很长，但会治好吧\n遗失物：变成到后来才找到吧\n盼望的人：不能出现吧\n盖新居、搬家：不好吧\n旅行：不好吧\n结婚、交往：变成不好的结果吧",
        "第二十五吉\n枯木逢春生\n前途必利亨\n亦得佳人箭\n乘车禄自行\n愿望：会实现吧\n疾病：会治好吧\n遗失物：会出现吧\n盼望的人：迟迟才来吧\n盖新居、搬家：似乎没问题\n结婚、旅行、交往：全部都变成好结果吧",
        "第二十六吉\n将军有异声\n进兵万里程\n争知临敌处\n道胜却虚名\n【争知】就是现代用语的『怎知』之意\n愿望：会实现吧\n疾病：会治好吧\n遗失物：会出现吧\n盼望的人：会出现吧\n盖新居、搬家：好吧\n旅行：好吧\n结婚、交往：会变成好结果吧",
        "第二十七吉\n望禄应重山\n花红喜悦颜\n举头看皎月\n渐出黑云间\n愿望：会实现吧\n疾病：会治好吧，但切忌粗心大意\n遗失物：会出现吧\n盼望的人：会出现吧\n盖新居、搬家：好吧\n旅行：非常好吧\n结婚、交往：全部都变成好结果吧",
        "第二十八凶\n意速无船渡\n波深必误身\n切须回旧路\n方可免灾迍\n迍：zhun(1,处境艰险，前进困难\n愿望：难以实现吧\n疾病：如果长期养生的话会治好吧\n遗失物：难出现吧\n盼望的人：变得迟迟地才出现吧\n盖新居、搬家：坏吧\n结婚、交往：坏吧",
        "第二十九吉\n忧轗渐消融\n求名得再通\n宝财临禄位\n当遇主人公\n轗：kan(3，形容车行颠簸不顺的样子，比喻人不得志)\n愿望：能被实现吧\n疾病：会治好吧\n遗失物：会出现吧\n盼望的人：会出现吧\n盖新居、搬家：好吧\n结婚、交往：全都好吧",
        "第三十半吉\n仙鹤立高枝\n防他暗箭亏\n井畔刚刀利\n户内更防危\n愿望：难实现吧\n疾病：危险吧\n遗失物：难出现吧\n盼望的人：不会出现吧\n盖新居、搬家：如果能祈求神佛的保佑，会变成勉强可以的结果吧\n旅行：坏吧\n结婚、交往：节制吧",
        "第三十一末吉\n鲲鲸未变时\n且守碧潭溪\n风云兴巨浪\n一息过天涯\n愿望：虽能被实现，但要考虑时机吧\n疾病：拖很久吧\n遗失物：变得迟迟地才出现吧\n盼望的人：变得迟迟地才出现吧\n盖新居、搬家：没阻碍吧\n旅行：好吧\n结婚、交往：好吧",
        "第三十二吉\n似玉藏深石\n休将故眼看\n一朝良匠别\n方见宝光寒\n愿望：会实现吧\n疾病：虽然会拖长，但是不会失去生命\n遗失物：会出现吧\n盼望的人：变得迟迟地才出现吧\n盖新居、搬家：好吧\n结婚、交往：全部和好结果有关吧",
        "第三十三吉\n枯木逢春艳\n芳菲再发林\n云间方见月\n前遇贵人钦\n愿望：能被实现吧\n疾病：会治好吧\n遗失物：会出现吧\n盼望的人：会出现吧\n盖新居、搬家：没有阻碍吧\n旅行：好吧\n结婚、交往：全都好吧",
        "第三十四吉\n腊木春将至\n芳菲喜再新\n鲲鲸兴巨浪\n举钩禄为真\n愿望：能被实现吧\n疾病：会治好吧\n遗失物：迟迟才出现吧\n盼望的人：迟吧\n盖新居、搬家：好吧\n旅行：好吧\n结婚、交往：全都和好结果相连吧",
        "第三十五吉\n射鹿须乘箭\n故僧引路归\n遇道同仙籍\n光华映晚晖\n愿望：能被实现吧\n疾病：会治好吧\n遗失物：会出现吧\n盼望的人：变迟才出现吧\n盖新居、搬家：没有障碍吧\n旅行：好吧\n结婚、交往：好吧",
        "第三十六末吉\n先损后有益\n如月之剥蚀\n玉兔待重生\n光华当满室\n愿望：稍后会实现吧\n疾病：虽然拖长，但可以治愈吧\n遗失物：难出现吧\n盼望的人：迟迟地才出现吧\n盖新居、搬家：应该先放弃，暂时多观察情况再说吧\n旅行：途中，似乎会有不好的事吧\n结亲缘、喜庆、交往：不好吧",
        "第三十七半吉\n阴叆未能通\n求名亦未逢\n幸然须有变\n一箭中双鸿\n愿望：难以实现吧\n疾病：变成迟迟地才好转吧\n遗失物：变成迟迟地才出现吧\n盼望的人：变成迟迟地才出现吧\n盖新居、搬家：好吧\n旅行：好吧\n结婚、交往：往后一点，变成好吧",
        "第三十八半吉\n月照天书静\n云生雾彩霞\n久想离庭客\n无事惹咨嗟\n愿望：难实现吧\n疾病：会拖长吧\n遗失物：难出现吧\n盼望的人：不会出现吧\n盖新居、搬家：不好也不坏吧\n旅行：先放弃，暂时观察情况再说吧\n结婚、交往：先放弃，暂时观察情况吧",
        "第三十九凶\n望用方心腹\n家乡被火灾\n忧危三五度\n由损断头财\n愿望：难以实现吧\n疾病：又坏又危险吧\n遗失物：难出现吧\n盼望的人：不会出现吧\n盖新居、搬家：避开比较好吧\n旅行：不好吧\n结婚、交往：招致坏结果吧",
        "第四十末小吉\n中正方成道\n奸邪恐惹愆\n壶中盛妙药\n非久去烦煎\n愆：qian(1，过失、罪过之意\n愿望：难以立刻地实现吧\n疾病：虽然拖长但会治好吧\n遗失物：会出现吧\n盼望的人：变成迟迟才地出现吧\n盖新居、搬家：好吧\n旅行：好吧\n结婚、交往：不好也不坏吧",
        "第四十一末吉\n有物不周旋\n须防损半边\n家乡烟火里\n祈福始安然\n愿望：难以实现吧\n疾病：会拖长吧\n遗失物：难出现吧\n盼望的人：变成迟迟地才出现吧\n盖新居、搬家：不好吧\n旅行：途中似乎有不好的事\n结婚、交往：会产生不好的结果吧",
        "第四十二吉\n桂华春将到\n云天好进程\n贵人相遇处\n暗月再分明\n愿望：会实现吧\n疾病：会治愈吧\n遗失物：会出现吧\n盖新居、搬家：好吧\n盼望的人：变成迟迟地才出现吧\n旅行：好吧\n结婚、交往：全都会变成好结果吧",
        "第四十三吉\n月桂将相满\n追鹿映山溪\n贵人乘远箭\n好事始相宜\n愿望：会实现吧\n疾病：虽然拖长但是会治好吧\n遗失物：难出现吧\n盼望的人：变成迟迟地才出现吧\n盖新居、搬家：好吧\n旅行：好吧\n结婚、交往：变成好结果吧",
        "第四十四吉\n盘中黑白子\n一着要先机\n天龙降甘泽\n洗出旧根基\n愿望：会实现吧\n疾病：会治愈吧\n遗失物：会出现吧\n盼望的人：变成迟迟地才出现吧\n盖新居、搬家：没问题吧\n旅行：好吧\n结婚、交往：全都好吧",
        "第四十五吉\n有意兴高显\n禄马引前程\n得遇云中箭\n芝兰满路生\n愿望：会实现吧\n疾病：会治好吧\n遗失物：迟迟地才出现吧\n盼望的人：变迟迟地才出现吧\n盖新居、搬家：好吧\n旅行：好吧\n结婚、交往：全都好结果相连吧",
        "第四十六凶\n雷发震天昏\n佳人独掩门\n交加文书上\n无事也遭迍\n迍：zhun(1处境艰险，前进困难\n愿望：难以实现吧\n疾病：会治好吧\n遗失物：难出现吧\n盼望的人：不会出现吧\n盖新居、搬家：现在放弃吧\n旅行：在途中有不好的事吧\n结婚、交往：会产生不好的结果吧",
        "第四十七吉\n更望身前立\n何期在晚成\n若遇重山去\n财禄自相迎\n愿望：会实现吧\n疾病：变成往后才会治好吧\n遗失物：会出现吧\n盼望的人：变得迟迟才出现吧\n盖新居、搬家：好吧\n旅行：在将来似乎有好事吧\n结婚、交往：全部都可得到好结果吧",
        "第四十八小吉\n见禄隔前溪\n劳心休更迷\n一朝逢好渡\n鸾凤入云飞\n愿望：如果一直抱持着正直的心的话，到后来能被实现吧\n疾病：虽然拖长，但将来会治好吧\n遗失物：会出现吧\n盼望的人：变成迟迟才来吧\n盖新居、搬家：虽然开始不好，但是到后来会变好吧\n结婚、交往、旅行：马马虎虎吧",
        "第四十九吉\n正好中秋月\n蟾蜍皎洁间\n暗云知何处\n故故两相攀\n愿望：会实现吧\n疾病：严重吧\n遗失物：难出现吧\n盼望的人：变成迟迟才出现吧\n盖新居、搬家：马马虎虎吧\n旅行：好吧\n结婚、交往：马马虎虎吧",
        "第五十吉\n有达宜更变\n重山利政逢\n前途相偶合\n财禄保亨通\n（重山即指两山相迭的出字）\n愿望：会实现吧\n疾病：会治好吧\n遗失物：会出现吧\n盼望的人：变迟吧\n盖新居、搬家：好吧\n旅行：成为好的旅行吧\n结婚、交往：成为好的结果吧",
        "第五十一吉\n修进甚功辛\n劳生未得时\n腾身游碧汉\n方得遇高枝\n愿望：会实现吧\n疾病：变成往后才治好吧\n遗失物：难出现吧\n盼望的人：变晚吧\n盖新居、搬家：好吧\n旅行：好事吧\n结婚、交往：会得到好结果吧",
        "第五十二凶\n有僭须惹讼\n兼有事交加\n门里防人危\n灾临莫叹嗟\n愿望：难实现吧\n疾病：会拖长吧\n遗失物：难出现吧\n盼望的人：不会出现吧\n盖新居、搬家：马马虎虎还算有点好吧\n旅行：因为不好，避开吧\n结婚、交往：不好也不坏吧",
        "第五十三吉\n久困渐能安\n云书降印权\n残花终结实\n时亨禄自迁\n愿望：能被实现吧\n疾病：会治好吧\n遗失物：变得迟迟才找到吧\n盼望的人：迟迟地才出现吧\n盖新居、搬家：好吧\n旅行：变成好的旅行吧\n结婚、交往：全都朝向好的方向发展吧",
        "第五十四凶\n身同意不同\n月蚀暗长空\n轮虽常在手\n鱼水未相逢\n愿望：难实现吧\n疾病：危险吧\n遗失物：难出现吧\n盼望的人：不会出现吧\n盖新居、搬家：暂时放弃，再观察看看吧\n结婚、交往：变成坏结果吧",
        "第五十五吉\n云散月重明\n天书得志诚\n虽然多阻滞\n花发再重荣\n愿望：会实现吧\n疾病：会治好吧\n遗失物：会找到吧\n盼望的人：变迟吧\n盖新居、搬家：好吧\n旅行：好吧\n结婚、交往：全都好吧",
        "第五十六末小吉\n生涯喜又忧\n未老先白头\n劳心千百度\n方遇贵人留\n愿望：难实现吧\n疾病：变成迟迟才治好吧\n遗失物：会出现吧\n盼望的人：迟迟才出现吧\n盖新居、搬家：半吉吧\n旅行：如果有一起同行的人的话好（安全）吧\n结婚、交往：马马虎虎还可以吧",
        "第五十七吉\n欲渡长江阔\n波深未自俦\n前津逢浪静\n重整钩鳌钩\n愿望：会实现吧\n疾病：虽然会治好，但会拖长吧\n遗失物：会出现吧\n盼望的人：变迟迟才出现吧\n盖新居、搬家：好吧\n旅行：坏吧\n结婚、交往：马马虎虎还可以吧",
        "第五十八凶\n有径江海隔\n车行峻岭危\n亦防多进退\n犹恐小人亏\n愿望：难实现吧\n疾病：不能安心吧\n遗失物：难出现吧\n盼望的人：不会出现吧\n盖新居、搬家：中止吧\n结婚、交往、旅行：坏吧",
        "第五十九凶\n去住心无定\n行藏亦未宁\n一轮清皎洁\n却被黑云乘\n愿望：难实现吧\n疾病：危险吧\n遗失物：难出现吧\n盼望的人：不会出现吧\n盖新居、搬家：坏吧\n旅行：似乎会发生坏事吧\n结婚、交往：得到坏结果吧",
        "第六十小吉\n高危安可涉\n平坦是延年\n守道当逢泰\n风云不偶然\n愿望：如果正心而行的话会实现吧\n疾病：会拖长吧\n遗失物：难出现吧\n盼望的人：不会出现吧\n盖新居、搬家：不好吧\n旅行：马马虎虎地算好吧\n结婚、交往：马马虎虎地算好吧",
        "第六十一半吉\n旧愆何日解\n户内保婵娟\n要逢十一口\n遇鼠过牛边\n愿望：难实现吧\n疾病：会拖长吧\n遗失物：难找到吧\n盼望的人：变迟吧\n盖新居、搬家：坏吧\n旅行：坏吧\n结婚、交往：不好吧",
        "第六十二大吉\n灾轗时时退\n名显四方扬\n改故重乘禄\n昴高福自昌\n轗：kan(3，形容车行颠簸不顺的样子，比喻人不得志)\n愿望：会实现吧\n疾病：会治好吧\n遗失物：会出现吧\n盼望的人：会出现吧\n盖新居、搬家：没问题吧\n旅行：好吧\n结婚、交往：全都好吧",
        "第六十三凶\n何故生荆棘\n佳人意渐疏\n久困重轮下\n黄金未出渠\n愿望：难实现吧\n疾病：难治愈吧\n遗失物：难找到吧\n盼望的人：不会出现吧\n盖新居、搬家：坏吧\n旅行：似乎会发生坏事吧\n结婚、交往：会产生坏结果吧",
        "第六十四凶\n安居且虑危\n情深主别离\n风飘波浪急\n鸳鸯各自飞\n愿望：难实现吧\n疾病：危险吧\n遗失物：不会出现吧\n盼望的人：不会出现吧\n盖新居、搬家：还可以吧\n旅行：还可以吧\n结婚、交往：不好吧",
        "第六十五末吉\n苦病兼防辱\n乘危亦未稣\n若见一阳后\n方可作良图\n愿望：以后会实现吧\n疾病：虽然拖长但会治好吧\n遗失物：不会出现吧\n盼望的人：变得迟迟才出现吧\n盖新居、搬家：好吧\n旅行：安全吧\n结婚、交往：得到还可以的好结果吧",
        "第六十六凶\n水滞少波涛\n飞鸿落羽毛\n重忧心绪乱\n闲事惹风骚\n愿望：难实现\n疾病：可疑，不明朗吧\n遗失物：难出现吧\n盼望的人：不会出现吧\n盖新居、搬家：坏吧\n旅行：坏吧\n结婚、交往：坏吧",
        "第六十七凶\n枯木未生枝\n独步上云岐\n岂知身未稳\n独自惹闲非\n愿望：难实现吧\n疾病：会拖长吧\n遗失物：难出现吧\n盼望的人：不会出现吧\n盖新居、搬家：多比较看看比较好吧\n旅行：不好吧\n结婚、交往：坏吧",
        "第六十八吉\n异梦生英杰\n前来事可疑\n芳菲春日暖\n依旧发残枝\n愿望：会实现吧\n疾病：会治好吧\n遗失物：会出来吧\n盼望的人：会出现吧\n盖新居、搬家：好吧\n旅行：好吧\n结婚、交往：全都好吧",
        "第六十九凶\n明月暗云浮\n花红一半枯\n惹事伤心处\n行舟莫远图\n愿望：难实现吧\n疾病：切忌粗心大意\n遗失物：难出现吧\n盼望的人：不会出现吧\n盖新居、搬家：坏吧\n旅行：放弃吧\n结婚、交往：坏吧",
        "第七十凶\n雷发庭前草\n炎火向天飞\n一心来赶禄\n争奈掩朱扉\n【争奈】就是宋代以后的『怎奈』、『无奈』之意（更早的唐代则是『争那』）\n愿望：难实现吧\n疾病：不能安心吧\n遗失物：难出现吧\n盼望的人：不会出现吧\n盖新居、搬家：避免吧\n结婚、旅行、交往：万事坏吧",
        "第七十一凶\n道业未成时\n何期两不宜\n事烦心绪乱\n飜做徘徊思\n愿望：难实现吧\n疾病：会拖长吧\n遗失物：难出现吧\n盼望的人：不会出现吧\n盖新居、搬家：坏吧\n结婚、旅行、交往：产生坏的结果吧",
        "第七十二吉\n户内防重厄\n花菓见分枝\n严霜纔过后\n方可始相宜\n愿望：后来会实现吧\n疾病：会拖长吧\n遗失物：变成迟迟才能找到吧\n盼望的人：迟迟才出现吧\n盖新居、搬家：还算好吧\n旅行：没有特别的阻碍吧\n结婚、交往：虽然还算好，但最后变得更好吧",
        "第七十三吉\n久暗渐分明\n登江绿水澄\n芝书从远降\n终得异人成\n愿望：变得往后才能被实现吧\n疾病：会治好吧\n遗失物：会出来吧\n盼望的人：会出现吧\n盖新居、搬家：好吧\n旅行：好吧\n结婚、交往：全都好吧",
        "第七十四凶\n蛇虎正交罗\n牛生二尾多\n交岁方成庆\n上下不能和\n愿望：难以实现吧\n疾病：不能安心吧\n遗失物：难出现吧\n盼望的人：不会出现吧\n盖新居、搬家：坏吧\n结婚、旅行、交往：坏吧",
        "第七十五凶\n孤舟欲过岸\n浪急渡人空\n女人立流水\n望月意情浓\n愿望：难实现吧\n疾病：陷入的话（若是病人的话）危险吧\n遗失物：不能找回来吧\n盼望的人：不会出现吧\n盖新居、搬家：坏吧\n旅行：坏吧\n结婚、交往：坏吧",
        "第七十六吉\n富贵天之佑\n何须苦用心\n前程应显迹\n久用得高临\n愿望：会实现吧\n疾病：会治好吧\n遗失物：会出来吧\n盼望的人：会出现吧\n盖新居、搬家：好吧\n旅行：好吧\n结婚、交往：全部都好吧",
        "第七十七凶\n累滞未能稣\n求名莫远图\n登舟波浪急\n咫尺隔天衢\n愿望：难实现吧\n疾病：不能安心吧\n遗失物：难找到吧\n盼望的人：不会出现吧\n盖新居、搬家：坏吧\n旅行：坏吧\n结婚、交往：坏吧",
        "第七十八大吉\n但存公道正\n何愁理去忠\n松柏苍苍翠\n前山禄马重\n愿望：会实现吧\n疾病：会治好吧\n遗失物：会出来吧\n盼望的人：会出现吧\n盖新居、搬家：好吧\n旅行：好吧\n结婚、交往：全都好吧",
        "第七十九吉\n残月未还光\n樽前非语伤\n户中有人厄\n祈福保青阳\n愿望：虽然能被实现但是大愿望不行吧\n疾病：虽然会拖长，但会治好吧\n遗失物：迟迟地才找到吧\n盼望的人：变迟才出现吧\n盖新居、搬家：好吧\n旅行：好吧\n结婚、交往：好吧",
        "第八十大吉\n深山多养道\n忠正帝王宣\n凤遂鸾飞去\n升高过九天\n愿望：会实现吧\n疾病：会治好吧\n遗失物：会出现吧\n盼望的人：会出现吧\n盖新居、搬家：好吧\n旅行：好吧\n结婚、交往：是好的，因为全部都保持谦虚的姿态，所以会招来好结果吧",
        "第八十一小吉\n道合须成合\n先忧事更多\n所求财宝盛\n更变得中和\n愿望：如果保持端正的心的话，会实现吧\n疾病：会治好吧\n遗失物：会出现吧\n盼望的人：会出现吧\n盖新居、搬家：好吧\n旅行：好吧\n结婚、交往：好吧",
        "第八十二凶\n火发应连天\n新愁惹旧愆\n欲求千里外\n要渡更无船\n愿望：难实现吧\n疾病：可疑，不明朗吧\n遗失物：难出现吧\n盼望的人：不会出现吧\n盖新居、搬家：坏吧\n旅行：多比较看看比较好吧\n结婚、交往：全都坏吧",
        "第八十三凶\n举步出云端\n高枝未可攀\n升头看皎月\n犹在黑云间\n愿望：难实现吧\n疾病：会拖长吧\n遗失物：难出现吧\n盼望的人：不会出现吧\n盖新居、搬家：坏吧\n旅行：危险吧\n结婚、交往：产生坏结果吧",
        "第八十四凶\n否极方无泰\n花开值晚秋\n人情不调备\n财宝鬼来偷\n愿望：难实现吧\n疾病：危险吧\n遗失物：难出现吧\n盼望的人：不会出现吧\n盖新居、搬家：坏吧\n旅行：不好吧\n结婚、交往：全部都产生坏的结果吧",
        "第八十五大吉\n望用何愁晚\n求名渐得宁\n云梯终有望\n归路入蓬瀛\n愿望：变成往后才会实现吧\n疾病：会治好吧\n遗失物：会出现吧\n盼望的人：会出现吧\n盖新居、搬家：好吧\n旅行：好吧\n结婚、交往：好吧",
        "第八十六大吉\n花发应阳台\n车行进宝财\n执文朝帝殿\n走马听声雷\n愿望：会实现吧\n疾病：会治好吧\n遗失物：会出现吧\n盼望的人：会出现吧\n盖新居、搬家：好吧\n旅行：好吧\n结婚、交往：全都好吧",
        "第八十七大吉\n凿石方逢玉\n淘沙始见金\n青霄终有路\n只恐不坚心\n愿望：能被实现吧\n疾病：会治好吧\n遗失物：会出现吧\n盼望的人：会出现吧\n盖新居、搬家：好吧\n结婚、交往：好吧",
        "第八十八凶\n作事不和同\n临危更主凶\n佳人生苦根\n闲虑两三重\n愿望：难实现吧\n疾病：危险吧\n遗失物：不会出现吧\n盼望的人：不会出现吧\n盖新居、搬家：坏吧\n旅行：坏吧\n结婚、交往：坏吧",
        "第八十九大吉\n一片无瑕玉\n从今好琢磨\n得遇高人识\n方逢喜气多\n愿望：能被实现吧\n疾病：会治好吧\n遗失物：不会出现吧\n盼望的人：会出现吧\n盖新居、搬家：好吧\n旅行：好吧\n结婚、交往：好吧",
        "第九十大吉\n一信向天飞\n秦川舟自归\n前途成好事\n应得贵人推\n愿望：会实现吧\n疾病：会治好吧\n遗失物：会出现吧\n盼望的人：会出现吧\n盖新居、搬家：好吧\n旅行：好吧\n结婚、交往：全部都好吧",
        "第九十一吉\n改变前途去\n月桂又逢圆\n云中乘禄至\n凡事可宜先\n愿望：如果守正道的话会实现吧\n疾病：会治好吧\n遗失物：会出现吧\n盼望的人：会出现吧\n盖新居、搬家：好吧\n旅行：好吧\n结婚、交往：好吧",
        "第九十二吉\n自幼常为旅\n逢春骏马骄\n前程宜进步\n得箭降青霄\n愿望：会实现吧\n疾病：会治好吧\n遗失物：会出现吧\n盼望的人：会出现吧\n盖新居、搬家：好吧\n旅行：好吧\n结婚、交往：好吧",
        "第九十三吉\n有鱼临旱池\n跳跃入波涛\n隔中须有望\n先且虑尘劳\n愿望：变成到后来能实现吧\n疾病：会拖长吧\n遗失物：难出现吧\n盼望的人：变迟吧\n盖新居、搬家：马马虎虎还算可以吧\n旅行：好吧\n结婚、交往：好吧",
        "第九十四半吉\n事忌樽前语\n人防小辈交\n幸乞阴公佑\n方免事敌爻\n愿望：不能按照所想的实现吧\n疾病：虽然会拖长但是不会危害生命吧\n要特别用心维持健康吧\n遗失物：会出现吧\n盼望的人：会出现吧\n盖新居、搬家：不好吧\n旅行：马马虎虎还算可以吧\n结婚、交往：勉强还算可以吧",
        "第九十五吉\n志气勤修业\n禄位未造逢\n若闻金鸡语\n乘船得便风\n愿望：能被实现吧\n疾病：变成迟迟才治好吧\n遗失物：变成迟迟地才出现吧\n盼望的人：迟迟地才出现吧\n盖新居、搬家：没有阻碍吧\n旅行：好吧\n结婚、交往：好吧",
        "第九十六大吉\n鸡逐凤同飞\n高林整羽仪\n棹舟须济岸\n宝货满船归\n愿望：能被实现吧\n但是，抱持全面谨慎的心是很重要的\n疾病：会治好吧\n遗失物：会出现吧\n盼望的人：会出现吧\n盖新居、搬家：好吧\n旅行：好吧\n结婚、交往：全部好吧",
        "第九十七凶\n雾罩重楼屋\n佳人水上行\n白云归去路\n不见月波澄\n愿望：难以实现吧\n疾病：危险吧\n遗失物：难出现吧\n盼望的人：不会出现吧\n盖新居、搬家：坏吧\n旅行：不好吧\n结婚、交往：坏吧",
        "第九十八凶\n欲理新丝乱\n闲愁足是非\n只困罗网里\n相见几人悲\n愿望：难以实现吧\n疾病：可疑，不明朗吧\n遗失物：难出现吧\n盼望的人：不会出现吧\n盖新居、搬家：坏吧\n旅行：坏吧\n结婚、交往：坏吧",
        "第九十九大吉\n红日当门照\n暗月再重圆\n遇珍须得宝\n颇有称心田\n愿望：能被实现吧\n在万事中要用谦虚的心吧\n疾病：会治好吧\n遗失物：会出现吧\n盼望的人：会出现吧\n盖新居、搬家：好吧\n旅行：好吧\n结婚、交往：好吧",
        "第一百签凶\n禄走白云间\n携琴走远山\n不遇神仙面\n空惹意阑珊\n愿望：难实现吧\n疾病：危险吧\n遗失物：难出现吧\n盼望的人：坏吧\n盖新居、搬家：坏吧\n旅行：坏吧\n结婚、交往：全部坏吧"
    ]
}


def genshinDraw():
    return random.choice(lucky) + random.choice(item)


def qianCao():
    return random.choice(qianc.get("浅草百签"))
if __name__ == '__main__':
    tarotChoice(0)
