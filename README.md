# 🔒 Bookstore API - Secure Token Authentication & DRF

Este projeto eleva a Bookstore API para um nível de produção, focando na segurança e proteção de dados. Implementei um sistema de **Autenticação via Token** utilizando o Django REST Framework para garantir que os recursos da API sejam acessíveis apenas por usuários autenticados.

---

# 📝 Resumo (Resume)
Neste projeto, configurei o ecossistema de segurança da API através do `rest_framework.authtoken`. Estabeleci políticas globais no `settings.py` que exigem autenticação para qualquer requisição (`IsAuthenticated`). Isso significa que a aplicação agora valida a identidade do usuário através de um cabeçalho de autorização antes de processar qualquer operação no banco de dados. Além disso, estruturei a aplicação de forma modular, separando as rotas da API das configurações de núcleo do Django, seguindo os melhores padrões de arquitetura corporativa.



## 🚀 Tecnologias e Ferramentas (Tech Stack)

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/DRF_Auth-A30000?style=for-the-badge&logo=django&logoColor=white)](https://www.django-rest-framework.org/)
[![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/)

## 📋 Funcionalidades em Destaque
* **Autenticação via Token:** Implementação de `TokenAuthentication`, onde o cliente envia uma chave única no Header da requisição para validar o acesso.
* **Permissões Globais:** Configuração de `DEFAULT_PERMISSION_CLASSES` para bloquear acessos anônimos em todos os endpoints por padrão.
* **Mapeamento de Modelos Seguro:** Uso de serializers para controlar exatamente quais campos (`id`, `nome`, `preco`, `descricao`) são expostos na API.
* **Arquitetura ASGI/WSGI:** Preparação do servidor para diferentes ambientes de execução, garantindo compatibilidade com servidores modernos e tradicionais.
* **Persistência de Usuários:** Uso do sistema nativo de autenticação do Django para gerenciar tokens vinculados a usuários reais.
* **Modularidade de Apps:** Registro da aplicação `products` e do sistema de tokens no `INSTALLED_APPS` para manter o código organizado e escalável.



---

# 👨‍💻 Sobre mim (About Me)
Olá, meu nome é **Kaio**, tenho 22 anos. Como meu foco principal é o **Back-End com Python**, dominar a segurança é um passo essencial. No Front-End com **React**, eu aprendi a enviar requisições; agora, no Back-End, aprendi a construir a barreira de proteção que valida essas requisições. Entender como os tokens funcionam me permite criar sistemas que protegem as informações dos usuários e garantem que as regras de negócio sejam aplicadas apenas por quem tem permissão.

### Entre em contato (Contact me)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-000?style=for-the-badge&logo=linkedin&logoColor=092E20)](https://linkedin.com/in/kaio-grativol-baldo-071a74150/)
[![Instagram](https://img.shields.io/badge/Instagram-000?style=for-the-badge&logo=instagram&logoColor=092E20)](https://www.instagram.com/kaiull__/)
[![GitHub](https://img.shields.io/badge/Github-000?style=for-the-badge&logo=github&logoColor=092E20)](https://github.com/SeuUsuarioAqui)

---
*Projeto desenvolvido para consolidar conhecimentos em segurança de APIs e autenticação baseada em tokens com DRF.*
