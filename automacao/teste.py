import base64
from time import sleep

from anticaptchaofficial import imagecaptcha
from anticaptchaofficial.imagecaptcha import *
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager


class automacao:
    def iniciar(self):
        self.configuracao_navegador()
        self.login()
        self.novo_servico()
        self.configuracao_de_servico()

    def configuracao_navegador(self):
        self.options = Options()

        self.options.add_argument('start-maximized')
        self.options.add_argument('disable-extensions')

        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=self.options
        )

    def tratativa_captcha(self):
        teste = self.driver.find_element(
            By.XPATH, self.captha)  # noqa E501

        teste = teste.screenshot_as_base64
        imagem = base64.b64decode(teste)
        with open('imagem.jpg', 'wb') as img_file:
            img_file.write(imagem)

        solver = imagecaptcha()
        solver.set_verbose(1)
        solver.set_key("1de9be01c262f1c9172f9bf5070c8ea9")

        solver.set_soft_id(0)

        resultado = solver.solve_and_return_solution('imagem.jpg')
        return resultado

    def login(self):
        self.driver.get('https://www.proeis.rj.gov.br/Default.aspx')
        self.driver.find_element(
            By.ID, 'ddlTipoAcesso').send_keys('ID Funcional')
        self.driver.find_element(By.ID, 'txtLogin').send_keys('50790323')
        self.driver.find_element(By.ID, 'txtSenha').send_keys('fac50@D')
        self.captha = '/html/body/main/form/div[3]/div/div[1]/div[2]/div[2]/div[1]/div/div/div'
        resultado = self.tratativa_captcha()
        self.driver.find_element(By.ID, 'TextCaptcha').send_keys(resultado)
        self.driver.find_element(By.ID, 'btnEntrar').click()
        sleep(1)

    def novo_servico(self):
        self.driver.find_element(
            By.XPATH, '/html/body/form/div[5]/div/div/div/div[1]/div[2]/a').click()  # noqa E501
        self.driver.find_element(
            By.XPATH, '/html/body/form/div[5]/div/div/div/input').click()

    def configuracao_de_servico(self):
        dia = 76
        convenio = 'MUNICÍPIO DE DUQUE DE CAXIAS'
        self.driver.find_element(
            By.XPATH, '/html/body/form/div[5]/div[2]/div[1]/div[2]/div/div/select').send_keys(convenio)  # noqa E501
        select = Select(self.driver.find_element(By.XPATH, '/html/body/form/div[5]/div[2]/div[1]/div[3]/div[1]/div/select'))  # noqa E501
        select.select_by_value(str(dia))
        self.driver.find_element(By.ID, 'lnkNewCaptcha').click()
        sleep(1)
        self.captha = '/html/body/form/div[5]/div[2]/div[1]/div[3]/div[3]/div[2]/div/div/div'
        resultado = self.tratativa_captcha()
        self.driver.find_element(
            By.XPATH, '/html/body/form/div[5]/div[2]/div[1]/div[3]/div[3]/div[1]/div/div/input').clear()
        self.driver.find_element(
            By.XPATH, '/html/body/form/div[5]/div[2]/div[1]/div[3]/div[3]/div[1]/div/div/input').send_keys(resultado)  # noqa E501
        sleep(5)
        self.driver.find_element(
            By.XPATH, '/html/body/form/div[5]/div[2]/div[1]/div[4]/div/input').click()  # noqa E501
        sleep(5)
        item = 2
        teste = 0

        try:
            for tabela in range(500):
                tabela = self.driver.find_element(
                    By.XPATH, f'/html/body/form/div[5]/div[2]/div[3]/div[3]/div[2]/div[2]/div/div[2]/div/table/tbody/tr[{item}]/td[1]')  # noqa E501
                horario = self.driver.find_element(
                    By.XPATH, f'/html/body/form/div[5]/div[2]/div[3]/div[3]/div[2]/div[2]/div/div[2]/div/table/tbody/tr[{item}]/td[2]')  # noqa E501

                if tabela.text.strip() == 'JARDIM PRIMAVERA CABINE' and horario.text.strip() == '19:00:00':  # noqa E501
                    teste += 1

                item += 1
        except NoSuchElementException:
            print(item, ' deu isso de linha')
        print(teste)


if __name__ == '__main__':
    start = automacao()
    start.iniciar()
