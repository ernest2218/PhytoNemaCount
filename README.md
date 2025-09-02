Claro, aqui está o texto organizado:

### **Projeto 1 – Contagem de nematóides**

**PhytoNemaCount: Contagem Descomplicada de Nematoides com IA e Visão Computacional**

**Resumo**

O cultivo do quiabeiro, especialmente no semiárido nordestino, é de grande importância socioeconômica, sendo fonte de renda e segurança alimentar para comunidades assentadas e quilombolas (IBGE, 2023). No entanto, sua produtividade é severamente afetada pelo nematoide das galhas (*Meloidogyne incognita*), parasita que compromete o desenvolvimento das plantas ao atacar suas raízes (MOENS et al., 2009). A contagem tradicional de ovos desse patógeno, feita manualmente sob microscópio, é lenta, subjetiva e depende de mão de obra especializada (ISAIAS, 2021), o que limita o diagnóstico precoce e o manejo eficaz da infestação. Diante desse cenário, este projeto propõe o desenvolvimento e a validação de um sistema automatizado para contagem de ovos de nematoides utilizando Redes Neurais Convolucionais (CNNs) e técnicas de visão computacional. A metodologia envolve a padronização da extração e preparação de amostras, criação de um banco de imagens microscópicas de alta resolução anotadas por especialistas, treinamento de modelos de CNNs e construção de uma interface acessível via web. Espera-se, com isso, proporcionar maior agilidade, precisão e reprodutibilidade na detecção da praga, contribuindo para práticas agrícolas mais sustentáveis e eficientes. A adoção dessa tecnologia pode representar um avanço significativo para o monitoramento fitossanitário de culturas sensíveis, democratizando o acesso ao diagnóstico e fortalecendo a agricultura familiar no contexto do semiárido brasileiro.

**Palavras-chave:** Visão computacional; Inteligência artificial; Nematoides; Quiabeiro; CNN; Agricultura de precisão; Diagnóstico fitossanitário.

---

### **Introdução**

O quiabo (*Abelmoschus esculentus*) é um vegetal utilizado em pratos icônicos da culinária brasileira, como caruru, ensopados e moquecas, sendo de extrema importância socioeconômica para o Nordeste brasileiro. Seu cultivo reúne famílias e impulsiona economias locais, provendo segurança alimentar e renda a grupos assentados e quilombolas (IBGE, 2023). No entanto, sua sustentabilidade está sob constante ameaça do nematoide das galhas, *Meloidogyne incognita* (MOENS et al., 2009). Esse parasita ataca as raízes, formando galhas que comprometem a absorção de nutrientes, levando a sintomas como nanismo, murcha e clorose (FILGUEIRA et al., 2020). O resultado são perdas significativas na produtividade e qualidade dos frutos, impactando diretamente a renda dos pequenos produtores.

Apesar da gravidade do problema, o manejo eficaz de *M. incognita* é limitado pela dificuldade de contagem precisa dos ovos. Os nematoides são microscópicos e vivem no subsolo, dificultando a detecção precoce. A contagem manual em microscópio é um processo laborioso, lento e suscetível a erros humanos, como subjetividade e fadiga do operador (ISAIAS, 2021). Além disso, a falta de padronização metodológica gera inconsistências nos diagnósticos (BARBEDO, 2018).

Essa lentidão no diagnóstico é crítica, pois os nematoides se multiplicam rapidamente, agravando a infestação antes da implementação de medidas de controle. O manejo é ainda mais desafiador devido à escassez de cultivares de quiabo resistentes e às restrições ao uso de agroquímicos (FILGUEIRA et al., 2020). Métodos alternativos, como rotação de culturas e controle biológico, exigem conhecimento técnico muitas vezes indisponível para agricultores do semiárido, reforçando a necessidade de soluções acessíveis e automatizadas.

---

### **Justificativa**

Diante dessas barreiras, a Inteligência Artificial (IA) surge como uma solução transformadora para superar as limitações humanas no processamento de grandes conjuntos de dados. A aplicação de métodos baseados em IA, como Redes Neurais Convolucionais (CNNs), pode automatizar e acelerar drasticamente a contagem de nematoides, processando imagens digitais em tempo real (BARBEDO, 2018). Essa abordagem não só garante um diagnóstico mais rápido e preciso, mas também oferece maior consistência nos resultados, reduzindo a variabilidade inerente aos métodos manuais (ISAIAS, 2021).

A IA se apresenta como a ferramenta ideal para otimizar a avaliação de infestações por nematoides, um passo crucial para reduzir as perdas econômicas e fortalecer a resiliência da cultura do quiabo no semiárido brasileiro. Para o quiabeiro, cultivado frequentemente por famílias em condições desafiadoras e com acesso limitado a diagnósticos laboratoriais, a IA oferece um monitoramento ágil e dados precisos (FILGUEIRA et al., 2020). Essa agilidade é vital, dada a alta suscetibilidade do quiabeiro a *Meloidogyne incognita* e seu ciclo de vida curto, permitindo uma resposta rápida na prevenção, disseminação e perdas na lavoura.

Além disso, a IA minimiza a subjetividade e a fadiga humana na contagem, um problema crônico nos métodos tradicionais que afeta diretamente a confiabilidade dos resultados (ISAIAS, 2021). Ao automatizar essa tarefa, a metodologia de IA libera tempo e recursos de especialistas para outras atividades de pesquisa e extensão. Esse avanço não só protege a produtividade do quiabo, mas também capacita os produtores a adotarem estratégias de manejo mais eficazes e sustentáveis, como a rotação de culturas baseada em dados obtidos em tempo real, o que é fundamental para a viabilidade econômica e a segurança alimentar das comunidades da região.

---

### **Objetivos**

**Objetivos gerais**

Desenvolver e validar uma metodologia baseada em Redes Neurais Convolucionais (CNNs) para a contagem automatizada de ovos de nematóides em amostras de quiabeiro, visando otimizar o diagnóstico e acelerar o manejo dessas pragas.

**Objetivos específicos**

* Padronizar e otimizar o processo de extração e preparação de amostras de ovos de nematóides de raízes de quiabeiro, visando obter suspensões homogêneas e com mínima interferência de detritos, ideais para a captura de imagens em microscopia;
* Desenvolver um protocolo para a captura de imagens digitais de alta resolução de ovos de nematóides sob microscopia, garantindo consistência na iluminação, foco e densidade de ovos, em cada campo de visão da lâmina, para a construção de um banco de dados de treinamento de alta qualidade;
* Criar dataset de imagens de ovos de nematóides validada por especialistas, utilizando técnicas de segmentação para delimitar precisamente cada ovo para o treinamento e avaliação dos modelos de CNNs;
* Validar e avaliar o desempenho do modelo de CNNs comparando as contagens automatizadas com as contagens manuais, para determinar a acurácia e a confiabilidade da metodologia;
* Desenvolver uma interface de usuário intuitiva para a metodologia, que permita o carregamento de imagens microscópicas e a visualização dos resultados da contagem de ovos de forma clara e acessível aos usuários.

---

### **Metodologia**

Uma abordagem metodológica dividida em 5 etapas será adotada visando automatizar a contagem de ovos de nematóides:

**1ª Etapa - Preparação de Amostras de Ovos**

Esta etapa visa garantir a consistência e a qualidade das amostras iniciais. Implementar-se-á um protocolo rigoroso para a coleta de raízes de quiabeiro, incluindo a definição do número de plantas e o tipo de solo, seguindo parâmetros estabelecidos para culturas infectadas por *Meloidogyne spp*. (MOENS et al., 2009).

Em seguida, a extração dos ovos será otimizada usando água sanitária comercial (hipoclorito de sódio a 1%) para desagregar os ovos, método amplamente validado para nematoides de galhas (LAMBERT et al.,2023), seguida de peneiramento e centrifugação para purificação. Finalmente, as suspensões serão padronizadas em diluição e volume para a captura homogênea de imagens em microscopia, conforme protocolos adaptados para visão computacional (ISAIAS, 2021).

Este processo garante amostras consistentes e de alta qualidade para as etapas subsequentes de aquisição de imagens e análise computacional, minimizando interferências por detritos ou aglomerações (FILGUEIRA et al., 2020).

**2ª Etapa - Protocolo de Captura de Imagens Digitais**

Para garantir que todas as imagens sejam de alta qualidade e consistentes, primeiramente, o microscópio e a câmera serão configurados de forma padronizada (ISAIAS, 2021). Isso significa que a ampliação (magnificação) e o tipo de microscópio serão sempre os mesmos, e a câmera será calibrada com precisão para garantir medidas corretas nas fotos. A iluminação será cuidadosamente ajustada para que seja uniforme e ofereça o melhor contraste, o que é crucial para que os ovos sejam bem visíveis (ISAIAS, 2021). Além disso, o foco dos ovos será padronizado para que todas as imagens sejam nítidas, e a quantidade de ovos em cada área fotografada (densidade por campo de visão) será controlada para evitar que fiquem muito juntos ou muito espalhados (ISAIAS, 2021). Por fim, será definido quantos campos de visão serão capturados por lâmina para garantir que a amostra seja bem representada, e a possibilidade de automatizar essa captura será considerada para maior eficiência.

**3ª Etapa - Criação de um Dataset**

Para a criação de um Dataset de imagens dos ovos de nematóides, validados por especialistas, o processo iniciará com a aquisição de um grande volume de imagens digitais de ovos, utilizando o protocolo de captura previamente estabelecido (ISAIAS, 2021). Em seguida, os especialistas em nematologia serão responsáveis pela anotação e segmentação precisas de cada ovo individualmente nas imagens, o que envolve a delimitação exata de cada ovo (por exemplo, criando máscaras ou caixas delimitadoras). Será implementado um processo de validação cruzada, onde múltiplos especialistas revisarão e, se necessário, corrigirão as anotações feitas, garantindo a consistência e a alta qualidade do dataset (FORTUNATO et al., 2025). Por fim, a organização deste dataset será utilizado para o treinamento e a avaliação dos modelos de CNNs.

**4ª Etapa - Avaliação de desempenho**

Após o treinamento do modelo de Rede Neural Convolucional (CNN), será realizada uma avaliação sistemática de seu desempenho com base em métricas quantitativas amplamente validadas na literatura (BARBEDO, 2018; ISAIAS, 2021). O conjunto de dados será dividido em subconjuntos de treinamento, validação e teste, seguindo proporções estabelecidas em estudos anteriores (FORTUNATO et al., 2025), garantindo que as imagens representem a variabilidade natural de tamanho, iluminação e densidade de ovos (MOENS et al., 2009). Essa abordagem visa assegurar que o modelo seja testado em condições realistas, evitando superestimativas de desempenho.

Para quantificar a precisão do modelo, serão utilizadas métricas consolidadas, como o Erro Médio Absoluto (MAE) e o Erro Quadrático Médio (RMSE), que medem a discrepância entre as contagens automatizadas e as manuais realizadas por especialistas (ISAIAS, 2021). Além disso, o Coeficiente de Determinação (R²) será empregado para avaliar a proporção da variabilidade nos dados explicada pelo modelo (BARBEDO, 2018). Essas métricas permitirão uma análise robusta da capacidade do modelo em generalizar para novas amostras, identificando possíveis tendências de sub ou superestimação.

Complementando as análises quantitativas, serão gerados gráficos de dispersão e de Bland-Altman, que auxiliarão na visualização da concordância entre as contagens preditas e as reais (ISAIAS, 2021). Os gráficos de dispersão destacarão a correlação entre os valores, enquanto os gráficos de Bland-Altman revelarão vieses sistemáticos, como a tendência do modelo em errar consistentemente para mais ou para menos em determinadas condições (FILGUEIRA et al., 2020). Essas análises gráficas são essenciais para identificar padrões de erro não capturados pelas métricas numéricas.

Caso o modelo apresente limitações, como baixa acurácia em imagens com iluminação irregular ou ovos de tamanhos atípicos, serão implementadas estratégias de aprimoramento. Entre elas, destacam-se o pré-processamento rigoroso das imagens, com aplicação de filtros de contraste e padronização de tamanhos (FILGUEIRA et al., 2020), e a ampliação do dataset para incluir uma maior diversidade de cenários (FORTUNATO et al., 2025). Essas medidas visam aumentar a robustez do modelo, garantindo que ele seja aplicável em condições reais de campo.

Por fim, os resultados da avaliação serão documentados e comparados com os obtidos em métodos manuais, destacando as vantagens da abordagem automatizada em termos de velocidade, precisão e reprodutibilidade (ISAIAS, 2021). Essa etapa é crucial para validar a eficácia do modelo e justificar sua adoção em substituição ou complementação aos métodos tradicionais.

**5ª Etapa - Desenvolvimento de Interface com usuário**

Com o modelo treinado e validado, será desenvolvida uma interface web interativa utilizando a biblioteca Streamlit (STREAMLIT, 2025), uma das ferramentas amplamente reconhecidas por sua eficiência na criação de aplicações acessíveis para projetos de ciência de dados e aprendizado de máquina. A interface será projetada para atender usuários não especializados, como agricultores e técnicos agrícolas, garantindo uma experiência intuitiva e funcional (FILGUEIRA et al., 2020).

A aplicação permitirá que o usuário carregue imagens microscópicas diretamente de seu dispositivo, iniciando a análise automatizada com um simples clique. Durante o processamento, o sistema exibirá em tempo real todas as etapas envolvidas, incluindo a imagem original, as fases de redimensionamento e normalização, e o resultado final da predição (BARBEDO, 2018). Essa transparência no processo visa aumentar a confiança do usuário, permitindo que ele acompanhe cada estágio da análise e compreenda como a contagem foi gerada (FORTUNATO et al., 2025).

Os resultados serão apresentados de forma clara e acessível, com a contagem numérica de ovos destacada em uma seção dedicada. Além disso, a interface incluirá marcações visuais na imagem processada, indicando a localização dos ovos detectados pelo modelo (ISAIAS, 2021). Para garantir a usabilidade em diferentes contextos, a aplicação será otimizada para desempenho, permitindo seu uso tanto em laboratórios quanto em ambientes rurais com recursos limitados (FILGUEIRA et al., 2020).

A implementação seguirá boas práticas de desenvolvimento, com modularização do código e documentação técnica detalhada, facilitando futuras atualizações e adaptações (STREAMLIT, 2025). A flexibilidade do sistema permitirá, por exemplo, a inclusão de suporte para novas espécies de nematoides ou adaptações regionais, expandindo seu alcance e aplicabilidade (LAMBERT et al., 2023). Essa abordagem assegura que a ferramenta não apenas atenda às necessidades imediatas do projeto, mas também se mantenha relevante diante de demandas futuras.

---

### **Resultados esperados**

Espera-se que a padronização e otimização do processo de extração e preparação de amostras de ovos de nematoides de raízes de quiabeiro resulte na obtenção de suspensões homogêneas, com baixa interferência de detritos, adequadas para a captura de imagens de alta qualidade em microscopia. A partir dessa padronização, a implementação de um protocolo para a captura de imagens digitais deverá garantir fotografias consistentes quanto à iluminação, foco e densidade de ovos por quadrante, possibilitando a construção de um banco de dados visual confiável e reproduzível.

Com base nesse banco de imagens, espera-se criar um dataset anotado e validado por especialistas em nematologia, com segmentações precisas de cada ovo de nematoide, que sirva como base de treinamento e avaliação dos modelos de Redes Neurais Convolucionais (CNNs). A validação dos modelos deverá demonstrar que a contagem automatizada pode atingir níveis de acurácia semelhantes ou superiores à contagem manual, com maior agilidade e menor suscetibilidade à fadiga ou erro humano. Espera-se, também, a identificação de métricas estatísticas sólidas, como baixo erro médio absoluto e alta correlação com os valores de referência.

Por fim, com a consolidação da metodologia, será possível disponibilizar uma interface de usuário intuitiva, capaz de realizar a contagem automatizada a partir de imagens carregadas diretamente pelo usuário, promovendo a democratização do acesso ao diagnóstico fitossanitário. A aplicação dos resultados deverá fortalecer o manejo de nematoides na cultura do quiabo, especialmente em contextos de agricultura familiar no semiárido, contribuindo para a sustentabilidade e a segurança alimentar dessas comunidades.

---

### **Referência bibliográfica**

**1. Artigos Científicos:**

* BARBEDO, Jayme Garcia Arnal. Digital image processing techniques for detecting, quantifying and classifying plant diseases. **SpringerPlus**, 2013, v. 2, p. 660. Disponível em: [http://www.springerplus.com/content/2/1/660](http://www.springerplus.com/content/2/1/660). Acesso em: 09 jul. 2025.
* FORTUNATO, H. F. M.; FIGUEIRA, R. M. A.; SOUZA, R. F. M. de; THEODORO JUNIOR, N.; MELLO, V. B. B. Artificial intelligence as an ally to assess and manage the golden mussel (*Limnoperna fortunei* (Dunker, 1857)) bioinvasion. **Aquatic Sciences**, v. 87, n. 53, p. 1-10, 2025. Disponível em: [https://doi.org/10.1007/s00027-025-01177-z](https://doi.org/10.1007/s00027-025-01177-z). Acesso em: 09 jul. 2025.
* MOENS, M.; PERRY, R.N.; STARR, J.L. (2009) *Meloidogyne* species – a diverse group of novel and important plant parasites. In: PERRY, R. N.; MOENS, M.; STARR, J.L. (Eds). **Root-knot nematodes**, CAB International, Wallingford, UK, pp. 01-17.
* FILGUEIRA, H. T. R. et al. Reação de resistência de genótipos de quiabeiro ao *Meloidogyne incognita* raça 1. **Brazilian Journal of Development**, Curitiba, v. 6, n. 6, p. 40776-40785, jun. 2020. DOI: 10.34117/bjdv6n6-569. Disponível em: [https://www.brazilianjournaldevelopment.com.br/article/569](https://www.brazilianjournaldevelopment.com.br/article/569). Acesso em: 09 jun. 2025.
* LAMBERT, José Carlos; MOULIN, Monique Moreira; SOUZA, Antônio Fernando de. **Método de detecção de nematoides das galhas em tomateiro**. Vitória: Edifes Acadêmico, 2023. ISBN 978-85-8263-721-0. Disponível em: [https://repositorio.ifes.edu.br/bitstream/handle/123456789/3496/Manual_Tecnico%20J%20C%20Lambert%20%281%29.pdf?sequence=4&isAllowed=y](https://repositorio.ifes.edu.br/bitstream/handle/123456789/3496/Manual_Tecnico%20J%20C%20Lambert%20%281%29.pdf?sequence=4&isAllowed=y). Acesso em: 09 jun. 2025.
* DIAS, Waldir Pereira; GARCIA, Antônio; SILVA, João Flávio Veloso; CARNEIRO, Geraldo E. de Souza. **Nematóides em soja: identificação e controle**. Londrina, PR: Embrapa Soja, 2010. ISSN 2176-2864. Disponível em: [https://www.embrapa.br/soja](https://www.embrapa.br/soja). Acesso em: 09 jun. 2025.

**2. Trabalhos Acadêmicos**

* ISAIAS, Pedro Henrique. **Técnicas de visão computacional para contagem de ovos de nematoides-das-galhas (*Meloidogyne spp*.)**. 2021. Trabalho de Conclusão de Curso (Bacharelado em Ciência da Computação) – Instituto Federal Goiano, Campus Morrinhos, 2021. Acesso em: 09 jun. 2025.

**3. Documentos Oficiais e Relatórios**

* BRASIL. Instituto Brasileiro de Geografia e Estatística (IBGE). **Produção Agrícola Municipal: Culturas Temporárias e Permanentes**. Rio de Janeiro: IBGE, 2023. Disponível em: [https://www.ibge.gov.br](https://www.ibge.gov.br). Acesso em: 09 jul. 2025.

**4. Softwares e Ferramentas**

* STREAMLIT. **Streamlit Docs**. 2025. Disponível em: [https://docs.streamlit.io/](https://docs.streamlit.io/). Acesso em: 09 jul. 2025.
