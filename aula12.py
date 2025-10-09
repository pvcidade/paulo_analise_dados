from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import pandas as pd

# --- Configurações ---
url = "https://www.dfimoveis.com.br/"
# O Chrome será fechado no final do script.
driver = webdriver.Chrome()
driver.get(url)
wait = WebDriverWait(driver, 15) # espera padrão de 15 segundos
time.sleep(3) # Pausa inicial

# --- FILTROS DE BUSCA (sem alterações) ---

# --- 1. Abre e Seleciona 'VENDA' ---
botao_negocio = wait.until(EC.element_to_be_clickable((By.ID, "select2-negocios-container")))
botao_negocio.click()
print("Dropdown de tipo de negócio aberto.")
nome_opcao = "VENDA"
xpath_opcao = (f"//li[contains(@class,'select2-results__option') and normalize-space(text())='{nome_opcao}']")
elemento_opcao = wait.until(EC.visibility_of_element_located((By.XPATH, xpath_opcao)))
elemento_opcao.click()
print(f"Opção '{nome_opcao}' selecionada com sucesso!")
time.sleep(1)

# --- 2. Abre e Seleciona 'APARTAMENTO' ---
try:
    botao_tipo_imovel = wait.until(EC.element_to_be_clickable((By.ID, "select2-tipos-container")))
    botao_tipo_imovel.click()
    print("Dropdown de tipo de imóvel aberto.")
except TimeoutException:
    print("Erro: Não foi possível encontrar ou clicar no dropdown de Tipo de Imóvel.")
    driver.quit()
    exit()
nome_opcao = "APARTAMENTO"
xpath_opcao = (f"//li[contains(@class,'select2-results__option') and normalize-space(text())='{nome_opcao}']")
try:
    elemento_opcao = wait.until(EC.visibility_of_element_located((By.XPATH, xpath_opcao)))
    elemento_opcao.click()
    print(f"Opção '{nome_opcao}' selecionada com sucesso!")
except TimeoutException:
    print(f"Erro: A opção '{nome_opcao}' não foi encontrada ou não pôde ser clicada.")
time.sleep(1)

# --- 3. Abre e Seleciona 'DF' ---
try:
    botao_estado = wait.until(EC.element_to_be_clickable((By.ID, "select2-estados-container")))
    botao_estado.click()
    print("Dropdown de estado aberto.")
except TimeoutException:
    print("Erro: Não foi possível encontrar ou clicar no dropdown de Estado.")
nome_opcao_estado = "DF"
xpath_opcao_estado = (f"//li[contains(@class,'select2-results__option') and normalize-space(text())='{nome_opcao_estado}']")
try:
    elemento_opcao_estado = wait.until(EC.visibility_of_element_located((By.XPATH, xpath_opcao_estado)))
    elemento_opcao_estado.click()
    print(f"Opção '{nome_opcao_estado}' selecionada com sucesso!")
except TimeoutException:
    print(f"Erro: A opção '{nome_opcao_estado}' não foi encontrada ou não pôde ser clicada.")
time.sleep(1)

# --- 4. Abre e Seleciona 'BRASILIA / PLANO PILOTO' ---
try:
    botao_cidade = wait.until(EC.element_to_be_clickable((By.ID, "select2-cidades-container")))
    botao_cidade.click()
    print("Dropdown de cidade aberto.")
except TimeoutException:
    print("Erro: Não foi possível encontrar ou clicar no dropdown de Cidade.")
nome_opcao_cidade = "BRASILIA / PLANO PILOTO"
xpath_opcao_cidade = (f"//li[contains(@class,'select2-results__option') and normalize-space(text())='{nome_opcao_cidade}']")
try:
    elemento_opcao_cidade = wait.until(EC.visibility_of_element_located((By.XPATH, xpath_opcao_cidade)))
    elemento_opcao_cidade.click()
    print(f"Opção '{nome_opcao_cidade}' selecionada com sucesso!")
except TimeoutException:
    print(f"Erro: A opção '{nome_opcao_cidade}' não foi encontrada ou não pôde ser clicada.")
time.sleep(1)

# --- 5. Abre e Seleciona 'ASA SUL' ---
try:
    botao_bairro = wait.until(EC.element_to_be_clickable((By.ID, "select2-bairros-container")))
    botao_bairro.click()
    print("Dropdown de bairro aberto.")
except TimeoutException:
    print("Erro: Não foi possível encontrar ou clicar no dropdown de Bairro.")
nome_opcao_bairro = "ASA SUL"
xpath_opcao_bairro = (f"//li[contains(@class,'select2-results__option') and normalize-space(text())='{nome_opcao_bairro}']")
try:
    elemento_opcao_bairro = wait.until(EC.visibility_of_element_located((By.XPATH, xpath_opcao_bairro)))
    elemento_opcao_bairro.click()
    print(f"Opção '{nome_opcao_bairro}' selecionada com sucesso!")
except TimeoutException:
    print(f"Erro: A opção '{nome_opcao_bairro}' não foi encontrada ou não pôde ser clicada.")
time.sleep(1)

# --- 6. Clica no botão PESQUISAR ---
try:
    botao_pesquisar = wait.until(EC.element_to_be_clickable((By.ID, "botaoDeBusca")))
    botao_pesquisar.click()
    print("Botão 'PESQUISAR' clicado com sucesso!")
except TimeoutException:
    print("Erro: Não foi possível encontrar ou clicar no botão 'PESQUISAR'.")
time.sleep(5) # Tempo para a página de resultados carregar

# ------------------------------------
## --- COLETA DE DADOS COM PAGINAÇÃO ---
# ------------------------------------
print("-" * 50)
print("Iniciando coleta e navegação por páginas...")

dados_imoveis = []
pagina_atual = 1
max_paginas = 100 # Limite de segurança para evitar loops infinitos

def coletar_imoveis_da_pagina():
    """Função para coletar todos os imóveis visíveis na página atual de forma robusta."""
    # Espera até que os cards de imóvel estejam carregados
    try:
        # Espera pela presença de pelo menos um card de imóvel
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "imovel-card")))
        # Rola um pouco a página para garantir que os elementos estejam visíveis
        driver.execute_script("window.scrollTo(0, 500);")
        time.sleep(2)
        cartoes_imoveis = driver.find_elements(By.CLASS_NAME, "imovel-card")
    except TimeoutException:
        print(f"Página {pagina_atual}: Não foi possível carregar os cards de imóvel.")
        return []

    imoveis_coletados = []
    
    for i, card in enumerate(cartoes_imoveis):
        try:
            url = card.get_attribute("href")
            
            # Endereço
            endereco_elems = card.find_elements(By.TAG_NAME, "h2")
            endereco = endereco_elems[0].text.strip() if endereco_elems else "N/A"

            # Título/Tipo
            titulo_elems = card.find_elements(By.CSS_SELECTOR, "h3.bold")
            titulo = titulo_elems[0].text.strip() if titulo_elems else "N/A"

            # Características Adicionais
            caracteristicas_elems = card.find_elements(By.CSS_SELECTOR, "h3.text-uppercase")
            caracteristicas = caracteristicas_elems[0].text.strip() if caracteristicas_elems else "N/A"

            # Preço
            preco_elems = card.find_elements(By.CSS_SELECTOR, ".imovel-price .body-large.bold")
            preco = "R$ " + preco_elems[0].text.strip() if preco_elems else "N/A"

            # Metragem e Quartos
            features = card.find_elements(By.CSS_SELECTOR, ".imovel-feature div")
            metragem = "N/A"
            quartos = "N/A"
            for feature in features:
                texto = feature.text.strip()
                if "m²" in texto:
                    metragem = texto
                elif "Quartos" in texto or "Quarto" in texto:
                    quartos = texto
            
            # Creci
            creci_elems = card.find_elements(By.CSS_SELECTOR, ".imovel-anunciante p.label-medium.ellipse-text")
            creci = creci_elems[0].text.strip() if creci_elems else "N/A"

            imoveis_coletados.append({
                "URL": url,
                "Endereço": endereco,
                "Tipo/Área": titulo,
                "Características": caracteristicas,
                "Preço": preco,
                "Metragem": metragem,
                "Quartos": quartos,
                "Creci": creci
            })

        except Exception as e:
            # Em caso de erro em um card, continua para o próximo
            continue
    
    print(f"Página {pagina_atual}: {len(imoveis_coletados)} imóveis coletados.")
    return imoveis_coletados


# --- Loop Principal de Paginação (Corrigido para evitar repetição da última página) ---
while pagina_atual <= max_paginas:
    print(f"\nColetando dados da Página {pagina_atual}...")
    
    # Coleta os dados da página atual
    novos_imoveis = coletar_imoveis_da_pagina()
    
    # Condição de PARADA 1: A página retornou 0 imóveis.
    if not novos_imoveis and pagina_atual > 1:
        print("Página atual não retornou imóveis. Fim da paginação.")
        break
    
    # Se a página 1 não tem imóveis, paramos
    if not novos_imoveis and pagina_atual == 1:
        print("Nenhum imóvel encontrado na primeira página. Fim da coleta.")
        break
        
    dados_imoveis.extend(novos_imoveis)
    
    # Salva o URL antes de tentar avançar
    url_antes_do_clique = driver.current_url
    
    # Tenta encontrar o botão para a próxima página
    try:
        # XPath CORRIGIDO: Procurando a tag <span> com a classe 'next' e o texto 'Próximo'
        botao_proximo_xpath_corrigido = "//span[contains(@class, 'next') and contains(text(), 'Próximo')]"
        
        # Usamos uma espera menor (5 segundos) para falhar rápido se o botão sumir
        wait_curta = WebDriverWait(driver, 5) 
        botao_proximo = wait_curta.until(EC.visibility_of_element_located((By.XPATH, botao_proximo_xpath_corrigido)))
        
        # SOLUÇÃO PARA ElementClickInterceptedException: Força o clique via JavaScript
        driver.execute_script("arguments[0].click();", botao_proximo)
        
        # Espera um pouco para o site processar e a página carregar
        time.sleep(3) 

        # NOVO MECANISMO DE PARADA: Verifica se o URL mudou
        url_depois_do_clique = driver.current_url
        if url_antes_do_clique == url_depois_do_clique:
            print("O URL não mudou após o clique em 'Próximo'. A página deve ser a última. Fim da paginação.")
            break
            
        pagina_atual += 1
        print("Avançando para a próxima página...")
        
    except (TimeoutException, NoSuchElementException):
        # Condição de PARADA 2: O botão "Próximo" não existe mais (fim da paginação).
        print("Botão 'Próximo' não encontrado. Fim da paginação.")
        break
    
    # Condição de PARADA 3: Limite máximo de páginas
    if pagina_atual > max_paginas:
        print(f"Limite máximo de {max_paginas} páginas atingido.")
        break


# ------------------------------------
## --- FINALIZAÇÃO E SALVAMENTO ---
# ------------------------------------
print("-" * 50)
print(f"Coleta de dados finalizada. Total de imóveis coletados: {len(dados_imoveis)}")

# 1. Cria o DataFrame
df = pd.DataFrame(dados_imoveis)

# 2. Exibe informações (opcional)
print("\nPrimeiras 5 linhas do DataFrame:")
print(df.head())
print(f"\nDimensões do DataFrame: {df.shape}")

# 3. Salva o DataFrame em um arquivo CSV
nome_arquivo = "imoveis_dfimoveis_asa_sul.csv"
df.to_csv(nome_arquivo, index=False, encoding='utf-8')
print(f"\nDados salvos com sucesso em: {nome_arquivo}")

# 4. Fecha o navegador
driver.quit()