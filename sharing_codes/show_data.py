
import json

def show_json_datas(json_results):
    print json.dumps(json_results, encoding="utf-8", ensure_ascii=False, sort_keys=False, indent=4)