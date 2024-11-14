from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
#import cloudscraper
#import requests
import time
import os
import re

# Configuração do WebDriver
options = webdriver.ChromeOptions()
#options.add_argument("--headless")  # Executa em modo invisivel para não abrir janela do navegador
driver = webdriver.Chrome(options=options)

# URL inicial
url = ''
driver.get('')
time.sleep(5)
driver.get(url)
time.sleep(60)  # Aguarda a página carregar completamente

# Cria a pasta principal para salvar as imagens, se não existir
main_folder = "imagens_baixadas"
os.makedirs(main_folder, exist_ok=True)

# Obtém a lista de âncoras e os nomes na grid
anchors = driver.find_elements(By.CSS_SELECTOR, 'div.grid.grid-cols-1.sm\\:grid-cols-2.lg\\:grid-cols-3.gap-4 a')
anchor_data = []
for anchor in anchors:
    link_url = anchor.get_attribute('href')
    title = anchor.text.strip() if anchor.text.strip() else "site_sem_nome"
    title = re.sub(r'[\\/*?:"<>|]', "", title)
    anchor_data.append((title, link_url))

# Itera sobre cada URL e baixa as imagens
for title, link_url in anchor_data:
    folder_path = os.path.join(main_folder, title)
    os.makedirs(folder_path, exist_ok=True)  # Cria a pasta específica para o site âncora

    print(f"Acessando site âncora: {title} - URL: {link_url}")
    driver.get(link_url)
    time.sleep(2)  # Aguarda a página de destino carregar

    # Rolagem da página para carregar imagens dinâmicas
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    image_divs = soup.find_all('div', class_='flex flex-col')
    print(f"Encontradas {len(image_divs)} divs de imagem para o site {title}")

    for idx, div in enumerate(image_divs):
        img_tag = div.find('img')
        if img_tag:
            img_url = img_tag.get('src')
            if img_url:
                try:
                    img_data = requests.get(img_url).content
                    img_path = os.path.join(folder_path, f'imagem_{idx}.jpg')
                    with open(img_path, 'wb') as handler:
                        handler.write(img_data)
                    print(f"Imagem salva em: {img_path}")
                except Exception as e:
                    print(f"Erro ao baixar imagem {img_url}: {e}")

print("Download de imagens concluído!")
driver.quit()