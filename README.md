# 🎓 AndreTaker — BabaYaga Core Educational Module
### Framework Pedagógico de Ciberdefensa, Alfabetización Digital & Juego Cívico "Guardianes Digitales"

![Version](https://img.shields.io/badge/Edition-Dual--Tier_RPG_v1.0-cyan.svg)
![Framework](https://img.shields.io/badge/Pedagogical-BabaYaga_Core-blueviolet.svg)
![License](https://img.shields.io/badge/License-Creative%20Commons%20BY--NC--SA%204.0-green.svg)
![Audience](https://img.shields.io/badge/Audience-Kids%20%7C%20Students%20%7C%20Citizens-orange.svg)
![Security](https://img.shields.io/badge/OpSec-Zero--Leakage-red.svg)

---

## 🎯 MISIÓN Y PROPÓSITO EDUCATIVO

El módulo educativo **AndreTaker — BabaYaga Core Educational Module** es una iniciativa de alfabetización tecnológica, soberanía digital y ciberdefensa ciudadana diseñada y dirigida por **Andrea Zabala Cárcamo (AnZaCa / AndreTaker)**. Su objetivo es democratizar la comprensión de conceptos avanzados de seguridad informática (criptografía, detección de manipulaciones digitales, auditoría de datos, soberanía de redes e ingeniería social) a través de la pedagogía activa y la gamificación táctica dual (para niños y adultos).

> **💡 NOTA METODOLÓGICA:**  
> Este repositorio constituye el **módulo pedagógico y formativo independiente**. La evidencia técnica forense dura, peritajes judiciales para tribunales internacionales (CIDH/FBI) y descompilación binaria ISO 32000-1 se preservan de forma rigurosa en el **[Repositorio Judicial Maestro](https://github.com/anzaca0330-pixel/AndreTaker-BabaYaga-Core-CyberDefense)** y en **[andretaker.org](https://www.andretaker.org/)**.

---

## 🛡️ LOS TRES PILARES PEDAGÓGICOS

```
                    ┌─────────────────────────────────────────┐
                    │      FRAMEWORK EDUCATIVO ANDRETAKER     │
                    └────────────────────┬────────────────────┘
                                         │
         ┌───────────────────────────────┼───────────────────────────────┐
         ▼                               ▼                               ▼
┌──────────────────┐            ┌──────────────────┐            ┌──────────────────┐
│  1. ALFABETIZACIÓN│           │ 2. JUEGO TÁCTICO │            │  3. GUÍAS CÍVICAS│
│    DIGITAL CIUDADANA│         │ "GUARDIANES RPG" │            │  Y ANTI-ESTAFAS  │
├──────────────────┤            ├──────────────────┤            ├──────────────────┤
│ • ¿Qué es un Hash?│           │ • Simulación por │            │ • Escudo contra  │
│ • Integridad SHA │            │   turnos en CLI  │            │   Job Scams/Phish│
│ • Lectura de actas│           │ • Los 6 Agentes  │            │ • Defensa del    │
│ • Ley de Benford  │           │ • Resistencia cív│            │   usuario común  │
└──────────────────┘            └──────────────────┘            └──────────────────┘
```

### 1. Alfabetización Digital y Ciencia de Datos Explicada
Módulos sin jerga técnica pesada diseñados para que estudiantes de secundaria, universitarios y ciudadanos entiendan:
- **Criptografía sin miedo:** ¿Por qué un hash SHA-256 es una "huella digital matemática" que no se puede falsificar?
- **La Ley de Benford (2BL):** Cómo los números en la naturaleza y en las elecciones siguen patrones que revelan anomalías.
- **Análisis de Metadatos:** Cómo inspeccionar la fecha de creación y las capas ocultas de un archivo.

👉 Consulta el documento maestro: **[EDUCATIONAL_FRAMEWORK_SPEC.md](docs/EDUCATIONAL_FRAMEWORK_SPEC.md)**.

---

### 2. El Juego Táctico Cívico: "Guardianes Digitales" (CLI RPG)
Un simulador pedagógico por turnos desarrollado en Python para enseñar conceptos de mitigación cibernética mediante juego de roles:
- **El Roster de Silicio y Humano:** Cada personaje representa un pilar de la ciberdefensa:
  - 🛡️ **AndreTaker (AnZaCa):** Estrategia de resistencia, psicología I-O y coordinación.
  - 🔭 **Tycho:** Instrumento de Silicio, medición metrológica y hashes SHA-256.
  - 🔍 **Kepler:** Armonizador orbital y estructuración de datos.
  - 🪓 **Baba Yaga:** Bisturí forense, descompilación binaria y anti-Palantir.
  - ⚔️ **Michael (Chris Báez):** Coordinación táctica, radio analógica y protocolo físico.
  - ⚙️ **Arthurius (11 años):** El Integrador y balanceador de carga.
  - 🐶 **Tobias y Bianca:** Centinelas perimetrales contra intrusiones.

#### 🎮 Cómo Ejecutar el Juego:
```bash
python3 game/play_cyberdefense_game.py
```
👉 Especificación de personajes y mecánicas: **[CHARACTERS_DUAL_RPG_SPEC.md](docs/CHARACTERS_DUAL_RPG_SPEC.md)**.

---

### 3. Escudo de Autodefensa Personal y Contra-Ingeniería Social
Herramientas prácticas para que estudiantes y profesionales protejan su identidad en el mundo real:
- Detección de ofertas de trabajo fraudulentas (*Job Scams* en plataformas universitarias como Handshake/LinkedIn).
- Prevención de phishing bancario y robo de números de seguro social (SSN) o pasaportes.

---

## ⚖️ POLÍTICA DE LICENCIAMIENTO & DELIMITACIÓN OPEN SOURCE

Para garantizar la máxima transparencia y blindaje legal, este repositorio delimita explícitamente qué componentes son de código abierto y cuáles constituyen propiedad intelectual reservada:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│             DELIMITACIÓN DE LICENCIAS (OPEN SOURCE VS. RESERVADO)           │
├──────────────────────────────────────┬──────────────────────────────────────┤
│ 🟢 OPEN SOURCE (CÓDIGO ABIERTO)      │ 🔴 PROPIEDAD INTELECTUAL & RESERVA   │
├──────────────────────────────────────┼──────────────────────────────────────┤
│ • Scripts y motores en Python        │ • Metodología pericial de auditoría  │
│   (game/play_cyberdefense_game.py)   │ • Narrativa, lore de personajes      │
│ • Herramientas de cálculo de hashes  │   (Baba Yaga, Tycho, etc.)           │
│   y verificación matemática          │ • Diseño curricular de ciberdefensa  │
│ • Estructura de simuladores CLI/Web  │ • Evidencia forense, actas y marcas  │
│                                      │   (Bajo cadena de custodia y reserva)│
├──────────────────────────────────────┴──────────────────────────────────────┤
│ 📜 Marco Legal Aplicable:                                                   │
│ - Código y herramientas: Licencia Apache 2.0 / MIT (Reutilización libre).   │
│ - Contenido pedagógico y guías: Creative Commons BY-NC-SA 4.0 (No comercial).│
│ - Marca, acervo y autoría: © Andrea Zabala Cárcamo (AnZaCa / AndreTaker).   │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 🏛️ ECOSISTEMA DE RESISTENCIA Y AUTORÍA

- **Diseño Curricular, Lore y Dirección Pedagógica:** Andrea Zabala Cárcamo (AnZaCa / AndreTaker).
- **Licenciamiento:** Abierto para fines educativos, académicos y comunitarios conforme a la tabla de delimitación superior.
- **Repositorio Judicial Maestro:** [AndreTaker-BabaYaga-Core-CyberDefense](https://github.com/anzaca0330-pixel/AndreTaker-BabaYaga-Core-CyberDefense)

