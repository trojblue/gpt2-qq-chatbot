# gpt2-qq-chatbot
QQ chatbot with gpt-2 integration; based on [nonebot](https://github.com/nonebot/nonebot) framework

Skills involved for this project:
- Flask (for sending data between different python programs)
- Decorator pattern and Event-Driven-Architecture

## Structure
`Hoshibobot/modules/tr0jan`: listens to `.c` prefix events in groupchat;

`GPT2-Chitchat/interact_mmi_coolq.py`: generating responses and send back to bot through flask server


## Setup

**Unfortunately the project is no longer working, because Tencent has banned the usage of third party robots on the QQ platform, including nonebot, which is the underlying framework of this project :(**

1. follow instructions on [HoshinoBot](https://github.com/Ice-Cirno/HoshinoBot) repository and run `run.py` in `/HoshinoBot` folder
2. follow instructions on [GPT2-chitchat](https://github.com/yangjianxin1/GPT2-chitchat) repository and run `interact_mmi_coolq.py` in `/GPT2-chitchat` folder
3. when `.c` prefix is detected in a chatroom, the bot will respond by running the gpt-2 model and evaluating the losses.
 

