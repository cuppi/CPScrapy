import os


class LuaLoader:
    @staticmethod
    def load_script(file_name: str):
        lua_script: str = ''
        with open(os.path.join(os.getcwd(), 'HelloScrapy', 'lua_script', file_name), 'r') as f:
            lua_script += f.read()
        return lua_script
