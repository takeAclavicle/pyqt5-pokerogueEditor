import os
import json
from py_mini_racer import MiniRacer
from KEY_DICT import dex_map, starter_map


class Cryptor:
    def __init__(self, key):
        self.key = key
        self.en_text = ''
        self.dict_data = {}
        self.dict_slot = {}

        parent_path = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(parent_path, 'js\\cryptography-js.min.js')

        self.ctx = MiniRacer()
        self.ctx.eval(open(file_path, 'r', encoding='utf-8').read())

    def encrypt(self, TYPE: int):
        if TYPE == Cryptor.DATA and self.dict_data != {}:
            self.en_text = self.ctx.call("encrypt", json.dumps(self.dict_data, ensure_ascii=False, indent=4), self.key)
        elif TYPE == Cryptor.SLOT and self.dict_slot != {}:
            self.en_text = self.ctx.call("encrypt", json.dumps(self.dict_slot, ensure_ascii=False, indent=4), self.key)
        else:
            return False
        return True

    def decrypt(self):
        if self.en_text.startswith('U2'):
            de_text = self.ctx.call("decrypt", self.en_text, self.key)
            dict = json.loads(de_text)
            if 'starterData' in dict:
                self.dict_data = dict
                if '$' in de_text:
                    self.repairKey()
                return Cryptor.DATA
            elif 'party' in dict:
                self.dict_slot = dict
                return Cryptor.SLOT
            else:
                return Cryptor.ERROR
        else:
            return Cryptor.ERROR

    def repairKey(self):
        for k, v in self.dict_data['dexData'].items():
            for tmp_k in list(v.keys()):
                if tmp_k in dex_map: v[dex_map[tmp_k]] = v.pop(tmp_k)

        for k, v in self.dict_data['starterData'].items():
            for tmp_k in list(v.keys()):
                if tmp_k in starter_map: v[starter_map[tmp_k]] = v.pop(tmp_k)

    ERROR = 0
    DATA = 1
    SLOT = 2


# if __name__ == '__main__':
    # with open('result.json', 'r', encoding='utf-8') as f:
    #     fileContent = f.read()
    # c = Cryptor('x0i2O7WRiANTqPmZ')
    # c.dict_data = json.loads(fileContent)
    # c.encrypt()
    # with open('result.prsv', 'w', encoding='utf-8') as f:
    #     f.write(c.en_text)
    # c.en_text = fileContent
    # start_time = time.time()
    # c.decrypt()
    # with open('result.json', 'w', encoding='utf-8') as f:
    #     json.dump(c.de_json, f, ensure_ascii=False, indent=4)
    # print("解密结果:", c.de_json)
    # print("花费时间:", time.time() - start_time)
