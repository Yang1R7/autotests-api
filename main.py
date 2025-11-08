# import json
# json_data = '{"name": "Maxim", "city": "Moscow", "age": "19"}'
# parsed_data = json.loads(json_data)
# # print(type(parsed_data))
#
# data = {
#     "name": "Максим",
#     "age": 23,
#     "city": "Максим"
# }
#
# dump_data = json.dumps(data, indent=3)
# # print(dump_data, )
# # with open("json_example.json","r", encoding="utf-8") as file:
# #     data = json.load(file)
# #     print(data, type(data))
#
# with open("json_data.json", "w", encoding="utf-8") as file:
#     json.dump(data, file, indent=2, ensure_ascii=False)
import uuid

print(uuid.uuid4())
