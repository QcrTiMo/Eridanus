#为func_calling提供函数映射
import inspect
import json

from run.basic_plugin import call_weather_query
from run.user_data import call_user_data_register,call_user_data_query,call_user_data_sign,call_change_city,call_change_name,call_permit
def func_map():
    tools=[
        {
          "type": "function",
          "function": {
            "name": "weather_query",
            "description": "Get the current weather in a given location",
            "parameters": {
              "type": "object",
              "properties": {
                "location": {
                  "type": "string",
                  "description": "The city and state, e.g. 上海"
                },
              },
              "required": ["location"]
            }
          }
        }
      ]
    return tools

def gemini_func_map():
    with open('plugins/core/gemini_func_call.json', 'r',encoding='utf-8') as f:
        data = json.load(f)
    tools = data
    return tools

async def call_func(bot,event,config,func_name, params):

    """
    动态调用已导入的函数。

    参数:
        func_name (str): 函数名。
        params (str): JSON 字符串，包含函数参数。

    返回:
        异步函数的返回值。
    """
    print(f"Calling function '{func_name}' with parameters: {params}")
    # 从全局作用域中获取函数对象
    func = globals().get(func_name)

    if func is None:
        raise ValueError(f"Function '{func_name}' not found.")

    # 检查是否为可调用对象
    if not callable(func):
        raise TypeError(f"'{func_name}' is not callable.")

    # 检查是否为异步函数
    if not inspect.iscoroutinefunction(func):
        raise TypeError(f"'{func_name}' is not an async function.")

    # 将 JSON 字符串解析为字典


    # 调用函数并传入参数
    return await func(bot,event,config,**params)