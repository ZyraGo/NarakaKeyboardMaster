from direct.showbase.ShowBase import ShowBase

class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # 创建一个全屏的红色背景
        self.setBackgroundColor(255, 255, 255, 1)

app = MyApp()
app.run()
