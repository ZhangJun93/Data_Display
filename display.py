# coding:utf-8
import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog
from MongoOperator import MongoOperator

db = MongoOperator('127.0.0.1', 27017, 'web_news', 'test_collection')


def search_action():
    table_name = collection_name_text.get()

    if table_name == '':
        display_text.insert(tk.INSERT, u"请输入合法的表名!!!")
    else:
        keyWord = key_word_text.get()
        print(type(keyWord))
        if keyWord == '':
            display_text.insert(tk.INSERT, u"请输入至少一个关键字!!!")
            return
        expression = {"content": {"$regex": keyWord}}
        # expression = {"date": "1970-01-01"}
        resultItem = db.find(expression=expression, collection_name=table_name)
        result_count = resultItem.count()
        if result_count == 0:
            display_text.insert(tk.INSERT, u"对不起，没有查询到结果，请重试！！！")
        else:
            content = u'             共找到%d篇相关文章       \n' % result_count
            idx = 1
            for item in resultItem:
                content += str(idx) + u"、 标题："  + item['title'] + u" 内容：" + item['content'][:50] + '\n'
                # content += str(idx) + u"、 标题：" + item['title'] + '\n'
                idx += 1
            clear_display()
            display_text.insert(tk.INSERT, content)
        # print(resultItem.count())

def clear_display():
    display_text.delete(index1="1.0", index2='10000.end')

def cancel_action():
    collection_name_text.delete(first=0, last=len(collection_name_text.get()))
    key_word_text.delete(first=0, last=len(key_word_text.get()))
    clear_display()
    # display_text.delete(index1=0, index2=len(display_text.get()))

root = tk.Tk()
root.title("CloudMinds")
root.geometry("550x550")
#root.resizable(False, False)

collection_name = tk.Label(root, text=u"数据库名: ", font=(10))
collection_name.grid(row=0, sticky=tk.NSEW, padx=50, pady=5, ipadx=10, ipady=0)
#collection_name.pack(side=tk.LEFT, fill=tk.NONE,expand=tk.YES,anchor=tk.CENTER)
# collection_name_text = tk.Entry(root, font=(10))
collection_name_text = ttk.Combobox(root, font=(10))
collection_name_text["values"] =("zsyh_spider", "tzj_spider", "rmw_spider", "jqrzj_spider",  "hsjqr_spider", "zhjqr_spider")
collection_name_text.grid(row=0, column=1, sticky=tk.NSEW, padx=0, pady=40, ipadx=0)
#collection_name_text.pack(side=tk.LEFT, fill=tk.NONE,expand=tk.YES, ipadx=100, ipady=5,anchor=tk.CENTER)


key_word = tk.Label(root, text=u"关键字: ", font=(10))
# key_word.pack(side=tk.LEFT, fill=tk.NONE, expand=tk.YES, anchor=tk.CENTER)
key_word.grid(row=1, sticky=tk.NSEW, padx=50, pady=5, ipadx=5, ipady=5)
# key_word_text = tk.Entry(root, font=(10))
key_word_text = tk.Entry(root, font=(10))
key_word_text.grid(row=1, column=1, sticky=tk.NSEW, padx=0, pady=40, ipadx=0)
# key_word_text.pack(side=tk.LEFT, fill=tk.NONE, expand=tk.YES, ipadx=100, ipady=5, anchor=tk.CENTER)
# collection_name_text =
# text = tkinter.Entry(root)
# btn1 = tkinter.Button(root, text='Input String', command=inputStr)
# btn2 = tkinter.Button(root, text='Input Integer', command=inputInt)
# btn3 = tkinter.Button(root, text='Input Float', command=inputFloat)
# text.pack(side='left')
# btn1.pack(side='left')
# btn2.pack(side='left')
# btn3.pack(side='left')

display_text = tk.Text(root, font=(10), width=40, height=10)
display_text.grid(row=3, columnspan=2, padx=30, pady=5,sticky=tk.NSEW)
search_button = tk.Button(root, text=u'搜索', font=(10), command=search_action)
search_button.grid(row=5, sticky=tk.EW, padx=0, pady=5, ipadx=0)
cancel_button = tk.Button(root, text=u'取消', font=(10), command=cancel_action)
cancel_button.grid(row=5, column=1, sticky=tk.EW, padx=0, pady=5, ipadx=0)
root.mainloop()
