# Drone Disabler

Ferramenta de pesquisa em segurança para testes de vulnerabilidade em drones Parrot Bebop.

## ⚠️ Aviso Legal

**IMPORTANTE:** Esta ferramenta foi desenvolvida **EXCLUSIVAMENTE** para fins educacionais e de pesquisa em segurança autorizada. O uso de técnicas de deautenticação WiFi (jamming) é **ILEGAL** na maioria das jurisdições sem autorização explícita.

- ✅ Uso permitido: Testes de penetração autorizados, pesquisa de segurança, competições CTF, ambientes controlados
- ❌ Uso proibido: Interferência não autorizada em redes, interrupção de serviços, ataques maliciosos

**O autor não se responsabiliza pelo uso indevido desta ferramenta. Use por sua própria conta e risco.**

## 📋 Descrição

O Drone Disabler é uma ferramenta de teste de segurança que demonstra vulnerabilidades em drones Parrot Bebop através de:

1. **Escaneamento de Redes WiFi**: Identifica drones Parrot através de prefixos MAC conhecidos
2. **Ataque de Deautenticação**: Desconecta o drone do controlador usando frames de deautenticação WiFi
3. **Comando de Pouso Forçado**: Conecta-se ao drone e envia comando de pouso automático

### Como Funciona

```
┌─────────────────────┐
│ Escanear WiFi       │
│ (wlan0)             │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Detectar Drone      │
│ Parrot (MAC)        │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Criar Interface     │
│ Monitor (mon0)      │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Ataque Deauth       │
│ (aireplay-ng)       │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Conectar ao Drone   │
│ via WiFi            │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Enviar Comando      │
│ de Pouso            │
└─────────────────────┘
```

## 🔧 Requisitos

### Sistema Operacional
- **Linux** (testado em Debian/Ubuntu)
- **Privilégios root** (necessário para operações de rede)

### Hardware
- Adaptador WiFi compatível com modo monitor
- Interface `phy1` disponível para modo monitor

### Software
- Python 2.7
- aircrack-ng
- iw / iwconfig
- dhclient

## 📦 Instalação

### Método 1: Script Automático

Execute o script de instalação incluído:

```bash
chmod +x drone_disabler_install.sh
sudo ./drone_disabler_install.sh
```

O script irá instalar automaticamente:
- aircrack-ng (suite de testes WiFi)
- git, mercurial (controle de versão)
- vim (editor de texto)
- libsdl1.2-dev (bibliotecas SDL)
- python-pygame (biblioteca gráfica Python)
- katarina (SDK Parrot Bebop)
- python-iwlist (wrapper de escaneamento WiFi)

### Método 2: Instalação Manual

```bash
# Atualizar sistema
sudo apt-get update
sudo apt-get upgrade -y

# Instalar dependências
sudo apt-get install -y aircrack-ng git vim mercurial libsdl1.2-dev python-pygame

# Clonar dependências Python
cd /tmp
hg clone https://bitbucket.org/robotika/katarina
cd katarina
sudo python setup.py install

cd /tmp
git clone https://github.com/iancoleman/python-iwlist
cd python-iwlist
sudo python setup.py install
```

## 🚀 Uso

### Pré-requisitos
1. Certifique-se de que possui um adaptador WiFi compatível
2. Execute como root
3. Verifique que as interfaces `wlan0` e `phy1` estão disponíveis

### Executar

```bash
sudo python drone_disabler.py
```

### Comportamento Esperado

```
Escaneando redes WiFi...
Escaneando redes WiFi...
Drone Parrot detectado!
  ESSID: Bebop2-XXXXXX
  MAC: 90:03:B7:XX:XX:XX
  Canal: 6

Criando interface monitor...
Enviando ataque de deautenticação...
Conectando ao drone...
Enviando comando de pouso...
Drone desabilitado com sucesso!
```

## 🎯 Drones Suportados

A ferramenta detecta drones Parrot através dos seguintes prefixos MAC:

| Prefixo MAC | Modelo |
|-------------|---------|
| 90:03:B7    | Parrot Bebop/Bebop 2 |
| A0:14:3D    | Parrot AR.Drone |
| 00:12:1C    | Parrot (antigos) |
| 00:26:7E    | Parrot (antigos) |
| 90:3A:E6    | Parrot Disco/Mambo |

## 🛠️ Solução de Problemas

### Erro: "No wireless networks found"
- Verifique se `wlan0` está ativa: `ifconfig wlan0`
- Certifique-se de que o adaptador WiFi está conectado

### Erro: "Permission denied"
- Execute o script como root: `sudo python drone_disabler.py`

### Erro: "mon0: No such device"
- Verifique se `phy1` existe: `iw dev`
- Certifique-se de que seu adaptador suporta modo monitor

### Erro ao instalar dependências
- Use Python 2.7 (Python 3 não é compatível)
- Instale pip2: `sudo apt-get install python-pip`

## 📚 Estrutura do Projeto

```
drone_disabler/
├── README.md                    # Este arquivo
├── drone_disabler.py            # Script principal
└── drone_disabler_install.sh    # Script de instalação
```

## 🔒 Considerações de Segurança

### Aspectos Éticos
- Esta ferramenta demonstra vulnerabilidades conhecidas em drones comerciais
- Use apenas em ambientes controlados e com autorização
- Respeite as leis locais sobre interferência em sinais de rádio

### Vulnerabilidades Demonstradas
1. **Deautenticação WiFi**: Drones Parrot usam WiFi sem proteção adequada contra deauth
2. **Acesso Não Autenticado**: Conexão ao drone sem credenciais
3. **Falta de Criptografia**: Comandos enviados em texto claro

### Contramedidas
- Use drones com protocolos mais seguros (ex: OcuSync, Lightbridge)
- Implemente autenticação forte
- Use frequências menos vulneráveis (5.8GHz com proteção)

## 📖 Referências

- [Aircrack-ng Documentation](https://www.aircrack-ng.org/)
- [Parrot Bebop SDK](https://bitbucket.org/robotika/katarina)
- [WiFi Deauthentication Attack](https://en.wikipedia.org/wiki/Wi-Fi_deauthentication_attack)

## 📝 Licença

Este projeto é fornecido "como está", sem garantias de qualquer tipo. Use por sua própria conta e risco.

## 🤝 Contribuições

Contribuições são bem-vindas! Antes de contribuir:
1. Certifique-se de que suas mudanças são éticas
2. Teste em ambiente controlado
3. Documente suas alterações

## ⚡ Aviso Final

**Esta ferramenta foi criada para demonstrar vulnerabilidades de segurança em drones comerciais com o objetivo de melhorar a segurança de sistemas autônomos. Qualquer uso malicioso ou ilegal é de responsabilidade exclusiva do usuário.**

---

**Desenvolvido para fins educacionais e de pesquisa em segurança** 🛡️
