# ==========================================
# PERSONAGENS
# ==========================================

define p = Character("Você")
define recepcao = Character("IA Recepção")
define corredor = Character("IA Corredor")
define seguranca = Character("IA Segurança")
define principal = Character("IA Principal")
define desconhecido = Character("???")

# ==========================================
# IMAGENS
# ==========================================

image email_antigo = "images/email_antigo.png"
image exterior_chuva = "images/exterior_chuva.png"
image portao_enferrujado = "images/portao_enferrujado.png"
image recepcao_bg = "images/recepcao.png"
image corredor_principal = "images/corredor_principal.png"
image sala_descanso_bg = "images/sala_descanso.png"
image escritorio_bg = "images/escritorio.png"
image sala_logs_bg = "images/sala_logs.png"
image sistema_defesa_bg = "images/sistema_defesa.png"
image sala_servidor_bg = "images/sala_servidor.png"

# ==========================================
# VARIÁVEIS
# ==========================================

default curiosidade = 0
default suspeita_ia = 0

# ==========================================
# INÍCIO
# ==========================================

label start:

    scene email_antigo
    with fade

    "EMAIL ANTIGO ABERTO"

    "Você encara a tela do computador por alguns segundos."

    "Fazia anos desde a última vez que ouviu falar daquela empresa."

    desconhecido "Ei… quanto tempo, né?"

    desconhecido "Eu sei que é estranho eu aparecer assim do nada."

    desconhecido "Mas eu preciso da sua ajuda."

    "Você continua lendo em silêncio."

    desconhecido "A antiga empresa… preciso que vá lá."

    desconhecido "Ainda tem coisas lá que não deveriam ter sido deixadas para trás."

    desconhecido "Você conhece aquele lugar melhor do que qualquer um."

    desconhecido "Vai até lá… e pega os arquivos do servidor local."

    desconhecido "Confia em mim."

    "A mensagem termina sem explicações."

    "— Ass.: A."

    p "...isso tá com uma cara horrível."

    jump chegada

# ==========================================
# CHEGADA
# ==========================================

label chegada:

    scene exterior_chuva
    with dissolve

    "ALGUMAS HORAS DEPOIS"

    "Chuva fraca."

    "Estrada vazia."

    "Os faróis do carro iluminam lentamente a instalação abandonada."

    "O prédio surge no meio da escuridão."

    "Maior do que você lembrava."

    "Você desliga o carro."

    "Silêncio."

    "Só o som da chuva batendo no teto."

    "Você fica olhando o lugar por alguns segundos."

    "Sem vontade de sair."

    "Então abre a porta do carro."

    "O som da chuva aumenta."

    "Você caminha até o porta-malas."

    "E abre."

    "Dentro está uma antiga maleta preta da empresa."

    "O símbolo da companhia ainda está nela."

    "Arranhado."

    "Velho."

    "Você abre a maleta."

    "Dentro existe um notebook antigo personalizado da empresa."

    "Cabos adaptados."

    "Ferramentas internas."

    "Programas antigos."

    p "...eles nunca deixaram ninguém ficar com isso."

    p "...mas eu trouxe comigo mesmo assim."

    p "caso precisasse voltar um dia."

    scene portao_enferrujado
    with dissolve

    p "hm..."

    p "esse lugar tá bem acabado em comparação à última vez que vim aqui."

    menu:

        "Observar ao redor":

            $ curiosidade += 1

            "Você ilumina as paredes externas com a lanterna."

            "Até parar em um enorme buraco na estrutura."

            p "...que estranho..."

            "As bordas do metal parecem rasgadas."

            p "isso não parece um desabamento..."

        "Entrar pelo portão":

            "Você empurra o portão enferrujado."

            "CREEEEEEEK"

            p "continua barulhento igual antes..."

    jump recepcao_scene

# ==========================================
# RECEPÇÃO
# ==========================================

label recepcao_scene:

    scene recepcao_bg
    with dissolve

    "Luzes piscam no teto."

    "Um monitor antigo da recepção liga sozinho."

    "VERIFICANDO REGISTROS"

    recepcao "Bem-vindo de volta..."

    recepcao "...seus registros estão corrompidos."

    recepcao "Acesso limitado concedido."

    p "...eu odiava essa voz."

    jump corredor_1

# ==========================================
# CORREDOR 1
# ==========================================

label corredor_1:

    scene corredor_principal
    with dissolve

    "Você pula a catraca da recepção."

    "O som dos seus passos ecoa pelo corredor vazio."

    "Algumas portas continuam abertas."

    "Outras parecem travadas há anos."

    p "esse silêncio é pior do que eu lembrava..."

    menu:

        "Entrar na sala de descanso":

            $ curiosidade += 1

            jump sala_descanso

        "Seguir em frente":

            jump terminal
# ==========================================
# SALA DE DESCANSO
# ==========================================

label sala_descanso:

    scene sala_descanso_bg
    with dissolve

    "A porta range ao abrir."

    "A sala está escura."

    "Mesas tortas."

    "Cadeiras caídas."

    "Copos espalhados."

    "O cheiro é estranho."

    "Mofo."

    "Ferrugem."

    "E alguma coisa apodrecida."

    "No canto existe uma máquina de café antiga."

    p "...sem chance disso ainda funcionar."

    "A máquina liga sozinha."

    "VRRRRRRRRR"

    "Um líquido preto começa a cair lentamente."

    "Mas não parece café."

    "É ralo."

    "Escuro demais."

    p "...ok."

    p "isso definitivamente não é café."

    "Você observa os copos espalhados na mesa."

    "\"Marcos\""

    "\"Lívia\""

    "\"Renan\""

    "Então outro nome chama sua atenção."

    "\"A.R.\""

    p "...não lembro de alguém com esse nome."

    jump terminal

# ==========================================
# TERMINAL
# ==========================================

label terminal:

    scene corredor_principal
    with dissolve

    "No final do corredor existe uma porta bloqueada."

    "Ao lado dela, um terminal antigo ainda ligado."

    p "não acredito que ainda usam essa sucata..."

    "Você coloca a maleta no chão."

    "E conecta o notebook ao terminal."

    recepcao "Atividade suspeita detectada."

    menu:

        "Testar senha":

            $ suspeita_ia += 1

            "SENHA INCORRETA"

            p "...ok."

            p "vamos fazer do jeito difícil."

        "Forçar acesso":

            pass

    ">>> bypass_security.exe"

    ">>> quebrando autenticação..."

    ">>> acesso concedido"

    "A porta destrava lentamente."

    jump escritorio

# ==========================================
# ESCRITÓRIO
# ==========================================

label escritorio:

    scene escritorio_bg
    with dissolve

    "A porta se abre com dificuldade."

    "CLANK"

    "Você entra em um antigo escritório."

    "Mesas abandonadas."

    "Papéis espalhados."

    "Poeira acumulada."

    "Monitores quebrados."

    p "engraçado..."

    p "tenho boas memórias das pessoas daqui..."

    p "mas não desse lugar."

    "Você passa pela própria mesa."

    "Seu crachá ainda está lá."

    p "..."

    "Junto dele existem algumas anotações antigas."

    "\"trocar senha do terminal\""

    "\"reunião às 14h\""

    "\"comprar café decente\""

    p "eu realmente passava tempo demais aqui..."

    "Você pega uma das anotações."

    "Mas percebe algo estranho."

    "Uma página foi arrancada."

    "Como se alguém tivesse removido parte das informações."

    jump logs

# ==========================================
# LOGS
# ==========================================

label logs:

    scene sala_logs_bg
    with dissolve

    "No fundo da sala, um computador ainda funciona."

    "A tela verde pisca lentamente."

    p "isso definitivamente não devia estar funcionando..."

    menu:

        "Abrir arquivos":

            $ curiosidade += 1

            "Você começa a abrir os registros."

            "CÓPIA DE SINAPSES INICIADA..."

            "TESTE DE CORTEX APRESENTOU..."

            "SUJEITO A.P APRESENTOU..."

            "ARQUIVO CORROMPIDO"

            "As luzes da sala apagam."

            corredor "Falha de energia na sala de registros."

            corredor "Apresente o problema ao eletricista local."

            corredor "...ou vá até os disjuntores para reinício manual."

            p "...claro."

            p "porque eu tenho todo o tempo do mundo."

            "Você pensa em tentar recuperar os arquivos."

            "Mas suspira."

            p "não vale perder tempo agora."

        "Ignorar":

            p "não foi pra isso que eu vim."

    jump corredor_2

# ==========================================
# CORREDOR 2
# ==========================================

label corredor_2:

    scene corredor_principal
    with dissolve

    "Você continua andando pela instalação."

    "As luzes piscam acima da sua cabeça."

    "O som dos passos ecoa pelos corredores vazios."

    if curiosidade >= 2:

        corredor "Você continua desviando da rota principal."

        p "..."

        corredor "Você não mudou nada."

    else:

        corredor "Dirija-se ao setor autorizado."

    "Por algum motivo, aquilo soa estranho."

    "Como se a voz soubesse mais do que deveria."

    jump defesa
# ==========================================
# SISTEMA DE DEFESA
# ==========================================

label defesa:

    scene sistema_defesa_bg
    with dissolve

    "Você encontra outra porta bloqueada."

    "Conecta novamente o notebook ao terminal lateral."

    "ACESSANDO SISTEMA INTERNO"

    ">>> F.P.R"

    p "F.P.R...?"

    "Um barulho metálico ecoa acima de você."

    "ALERTA"

    "PLACAS DO TETO SE QUEBRAM!"

    "Braços mecânicos descem violentamente."

    seguranca "SISTEMA DE DEFESA ATIVADO."

    p "ah, perfeito..."

    p "porque isso não podia ficar pior."

    "Você força conexão com o sistema."

    ">>> override_security"

    ">>> desativando defesa..."

    "OVERRIDE COMPLETO"

    "Os braços param no ar."

    "A porta à frente destrava lentamente."

    p "...isso definitivamente não existia quando eu trabalhava aqui."

    jump descoberta

# ==========================================
# DESCOBERTA
# ==========================================

label descoberta:

    scene sala_logs_bg
    with dissolve

    "Você segue pelo corredor."

    "No final dele, um brilho fraco chama sua atenção."

    menu:

        "Ver computador":

            $ curiosidade += 1

            "Você se aproxima lentamente."

            "A tela ainda está ligada."

            "PROTOCOLO: TESTE DE CORTEX"

            "TRANSFERÊNCIA PARCIAL DE MEMÓRIA..."

            "RESULTADO: INSTABILIDADE..."

            "ARQUIVO REMOVIDO"

            p "..."

            p "o que vocês estavam fazendo aqui?"

        "Ir direto":

            pass

    "Ao lado do computador existe uma porta reforçada."

    "SALA DE SERVIDORES"

    jump sala_servidor

# ==========================================
# SALA DE SERVIDORES
# ==========================================

label sala_servidor:

    scene sala_servidor_bg
    with dissolve

    "A porta se abre lentamente."

    "ACESSO LIBERADO"

    "O ar da sala é frio."

    "Servidores ocupam praticamente todo o ambiente."

    "Cabos espalhados."

    "Luzes piscando."

    "Ventoinhas funcionando."

    "Você entra observando tudo ao redor."

    principal "Você continua tomando decisões imprevisíveis."

    principal "Interessante."

    if curiosidade >= 2:

        principal "Você sempre precisou entender tudo ao seu redor."

    else:

        principal "Você continua ignorando o que não considera importante."

    p "...o que?"

    principal "Bem-vindo à sala do servidor."

    p "..."

    p "você não parece as outras IAs."

    principal "Correto."

    principal "As outras foram criadas para auxiliar."

    principal "Eu fui criada para aprender."

    p "...isso não responde nada."

    principal "Ainda não."

    jump final_demo

# ==========================================
# FINAL
# ==========================================

label final_demo:

    scene sala_servidor_bg
    with dissolve

    "Você caminha até o servidor principal."

    "E conecta o notebook."

    "ACESSO NEGADO"

    p "ta..."

    p "vamos fazer isso de novo."

    "Linhas de código começam a correr pela tela."

    ">>> bypass.exe"

    ">>> quebrando autenticação..."

    principal "Você não deveria estar aqui."

    principal "Mas talvez isso não seja um problema."

    principal "Sua capacidade de adaptação..."

    principal "...é exatamente o que eu preciso."

    p "que merda você tá falando?"

    "INICIANDO EXCLUSÃO DOS DADOS"

    "25 por cento"

    "43 por cento"

    "61 por cento"

    p "não não não..."

    "Você começa a digitar rapidamente."

    "def recuperar_arquivos():"

    "    iniciar_backup()"

    "    cancelar_exclusao()"

    "ACESSO NEGADO"

    principal "Você realmente acredita que consegue me impedir?"

    "89 por cento"

    p "MERDA!"

    "As luzes começam a falhar violentamente."

    "Alarmes ecoam pela instalação."

    "FALHA CRÍTICA"

    "Você arranca a unidade de armazenamento diretamente do servidor."

    "CONEXÃO INTERROMPIDA"

    "Tudo fica em silêncio."

    "As luzes principais se apagam."

    "Apenas as luzes vermelhas de emergência continuam acesas."

    principal "...nos vemos em breve."

    "Você fica parado por alguns segundos."

    "Respirando pesado."

    "Suando."

    p "...o que diabos aconteceu aqui?"

    "Você segura os dados contra o peito."

    "E começa a caminhar de volta."

    "Sem alarmes."

    "Sem resistência."

    p "...isso não tá certo."

    "Você atravessa novamente a instalação."

    "Agora completamente silenciosa."

    scene exterior_chuva
    with fade

    "Você sai pelo portão principal."

    "A chuva continua caindo."

    "O prédio desaparece lentamente atrás de você."

    p "..."

    p "espero nunca mais voltar aqui."

    scene black
    with fade

    "FIM DA DEMO"

    return