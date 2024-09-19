from core.prompt import say, select
import game

id = "归云派大殿"
grid_x = 0
grid_y = 1


def callback():
    say(who="卫泓", text="这大殿可真气派。")
    say(who="李梦卿", text="那当然，这还只是外门的接待区，我听说他们内门的建筑更恢弘呢！")
    say(who="张铭", text="那这入门的要求会不会很高？")
    say(who="陈远舟", text="凡事不可强求，我们尽力而为，顺其自然就好。")
    game.update_quest(id="初入归云", finished=True)
    say(who="纪瑶华", text="这位道友，你也是来加入归云派的吧？")
    answer = select(who="纪瑶华", text="我看你神情自若，似乎对入门考核很有把握，你难道不紧张吗？",
                    choices=["呃，我就不参加了。", "我注定会成为归云派的一员。"])
    if answer == 0:
        say(who="纪瑶华", text="道友可别怯场呀。来都来了，不试试又怎知自己不行？")
    else:
        say(who="纪瑶华", text="哈哈，看来道友很有信心呀。那祝你顺利通过考核。")
    say(who="李兴", text="诶？你们看天上那是什么？")
    say(text="众人正说话间，突然天地变色，电闪雷鸣。")
    say(text="随即地动山摇，火雨天降，宛如末日来临一般。")
    say(text="只见一颗巨大的陨石砸向不远处的紫云山主峰。顷刻间，整座山化为乌有。")
    say(text="周遭各峰也在火雨的冲击下摇摇欲坠，放眼望去，归云派的上百座楼台亭阁尽数崩塌。")
    say(text="千钧一发之际，几道奇异的光芒护住了山门外的散修。众人这才反应过来，匆匆逃到山下。")
    say(text="正当一众散修惊魂未定之时，有一人从空中跌落下来，看装束似乎是归云派的弟子。")
    say(text="在场众人面面相觑，不知如何是好。此时一道身影从远处匆匆赶来。")
    say(text="他冲到这位遍体鳞伤、昏迷不醒的归云派弟子身旁，面露焦急之色。")
    game.position_room("归云派山下")
