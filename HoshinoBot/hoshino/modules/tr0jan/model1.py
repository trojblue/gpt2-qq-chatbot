# import random
# from hoshino import Service, aiorequests
# from hoshino.typing import CQEvent, CQHttpError
#
# # 测试群
# TEST_GROUP = [582368081]
# # 允许发言, 不包含测试群
# ALLOWED_GROUP = [863688150]
# # 发言几率
# RESPONSE_PROB = 0.05
# # API
# GPT2_API = "http://127.0.0.1:7777/message"
#
# # ==========================================================
#
# sv = Service('random-repeater', help_='随机复读机')
#
#
# @sv.on_prefix('teststring')
# async def send_help(bot, ev: CQEvent) -> None:
#     test_string = '''
# =====================- HoshinoBot使用说明 -================阿萨德阿萨德UG: Suc
# ceed to add prefix trigger `帮 284 nonebot] INFO: Succeeded to im
# ========※除这里中cnm这么写字可以吗※隐藏功能属于赠品 不保证可用性※本bot开源，可自行搭建这是一段很长的文字文字文
# 字文字文字文字文字※您的支阿达阿萨德阿萨德力※※调教时请注意使用频率，您的滥用可能会导致bot账号被封禁
# '''.strip()
#     await bot.send(ev, test_string)
#
#
# def is_valid_for_response(ev: CQEvent) -> bool:
#     """用来判断是否进行回复"""
#     if ev.group_id == TEST_GROUP:  # 测试群
#         return True
#
#     elif ev.group_id in ALLOWED_GROUP:  # 允许回复的群
#         if len(ev.message.extract_plain_text()) not in [5, 15]:
#             return False
#         if random.random() > RESPONSE_PROB:
#             return False
#
#         return True
#
#     # 不在允许群内
#     return False
#
#
# @sv.on_prefix('聊')
# async def random_repeater(bot, ev: CQEvent) -> None:
#     if not is_valid_for_response(ev):
#         return
#
#     payload = {
#         "msg": ev.message.extract_plain_text(),
#         "group": ev.group_id,
#         "qq": ev.user_id
#     }
#
#     sv.logger.debug(payload)
#     api = GPT2_API
#     GPT2_response = await aiorequests.post(api, data=payload, timeout=10)
#     GPT2_response = await GPT2_response.json()
#     sv.logger.debug(GPT2_response)
#
#     GPT2_loss = GPT2_response['loss']
#     GPT2_msg = GPT2_response['msg']
#
#     if not GPT2_msg:
#         return
#
#     if ev.group_id in TEST_GROUP:  # 测试群, 发送所有结果
#         await bot.send(ev, GPT2_msg)
#
#     elif GPT2_loss < 2.5:  # 其他群: 满足概率 + loss够小
#         await bot.send(ev, GPT2_msg)
#
#     return
