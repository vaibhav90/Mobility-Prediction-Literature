from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import platform

def delayFechar(tempo):
    for ind in range(tempo, 0, -1):
        print("Browser fechando em " + str(ind) + " segundos")
        time.sleep(1)


print("Enter string")
palavras_chave = str(input())

print("Number of pages?")
paginas = int(input())

inicio_link = 'https://preview.academic.microsoft.com/home'
fim_link = '&sort=relevance&pdf=true'
fim_link_outras_comeco = '&sort=relevance&page='
fim_link_outras_fim = '&pdf=true'
meio_link = ''
palavras_separadas = palavras_chave.split()

for palavra in palavras_separadas:
    meio_link += palavra
    if palavra is not palavras_separadas[-1]:
        meio_link += '%20'

url1 = inicio_link + meio_link + fim_link
lista_de_urls = [url1]

for i in range(2, paginas+1):
    temp = inicio_link + meio_link + fim_link_outras_comeco + str(i) + fim_link_outras_fim
    lista_de_urls.append(temp)

options = webdriver.ChromeOptions()

diretorio_atual = os.getcwd()

plataforma = platform.system()
if plataforma == 'Darwin':
    diretorio_chromedriver = diretorio_atual + '/ChromeDriver/ChromeDriverMac'
elif plataforma == 'Windows':
    diretorio_chromedriver = diretorio_atual + '/ChromeDriver/ChromeDriverWin.exe'
else:
    diretorio_chromedriver = diretorio_atual + '/ChromeDriver/ChromeDriverLin'

diretorio_pdf = diretorio_atual + '/PDFs'

if os.path.exists(diretorio_pdf):
    pass
else:
    os.mkdir('PDFs')

options.add_experimental_option("prefs", {
  "download.default_directory": diretorio_pdf,
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  "plugins.always_open_pdf_externally": True,
  "safebrowsing.enabled": True
})
driver = webdriver.Safari()

nomes_artigos = []

for url in lista_de_urls:
    driver.get(url)
    try:
        element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, 'PDF')))
    finally:
        lista_de_artigos = driver.find_elements_by_class_name('search-result-title')
        print(len(lista_de_artigos))
        for artigo in lista_de_artigos:
            link = artigo.get_attribute('aria-label')
            print("Link: " + str(link))

delayFechar(3)
driver.quit()