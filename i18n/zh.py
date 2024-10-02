import game


language_name = "简体中文"
title = "\
 [light_goldenrod2] ⎽⎽⎽⎽⎽\n\
 │[on light_goldenrod2]灵 一[/on light_goldenrod2]│\n\
 │[on light_goldenrod2]田 方[/on light_goldenrod2]│\n\
  ⎺⎺⎺⎺⎺ [/light_goldenrod2]"

main_menu_continue = "再续前缘"
main_menu_new = "初入仙山"
main_menu_load = "读取进度"
main_menu_settings = "游戏设置"
main_menu_quit = "退出游戏"
main_menu_language = "游戏语言"

character_creation = "主角设定"
character_creation_male = "男"
character_creation_female = "女"
character_creation_gender = "性别"
character_creation_last_name = "姓"
character_creation_first_name = "名"


def _get_character_name(surname, given_name):
    return f"{surname}{given_name}"


saved = "存档成功"
loading = "载入中"
hint = "请按回车键继续"

quest_finished = "任务完成"
quest_received = "接收任务"

intro_cutscene_01 = "%pcname小友，\n    别来无恙？数月前于山中偶遇，相谈甚欢。我观小友于灵植一道颇有天赋，且有向道修行之心。如今正有一桩机缘送于小友：我归云派门下产业众多，其中一处山谷，名曰「山岚谷」，虽灵气丰沛，山清水秀，但苦于门中无人擅长耕作，以至荒废许久。"
intro_cutscene_02 = "    前几日门中长老议事，正巧有人提议招募灵植散修如我归云派，专门打理山岚谷，并以此间产出的灵植草药向门派换取功法丹药，助其修行。此议正合小友所需，不知小友意下如何？"
intro_cutscene_03 = "    若小友有意，可凭此信来归云派寻我详谈。"
intro_cutscene_04 = "    归云派炼丹长老 左明渊"

归云派山门 = "归云派山门"
归云派大殿 = "归云派大殿"
归云派山脚 = "归云派山脚"
回春堂 = "回春堂"
落霞客栈 = "落霞客栈"

归云派弟子 = "归云派弟子"
归云派弟子_01 = "这位道友留步，不知来我归云派所为何事？"
归云派弟子_01_01 = "将左长老的信物交给他查看。"
归云派弟子_02 = "原来你就是%pcname？太好了，左长老命我前来接引。我已在此恭候多时了。"
归云派弟子_03 = "说起来那山岚谷也是丰饶富庶之地。只可惜我派剑修当道，灵植一道无甚人才，这才让它荒废至今。"
归云派弟子_04 = "此刻左长老正在主峰议事。长老他让我将这山岚谷禁制的符咒先交给你，晚点他会亲自带你过去。"
归云派弟子_04_01 = "前面似乎聚了很多人，可是发生了什么事？"
归云派弟子_05 = "哦，归云派最近正在招募新弟子，他们都是前来参加入门考核的散修。"
归云派弟子_06 = "我派考核向来严格，能入选者不过十之一二。不过道友是左长老亲自选定之人，自然不必参加考核。"
归云派弟子_07 = "还请道友先随他们一起在大殿前等候片刻。我这就去通禀一声。"
归云派山门_01 = "使用命令[东][南][西][北]可操作角色行走"
归云派山门_02 = "向[bold]北[/bold]走前往[bold]大殿[/bold]，和其他人一起等候通禀吧。"
归云派山门_03 = "现在不是闲逛的时候，先去殿前等候吧。"

初入归云 = "初入归云"
初入归云_01 = "向北走前往归云派大殿处等候"
