import asyncio
import telebot
from telebot.async_telebot import AsyncTeleBot
import requests
import json

TOKEN = '5910116610:AAHiRBYEf9KkPzsNoACoSz0JY4UygqlIQqA'
bot = AsyncTeleBot(TOKEN)
URL_pdf = 'pdf_live_Q0j0WxI8ItS5wLS5hYxOI4RMAsDyMPUED7dIPu4Gcug'


def xlsPdf(doc,filename):
    instructions = {
      'parts': [
        {
          'file': 'document'
        }
      ]
        }

    response = requests.request(
      'POST',
      'https://api.pspdfkit.com/build',
      headers = {
        'Authorization': 'Bearer pdf_live_Q0j0WxI8ItS5wLS5hYxOI4RMAsDyMPUED7dIPu4Gcug'
      },
      files = {
        'document': open(doc, 'rb')
      },
      data = {
        'instructions': json.dumps(instructions)
      },
      stream = True
    )

    if response.ok:
      with open('C:\\'+filename+'.pdf', 'wb') as fd:
        for chunk in response.iter_content(chunk_size=8096):
          fd.write(chunk)
    else:
      print(response.text)
      exit()

def xlsxPdf(doc,filename):
    instructions = {
      'parts': [
        {
          'file': 'document'
        }
      ]
    }

    response = requests.request(
      'POST',
      'https://api.pspdfkit.com/build',
      headers = {
        'Authorization': 'Bearer pdf_live_Q0j0WxI8ItS5wLS5hYxOI4RMAsDyMPUED7dIPu4Gcug'
      },
      files = {
        'document': open(doc, 'rb')
      },
      data = {
        'instructions': json.dumps(instructions)
      },
      stream = True
    )

    if response.ok:
      with open('C:\\'+filename+'.pdf', 'wb') as fd:
        for chunk in response.iter_content(chunk_size=8096):
          fd.write(chunk)
    else:
      print(response.text)
      exit()

def docPdf(doc,filename):
    instructions = {
  'parts': [
    {
      'file': 'document'
    }
  ]
    }

    response = requests.request(
      'POST',
      'https://api.pspdfkit.com/build',
      headers = {
        'Authorization': 'Bearer pdf_live_Q0j0WxI8ItS5wLS5hYxOI4RMAsDyMPUED7dIPu4Gcug'
      },
      files = {
        'document': open(doc, 'rb')
      },
      data = {
        'instructions': json.dumps(instructions)
      },
      stream = True
    )

    if response.ok:
      with open('C:\\'+filename+'.pdf', 'wb') as fd:
        for chunk in response.iter_content(chunk_size=8096):
          fd.write(chunk)
    else:
      print(response.text)
      exit()

def docxPdf(doc,filename):
    instructions = {
      'parts': [
        {
          'file': 'document'
        }
      ]
    }

    response = requests.request(
      'POST',
      'https://api.pspdfkit.com/build',
      headers = {
        'Authorization': 'Bearer pdf_live_Q0j0WxI8ItS5wLS5hYxOI4RMAsDyMPUED7dIPu4Gcug'
      },
      files = {
        'document': open(doc, 'rb')
      },
      data = {
        'instructions': json.dumps(instructions)
      },
      stream = True
    )

    if response.ok:
      with open('C:\\'+filename+'.pdf', 'wb') as fd:
        for chunk in response.iter_content(chunk_size=8096):
          fd.write(chunk)
    else:
      print(response.text)
      exit()

def pptxPdf(doc,filename):
    instructions = {
      'parts': [
        {
          'file': 'document'
        }
      ]
    }
    response = requests.request(
      'POST',
      'https://api.pspdfkit.com/build',
      headers = {
        'Authorization': 'Bearer pdf_live_Q0j0WxI8ItS5wLS5hYxOI4RMAsDyMPUED7dIPu4Gcug'
      },
      files = {
        'document': open(doc, 'rb')
      },
      data = {
        'instructions': json.dumps(instructions)
      },
      stream = True
    )

    if response.ok:
      with open('C:\\'+filename+'.pdf', 'wb') as fd:
        for chunk in response.iter_content(chunk_size=8096):
          fd.write(chunk)
    else:
      print(response.text)
      exit()

def pptPdf(doc,filename):
    instructions = {
      'parts': [
        {
          'file': 'document'
        }
      ]
    }

    response = requests.request(
      'POST',
      'https://api.pspdfkit.com/build',
      headers = {
        'Authorization': 'Bearer pdf_live_Q0j0WxI8ItS5wLS5hYxOI4RMAsDyMPUED7dIPu4Gcug'
      },
      files = {
        'document': open(doc, 'rb')
      },
      data = {
        'instructions': json.dumps(instructions)
      },
      stream = True
    )

    if response.ok:
      with open('C:\\'+filename+'.pdf', 'wb') as fd:
        for chunk in response.iter_content(chunk_size=8096):
          fd.write(chunk)
    else:
      print(response.text)
      exit()

@bot.message_handler(commands=['start'])
async def msg(message: telebot.types.Message):
    await bot.send_message(message.chat.id, 'Olá '+message.chat.first_name+', tudo bem?'
                                            '\nEnvie-me um arquvo para que eu possa trabalhar...', parse_mode='HTML', disable_web_page_preview=True)


#reconhece Documento
@bot.message_handler(content_types=['document'])
async def new_message(message: telebot.types.Message):
    result_message = await bot.send_message(message.chat.id, '<i>Lendo seu arquivo...</i>', parse_mode='HTML', disable_web_page_preview=True)
    file_path = await bot.get_file(message.document.file_id)
    downloaded_file = await bot.download_file(file_path.file_path)
    arq_type = file_path.file_path.split('.')[1]
    arq_name = message.document.file_name.split('.')[0]

#verifica XLS
    if arq_type == 'xls':
        with open('file.xls', 'wb') as new_file:
            new_file.write(downloaded_file)
        xlsPdf('file.xls',arq_name)
        await bot.send_document(chat_id = message.chat.id, document=open('C:\\'+arq_name+'.pdf','rb'))
        await bot.edit_message_text(chat_id=message.chat.id, message_id=result_message.id, text='<i>Feito!</i>', parse_mode='HTML')

#verifica XLSX
    if arq_type == 'xlsx':
        with open('file.xlsx', 'wb') as new_file:
            new_file.write(downloaded_file)
        xlsxPdf('file.xlsx',arq_name)
        await bot.send_document(chat_id = message.chat.id, document=open('C:\\'+arq_name+'.pdf','rb'))
        await bot.edit_message_text(chat_id=message.chat.id, message_id=result_message.id, text='<i>Feito!</i>', parse_mode='HTML')

#verifica doc
    elif arq_type == 'doc':
        with open('file.doc', 'wb') as new_file:
            new_file.write(downloaded_file)
        docPdf('file.doc',arq_name)
        await bot.send_document(chat_id = message.chat.id, document=open('C:\\'+arq_name+'.pdf','rb'))
        await bot.edit_message_text(chat_id=message.chat.id, message_id=result_message.id, text='<i>Feito!</i>', parse_mode='HTML')

#verifica docx
    elif arq_type == 'docx':
        with open('file.docx', 'wb') as new_file:
            new_file.write(downloaded_file)
        docPdf('file.docx',arq_name)
        await bot.send_document(chat_id = message.chat.id, document=open('C:\\'+arq_name+'.pdf','rb'))
        await bot.edit_message_text(chat_id=message.chat.id, message_id=result_message.id, text='<i>Feito!</i>', parse_mode='HTML')

#verifica ppt
    elif arq_type == 'ppt':
        with open('file.ppt', 'wb') as new_file:
            new_file.write(downloaded_file)
        pptPdf('file.ppt',arq_name)
        await bot.send_document(chat_id = message.chat.id, document=open('C:\\'+arq_name+'.pdf','rb'))
        await bot.edit_message_text(chat_id=message.chat.id, message_id=result_message.id, text='<i>Feito!</i>', parse_mode='HTML')

#verifica pptx
    elif arq_type == 'pptx':
        with open('file.pptx', 'wb') as new_file:
            new_file.write(downloaded_file)
        pptxPdf('file.pptx',arq_name)
        await bot.send_document(chat_id = message.chat.id, document=open('C:\\'+arq_name+'.pdf','rb'))
        await bot.edit_message_text(chat_id=message.chat.id, message_id=result_message.id, text='<i>Feito!</i>', parse_mode='HTML')

#verifica pdf
    elif arq_type == 'pdf':
        await bot.edit_message_text(chat_id=message.chat.id, message_id=result_message.id, text='<i>este arquivo já é PDF!</i>', parse_mode='HTML')
#verifica não reconhecido
    else:
        await bot.edit_message_text(chat_id=message.chat.id, message_id=result_message.id, text='<i>Tipo de arquivo não reconhecido!</i>', parse_mode='HTML')



asyncio.run(bot.polling())
#envia arquivo
#await bot.send_document(chat_id = message.chat.id, document=open('C:\\a.txt','rb'))