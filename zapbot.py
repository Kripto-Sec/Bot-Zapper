from selenium import webdriver
import time 

class WhatsappBot:
    def __init__(self):
        self.mensagem = "Teste Teste testando o bot"
        self.grupos = ["🌎🇬🇷GREGO GEEK'S🇬🇷🌐","Mãe"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(
             executable_path=r'./chromedriver.exe')

    def EnviarMensagen(self):
        #<span dir="auto" title="Abiguinha de 30cm❤💙" class="_1wjpf _3NFp9 _3FXB1">Abiguinha de 30cm</span>
        #<footer tabindex="-1" class="_2tW_W">
        #<span data-icon="send" class="">
        self.driver.get('https://web.whatsapp.com')
        time.sleep(35)
        for grupo in self.grupos:
            grupo = self.driver.find_element_by_xpath(f"//span[@title='{grupo}']")
            time.sleep(3)
            grupo.click()
            chat_box = self.driver.find_element_by_class_name('_2tW_W')
            time.sleep(3)
            chat_box.click()
            chat_box.send_keys(self.mensagem)
            botao_enviar = self.driver.find_element_by_xpath(
                "//span[@data-icon='send']")
                
            time.sleep(3)
            botao_enviar.click()
            time.sleep(5)
bot = WhatsappBot()
bot.EnviarMensagen()






        #<span dir="auto" title"🌎🇬🇷GREGO GEEK'S🇬🇷🌐" class="_1wjpf _3NFp9 _3FXB1"></span>
 

