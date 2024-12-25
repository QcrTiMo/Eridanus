#random_str,file_upload_toUrl,and so on.
from plugins.core.llmDB import get_user_history, update_user_history

"""
从processed_message构造openai标准的prompt
"""


async def prompt_elements_construct(precessed_message):
    prompt_elements=[]

    #{"role": "assistant","content":[{"type":"text","text":i["text"]}]}
    for i in precessed_message:
        if "text" in i:
            prompt_elements.append({"type":"text","text":i["text"]})
        elif "image" in i:
            prompt_elements.append({"type":"image_url","image_url":i["image"]["url"]})
        elif "record" in i:
            pass
            #prompt_elements.append({"type":"voice","voice":i["voice"]})
    return {"role": "user","content":prompt_elements}
async def construct_openai_standard_prompt(processed_message, user_id, config):
    message=await prompt_elements_construct(processed_message)
    history = await get_user_history(user_id)
    original_history = history.copy()  # 备份，出错的时候可以rollback
    history.append(message)

    full_prompt = [
        {"role": "system", "content": [{"type": "text", "text": config.api["llm"]["system"]}]},
    ]
    full_prompt.extend(history)
    await update_user_history(user_id, history)  # 更新数据库中的历史记录
    return full_prompt, original_history
"""
gemini标准prompt构建
"""
async def gemini_prompt_elements_construct(precessed_message):
    prompt_elements=[]

    #{"role": "assistant","content":[{"type":"text","text":i["text"]}]}
    for i in precessed_message:
        if "text" in i:
            prompt_elements.append({"type":"text","text":i["text"]})
        elif "image" in i:
            prompt_elements.append({"type":"image_url","image_url":i["image"]["url"]})
        elif "record" in i:
            pass
            #prompt_elements.append({"type":"voice","voice":i["voice"]})
    return {"role": "user","content":prompt_elements}
async def construct_gemini_standard_prompt(processed_message, user_id, config):
    message=await gemini_prompt_elements_construct(processed_message)
    history = await get_user_history(user_id)
    original_history = history.copy()  # 备份，出错的时候可以rollback
    history.append(message)

    full_prompt = [
        {"role": "system", "content": [{"type": "text", "text": config.api["llm"]["system"]}]},
    ]
    full_prompt.extend(history)
    await update_user_history(user_id, history)  # 更新数据库中的历史记录
    return full_prompt, original_history