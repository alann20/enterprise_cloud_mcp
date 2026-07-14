# 🚀 Enterprise Cloud MCP Server

## 📖 Descripción

**Enterprise Cloud MCP Server** es un proyecto desarrollado en **Python** utilizando el **SDK oficial de Model Context Protocol (MCP)**. Su objetivo es demostrar cómo construir un servidor MCP capaz de exponer herramientas (**Tools**) para apoyar escenarios de **Arquitectura Empresarial**, **Arquitectura Cloud** y **Arquitectura de Soluciones**.

El proyecto implementa un servidor compatible con **MCP Inspector**, permitiendo descubrir, ejecutar y probar herramientas de forma interactiva mediante el protocolo **Model Context Protocol (MCP)** utilizando el transporte **Streamable HTTP**.

---

# 🎯 Objetivos

* Comprender la arquitectura de **Model Context Protocol (MCP)**.
* Implementar un servidor MCP desde cero utilizando Python.
* Exponer herramientas reutilizables mediante MCP.
* Integrar el servidor con **MCP Inspector**.
* Construir una base para futuros asistentes de **Arquitectura Empresarial**.

---

# 🏗️ Arquitectura

```text
                    +----------------------+
                    |    MCP Inspector     |
                    +----------+-----------+
                               |
                               |
                      Streamable HTTP
                               |
                               |
                    http://127.0.0.1:8000/mcp
                               |
               +---------------+---------------+
               |                               |
        Enterprise Cloud MCP Server
               |
        +------+------+----------------+
        |             |                |
   health_check      add     cloud_architecture
```

---

# 🛠️ Tecnologías

* Python 3.12
* Model Context Protocol (MCP)
* FastMCP
* Streamable HTTP
* MCP Inspector

---

# ⚙️ Funcionalidades

## ✅ Health Check

Permite verificar que el servidor MCP se encuentre funcionando correctamente.

### Salida

* Estado del servidor
* Nombre del servicio
* Timestamp UTC

---

## ➕ Add

Herramienta utilizada para validar la comunicación entre **MCP Inspector** y el servidor.

### Entrada

```text
a = 10
b = 20
```

### Salida

```text
30
```

---

## ☁️ Cloud Architecture

Devuelve una arquitectura empresarial para una plataforma de **Real-Time Fraud Detection** sobre AWS.

### Incluye

* Componentes de la solución
* Flujo de datos
* Servicios AWS utilizados
* Arquitectura de referencia

---

# 🚀 Instalación

Crear el entorno virtual:

```bash
python -m venv .venv
```

Activar el entorno virtual (Windows):

```bash
.venv\Scripts\activate
```

Instalar las dependencias:

```bash
pip install mcp
```

---

# ▶️ Ejecución

## Iniciar el servidor MCP

```bash
python server.py --transport streamable-http
```

Servidor disponible en:

```text
http://127.0.0.1:8000/mcp
```

---

## Ejecutar MCP Inspector

```bash
npx @modelcontextprotocol/inspector
```

Configurar:

**Transport**

```text
Streamable HTTP
```

**URL**

```text
http://127.0.0.1:8000/mcp
```

---

# 💼 Casos de uso

Este proyecto puede evolucionar para implementar herramientas como:

* Enterprise Architecture Assistant
* Cloud Architecture Advisor
* AWS Well-Architected Review
* TOGAF Assessment
* BIAN Assessment
* PCI DSS Assessment
* Kubernetes Architecture Review
* Terraform Validator
* Solution Architecture Generator
* Architecture Decision Record (ADR) Generator

---

# 🗺️ Roadmap

Próximas funcionalidades:

* Resources
* Prompts
* AI Agents
* LangGraph
* OpenAI
* Claude
* Azure OpenAI
* Amazon Bedrock
* Google Vertex AI
* Vector Database
* Retrieval-Augmented Generation (RAG)
* Enterprise Knowledge Base

---

# 📚 Aprendizajes

Durante este laboratorio se exploraron los principales componentes de **Model Context Protocol (MCP)**:

* Servidores MCP
* Clientes MCP
* Tools
* Resources
* Prompts
* Streamable HTTP
* MCP Inspector
* JSON-RPC
* Arquitectura Cliente-Servidor

---

# 📌 Referencias

* Model Context Protocol (MCP)
* MCP Python SDK
* MCP Inspector

---

# 👨‍💻 Autor

**Michel Alan López Lara**
linkedin: https://www.linkedin.com/in/michel-alan-l%C3%B3pez-lara-49a88239/

**Enterprise Data & AI Architect | Cloud Strategy | Enterprise Architecture | Generative AI**

---

⭐ Si este proyecto te resulta útil, considera darle una estrella al repositorio y compartirlo con otros profesionales interesados en Enterprise Architecture, Cloud e Inteligencia Artificial.
