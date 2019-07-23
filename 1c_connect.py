#coding=UTF-8
import pythoncom
import win32com.client
V83_CONN_STRING = 'File="E:\\123";Usr="Администратор";Pwd="";'
pythoncom.CoInitialize()
V83 = win32com.client.Dispatch("V83.COMConnector").Connect(V83_CONN_STRING)

q = '''
Выбрать
Номенклатура.Наименование КАК NameNom
Из
Справочник.Номенклатура КАК Номенклатура
Где
Номенклатура.ЭтоГруппа = Истина
'''

query = V83.NewObject("Query", q)

selector = query.Execute().Choose()

while selector.next():
    print(selector.NameNom)
