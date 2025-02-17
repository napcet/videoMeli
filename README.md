# Downloader de Vídeos do Mercado Livre `.m3u8` com `ffmpeg`

## Descrição

Este é um **programa Python** para **baixar vídeos** a partir de **links de índice `.m3u8`** usando o software de linha de comando `ffmpeg`. Ele permite que você baixe vídeos de anúncios (ou qualquer outro vídeo disponível via link `.m3u8`) e os salve com um nome de arquivo customizado, baseado no código do anúncio fornecido.

## Funcionalidades

- **Verificação do `ffmpeg`**: O programa verifica se o `ffmpeg` está instalado corretamente no sistema antes de tentar baixar o vídeo.
- **Entrada do link `.m3u8`**: O usuário fornece um link de índice `.m3u8`, que é a referência para o vídeo a ser baixado.
- **Código do anúncio**: O programa solicita ao usuário o código do anúncio, usado para gerar o nome do arquivo de saída no formato `MLB<codigo>.mp4`.
- **Baixando o vídeo**: O `ffmpeg` é utilizado para baixar o vídeo diretamente para o formato `.mp4` e salvá-lo com o nome gerado.

## Requisitos

Para rodar este programa, você precisa ter:

- **Python 3.x**: A versão mais recente do Python deve estar instalada em sua máquina.
- **ffmpeg**: O `ffmpeg` é uma ferramenta de linha de comando que permite a conversão e manipulação de arquivos de mídia. O programa verifica automaticamente se o `ffmpeg` está disponível no seu sistema.

### Como instalar o `ffmpeg`

- **No Ubuntu/Debian**:

  ```bash
  sudo apt update
  sudo apt install ffmpeg
  ```

- **No macOS (via Homebrew)**:

  ```bash
  brew install ffmpeg
  ```

- **No Windows**:
  1. Baixe o `ffmpeg` do [site oficial](https://ffmpeg.org/download.html).
  2. Extraia o arquivo e adicione a pasta `bin` ao **PATH** do sistema.

## Como Obter o Link do Índice `.m3u8`

Para baixar o vídeo, você precisa obter o **link do índice `.m3u8`**. O índice `.m3u8` é o arquivo que contém informações sobre o fluxo de vídeo, como a lista de segmentos e o formato de cada um.

### Passo a Passo para Obter o Link do Índice `.m3u8`:

1. **Abra a página de vídeo no seu navegador**:

   - Vá até a página onde o vídeo está hospedado (por exemplo, em um anúncio ou página de mídia).

2. **Abra as Ferramentas de Desenvolvedor**:

   - No **Google Chrome** ou **Microsoft Edge**, pressione `F12` ou clique com o botão direito do mouse na página e selecione "Inspecionar".
   - No **Firefox**, pressione `F12` ou clique com o botão direito e selecione "Inspecionar Elemento".

3. **Vá para a aba "Network" (Rede)**:

   - Na interface das ferramentas de desenvolvedor, selecione a aba **"Network"** (Rede). Esta aba mostra todas as requisições feitas pela página, incluindo as de arquivos de mídia.

4. **Filtre por `.mp4`**:

   - No campo de filtro de requisições, digite `mp4`. Isso irá filtrar e mostrar apenas as requisições que envolvem arquivos `.mp4` ou arquivos relacionados ao vídeo.

5. **Recarregue a página e inicie o vídeo**:

   - Após aplicar o filtro, recarregue a página ou clique para iniciar o vídeo. Isso fará com que o navegador faça as requisições para o arquivo de vídeo.

6. **Encontre a requisição `.m3u8`**:

   - No painel "Network", procure por uma requisição que contenha a URL que termina com `.m3u8`. Esse será o **link do índice do vídeo**.
   - Normalmente, ele está listado como uma requisição de "Media" ou "XHR" e pode estar em uma lista de fluxos ou segmentos de vídeo.

7. **Copie o Link do Índice**:
   - Clique na requisição `.m3u8` e, na parte de "Headers" ou "Response", copie o URL completo. Este será o link que você irá fornecer ao programa.

### Exemplo de Link do Índice `.m3u8`

O link do índice `.m3u8` terá um formato semelhante a:

https://example.com/path/to/video/index.m3u8

Esse link é o que você deve fornecer quando o programa solicitar o **link do índice `.m3u8`**.

## Como usar o programa

1. Clone este repositório para o seu computador:

   ```bash
   git clone https://github.com/napcet/videoMeli.git
   cd videoMeli
   ```

2. Execute o script Python:

   ```bash
   python3 main.py
   ```

3. O programa solicitará o link do índice `.m3u8` e o código do anúncio.
   - Exemplo de código do anúncio: `1111111111`
   - O vídeo será baixado e salvo com o nome de arquivo `MLB<codigo>.mp4`.

## Exemplo de Execução

Quando você executar o programa, o terminal pedirá os seguintes dados:

```
Digite o link do índice .m3u8: https://example.com/video.m3u8
Digite o código do anúncio: 1111111111
Baixando o vídeo de: https://example.com/video.m3u8
Vídeo salvo em: MLB1111111111.mp4
```

## Benefícios

- **Simplicidade**: A interface simples do programa permite que qualquer pessoa baixe vídeos de forma rápida e eficiente.
- **Automação**: O processo de verificação do `ffmpeg` e nomeação automática do arquivo facilita o uso.
- **Acessibilidade**: O programa é compatível com qualquer sistema operacional que suporte o Python e o `ffmpeg`.

## Tecnologias Utilizadas

- **Python**: A linguagem de programação utilizada para desenvolver o script.
- **ffmpeg**: Ferramenta de linha de comando para processamento de vídeos e áudios.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
