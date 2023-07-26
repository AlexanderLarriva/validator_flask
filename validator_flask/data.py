import sys
import uuid
from flask import session


class Repository: # Определение класса, который является оболочкой над сессией Flask для хранения и извлечения данных. 
    def content(self): # Метод возвращает все значения, которые в данный момент хранятся в сессии. 
        return session.values()

    def find(self, id): # Метод пытается найти и вернуть элемент из сессии по его идентификатору. 
        try:
            return session[id]
        except KeyError:
            sys.stderr.write(f'Wrong item id: {id}')
            raise

    def save(self, item): # Метод сохраняет элемент в сессии. 
        item['id'] = str(uuid.uuid4()) # Генерация уникального идентификатора
        session[item['id']] = item  # Сохраняет элемент в сессии под этим уникальным идентификатором.
