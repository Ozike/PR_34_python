from kivy.config import Config
Config.set('graphics', 'resizable', False)

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.core.window import Window


class CalculatorApp(App):
    
    def add_number(self, instance):
        if self.formula == "0":
            self.formula = ""
        
        self.formula +=str(instance.text)
        self.update_label()

    def add_operation(self, instance):
        if str(instance.text).lower() == "x":
            self.formula += "*"
        elif str(instance.text) == "%":
            self.formula += "/100*"
        else:
            self.formula += str(instance.text)
        self.update_label()

    def update_label(self):
        self.lbl.text = self.formula

    def calc_result(self, instance):
        if instance.text:
            try:
                self.lbl.text = str(eval(self.lbl.text))
            except:
                self.lbl.text = "Неправильные рассчёты"
        self.formula = "0"
    
    def clear(self, instance):
        if str(instance.text) != "":
            self.formula = ""
        self.update_label()

    def back(self, instance):
        if str(instance.text) == "DEL":
            self.formula = self.formula[0:len(self.formula) -1]
        self.update_label()

    def build(self):
        self.formula = "0"
        Window.size = (200,300)

        bl = BoxLayout(orientation = 'vertical', padding = 10)
        gl = GridLayout(cols = 4, spacing = 2, size_hint = (1, .6))
        
        self.lbl = Label(text = "0", 
        font_size = 25,
        size_hint = (1, .4),
        text_size = (200 - 20, 300 * .4 - 20),
        halign = "right",
        valign = "center")
        bl.add_widget(self.lbl) 

        gl.add_widget(Button(text = "C", on_press = self.clear))
        gl.add_widget(Button(text = "%", on_press = self.add_operation))
        gl.add_widget(Button(text = "DEL", on_press = self.back))
        gl.add_widget(Button(text = "/", on_press = self.add_operation))
        
        gl.add_widget(Button(text = "7", on_press = self.add_number))
        gl.add_widget(Button(text = "8", on_press = self.add_number))
        gl.add_widget(Button(text = "9", on_press = self.add_number))
        gl.add_widget(Button(text = "X", on_press = self.add_operation))

        gl.add_widget(Button(text = "4", on_press = self.add_number))
        gl.add_widget(Button(text = "5", on_press = self.add_number))
        gl.add_widget(Button(text = "6", on_press = self.add_number))
        gl.add_widget(Button(text = "-", on_press = self.add_operation))
        
        gl.add_widget(Button(text = "1", on_press = self.add_number))
        gl.add_widget(Button(text = "2", on_press = self.add_number))
        gl.add_widget(Button(text = "3", on_press = self.add_number))
        gl.add_widget(Button(text = "+", on_press = self.add_operation))

        gl.add_widget(Button(text = "00", on_press = self.add_number))
        gl.add_widget(Button(text = "0", on_press = self.add_number))
        gl.add_widget(Button(text = ".", on_press = self.add_number))
        gl.add_widget(Button(text = "=", on_press = self.calc_result))

        bl.add_widget(gl)
        return bl


if __name__ == "__main__":
    CalculatorApp().run()