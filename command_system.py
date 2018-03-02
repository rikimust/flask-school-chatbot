command_list = []

class Command:
   def __init__(self):
       self.__keys = []
       self.__aliases = []
       self.description = ''
       command_list.append(self)

   def __get_keys(self):
       return self.__keys

   def __set_keys(self, keys_list):
       for key in keys_list:
           self.__keys.append(key)

   def __get_aliases(self):
       return self.__aliases

   def __set_aliases(self, aliases_list):
       for alias in aliases_list:
           self.__aliases.append(alias)

   keys = property(__get_keys, __set_keys)
   aliases = property(__get_aliases, __set_aliases)

   def process(self):
       pass