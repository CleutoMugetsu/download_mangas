# Download Mangá

Este projeto é um script de automação desenvolvido para baixar imagens de sites de mangá, utilizado para testes de conhecimento. O script faz uso do Selenium WebDriver e BeautifulSoup para acessar uma URL principal, coletar links de âncoras dentro de uma grid, navegar até cada uma dessas URLs e baixar as imagens disponíveis.

## Pré-requisitos

- **Python 3.7+**
- **Selenium**
- **BeautifulSoup4**
- **Chrome WebDriver** (ou outro navegador suportado pelo Selenium)
- **Requests**

Instale as dependências necessárias com o seguinte comando:

```bash
pip install selenium beautifulsoup4 requests
```

Baixe o **Chrome WebDriver** adequado para a versão do seu navegador e coloque-o em um diretório acessível pelo sistema ou no mesmo diretório do script.

## Configuração

1. **Defina a URL principal**: Atualize a variável `url` com a URL do site de mangá que deseja acessar para iniciar a busca.
2. **Configuração do WebDriver**: Por padrão, o script abrirá o navegador de forma visível. Para executá-lo em modo invisível (sem abrir a janela do navegador), descomente a linha `options.add_argument("--headless")`.

## Como usar

1. Execute o script com o seguinte comando:

   ```bash
   python teste.py
   ```

2. O script realizará as seguintes ações:
   - Acessará a URL principal.
   - Extrairá os links de todas as âncoras encontradas na grid de links.
   - Criará uma pasta chamada `imagens_baixadas` no diretório atual, com subpastas correspondentes ao título de cada âncora.
   - Acessará cada URL extraída, rolando a página para carregar imagens dinâmicas e baixando as imagens encontradas.

## Estrutura das Pastas

O script cria a seguinte estrutura de diretórios:

- `imagens_baixadas/`: Diretório principal onde as imagens serão salvas.
  - Cada subdiretório será nomeado conforme o título de cada âncora (se o título estiver vazio, o nome será `site_sem_nome`).

## Personalização

- **Tempo de carregamento da página**: O tempo de espera entre as ações é controlado pelas instruções `time.sleep()`. Ajuste esses valores conforme necessário para garantir que as páginas e imagens carreguem corretamente.
- **Classe do contêiner de imagens**: A classe `flex flex-col` foi usada no script para encontrar as imagens. Se o site que você está acessando tiver uma estrutura diferente, altere a linha `image_divs = soup.find_all('div', class_='flex flex-col')` para refletir a classe apropriada.

## Erros Comuns

- **Caixa de diálogo de confirmação**: Se a página exigir a confirmação de uma caixa de diálogo antes de permitir o acesso, adicione a URL inicial no primeiro `driver.get('')`.
- **Problemas de conexão**: Certifique-se de que a URL está acessível e que o WebDriver é compatível com a versão do navegador instalado.
- **Imagens dinâmicas**: Se as imagens forem carregadas dinamicamente via JavaScript, aumente o tempo de espera (`time.sleep()`) ou ajuste a lógica de rolagem da página para garantir que todas as imagens sejam carregadas.

## Finalização

Após o término do processo, o script salvará todas as imagens no diretório correspondente e encerrará o WebDriver. O script exibirá mensagens indicando o progresso do download e o sucesso ou falha em salvar as imagens.