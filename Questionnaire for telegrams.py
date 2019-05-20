

import telebot
import requests
import os
import json
import random





def clear_res():
	qu={

		'вопрос№1':
			["Как вы отсноситесь к жаре ?", ["погода", "явление_стихии", "градусы"],
				[
					[0,0]
				]
			],
		'вопрос№2':
			["Как вы отсноситесь к холоду ?", ["погода", "явление_стихии", "градусы"],
				[
					[0,0]
				]
			],

		'вопрос№3':
			["Вы любите пить алкоголь ?", ["погода", "явление_стихии", "градусы"],
				[
					[0,0]
				]
			],
		'вопрос№4':
			["Смысл жизни в чем ?", ["погода", "явление_стихии", "градусы"],
				[
					[0,0]
				]
			],
		'вопрос№5':
			["Если бы вы вам предстояло жить всю жизнь с одним человеком какого бы вы выбрали?", ["погода", "явление_стихии", "градусы"],
				[
					[0,0]
				]
			],
		'вопрос№6':
			["Ненависть к хомякам это хорошо ?", ["погода", "явление_стихии", "градусы"],
				[
					[0,0]
				]
			],
		'вопрос№7':
			["Что такое любовь для вас ?", ["погода", "явление_стихии", "градусы"],
				[
					[0,0]
				]
			],
		'вопрос№8':
			["Что такое общественное мнение ?", ["погода", "явление_стихии", "градусы"],
				[
					[0,0]
				]
			],
		'вопрос№9':
			["Когда человек счастлив ?", ["погода", "явление_стихии", "градусы"],
				[
					[0,0]
				]
			],
		'вопрос№10':
			["Почему некоторые люди богатые а другие бедные ?", ["погода", "явление_стихии", "градусы"],
				[
					[0,0]
				]
			],
		'вопрос№11':
			["Вы верете в то что справедливость существует  ?", ["погода", "явление_стихии", "градусы"],
				[
					[0,0]
				]
			],
		'вопрос№12':
			["Что для вас Дом это - ", ["погода", "явление_стихии", "градусы"],
				[
					[0,0]
				]
			],

		'вопрос№13':
			["Деньги это - ", ["погода", "явление_стихии", "градусы"],
				[
					[0,0]
				]
			],

		'вопрос№14':
			["Почему люди не получают что хотят ?", ["погода", "явление_стихии", "градусы"],
				[
					[0,0]
				]
			],

		'вопрос№15':
			["Что радует вашу семью ?", ["погода", "явление_стихии", "градусы"],
				[
					[0,0]
				]
			],

		'вопрос№16':
			["Люблю думать о высоком но живу низко", ["погода", "явление_стихии", "градусы"],
				[
					[0,0]
				]
			]

		}
	with open("вопрос.json",'w',encoding="utf-8") as file_handler:
		json.dump(qu,file_handler,sort_keys=False,ensure_ascii=False)
	with open("ответы.json",'w',encoding="utf-8") as file_handler:
		json.dump(qu,file_handler,sort_keys=False,ensure_ascii=False)




def Запись(ответ):
	# ответ =['вопрос№1','00000','-2']
	print(ответ)
	with open("вопрос.json",'r',encoding="utf-8") as file_handler:
		вопрос = json.load(file_handler)
	with open("ответы.json",'r',encoding="utf-8") as file_handler:
		memory_qu = json.load(file_handler)
		memory_qu[ответ[0]][2].append([ответ[1],ответ[2]])
	with open("ответы.json",'w',encoding="utf-8") as file_handler:
		json.dump(memory_qu,file_handler,sort_keys=False,ensure_ascii=False)




i = 0
def handle_messages(messages):
	def Проверка(memory_qu,QU):
		nonlocal вопрос
		nomer_qu = random.choice(вопрос)
		#print('---- {} ----\n'.format(nomer_qu))
		res = 0
		for x in memory_qu[nomer_qu][2]:
			# print(x[0])
			if QU == x[0]:
				# print('----------+ + + +---------')
				# print(x[0])
				# print(QU)
				# print('----------+ + + +---------')
				вопрос.pop(вопрос.index(nomer_qu))
				# print(вопрос)
				if вопрос == []:
					# print('**********')
					return 1
				nomer_qu=random.choice(вопрос)
				Результат_повторный = Проверка(memory_qu,QU)
				# print('Повторный цикл - {}'.format(Результат_повторный))
				if Результат_повторный == 1:
					return 1
				if Результат_повторный == nomer_qu:
					return nomer_qu
				res = 0
				return nomer_qu
			else:
				res = 1
		if res == 1:
			#print('--- В вопросе |{}| нет такого ID ---'.format(nomer_qu))
			return nomer_qu


	global i
	message = messages[-1]
	QU = message.from_user.id

	if i == 0:
		with open("вопрос.json",'r',encoding="utf-8") as file_handler:
			all_qu = json.load(file_handler)
		with open("ответы.json",'r',encoding="utf-8") as file_handler_re:
			memory_qu = json.load(file_handler_re)
		вопрос = [*all_qu]
		Результат = Проверка(memory_qu,QU)
		if Результат == 1:
			Результат = 'Вы ответили на все вопросы'
		# print('Основной цикл - {}'.format(Результат))
		i=1


	if i == 1:
		try:
			# print(all_qu[Результат][0])
			bot.send_message(message.from_user.id,'{} - {}'.format(Результат,all_qu[Результат][0]))
			ответ = [Результат,message.from_user.id,message.text]
			Запись(ответ)
		except KeyError:
			print([Результат,message.from_user.id,message.text])
			bot.send_message(message.from_user.id,'Благодарю - {}'.format(Результат))
		i=0
					




with open('Token.txt','r') as file_tok:
	token = file_tok.read()

bot= telebot.TeleBot(token)
# clear_res()
bot.set_update_listener(handle_messages)
bot.polling()