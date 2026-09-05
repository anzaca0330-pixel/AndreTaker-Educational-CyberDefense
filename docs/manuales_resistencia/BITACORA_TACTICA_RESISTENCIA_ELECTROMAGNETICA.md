# BITÁCORA TÁCTICA: RESISTENCIA ELECTROMAGNÉTICA & SOBERANÍA FÍSICA
## Protocolos de Defensa Perimetral, Señuelos y Hardware Reutilizado
**Autores / Oficiales de Guardia:** Johannes (Andrea Zabala Cárcamo) & Escuadrón AndreTaker / Tycho / Baba Yaga / Arturius  
**Fecha de Registro:** 2026-09-05  
**Clasificación:** Doctrina de Ciberdefensa Educativa & Táctica Anti-Palantir  

---

### 1. EL MANIFIESTO DEL CIELO LIBRE (ANTENAS SATELITALES FTA)
* **La Realidad Oculta:** Las antenas parabólicas abandonadas de DirecTV/Dish en patios y techos son colectores de fotones de alta precisión.
* **La Física:** Los satélites geoestacionarios (a 35.786 km de la Tierra) emiten señales electromagnéticas gratuitas las 24 horas. El cielo y el espacio radioeléctrico no tienen candado por naturaleza.
* **El "Hack" Físico:** Cambiando el LNB de la punta por uno universal de Banda Ku y apuntando a satélites abiertos (Hispasat 30W, Galaxy 19, SES-6), se captan decenas de canales internacionales (DVB-S2) en Full HD sin suscripción, sin cuentas y sin internet.
* **Aspecto Legal:** 100% amparado por la ley federal de EE.UU. (FCC OTARD Rule - 47 C.F.R. § 1.4000 y Sección 705 de la Ley de Comunicaciones, 47 U.S.C. § 605). Una antena parabólica receptora es **100% PASIVA**: no emite radiofrecuencia (Zero TX), es indetectable por radar y no invade el espacio aéreo.

---

### 2. EL RETORNO AL COBRE (EL CABLE COMO ESCUDO ANTI-PALANTIR)
* **La Trampa del Aire (Wi-Fi / RF):** El Wi-Fi radia ondas esféricas en 360° que traspasan paredes y ventanas. Plataformas de correlación masiva (tipo Palantir) usan RF Fingerprinting, triangulación de presencia y recolección de metadatos aéreos.
* **La Capa 1 Inmune (Cobre Físico):**
  * Un cable de red **Ethernet (RJ45)** trenzado o un cable **HDMI** blindado transporta los electrones confinados en su interior.
  * Emisión electromagnética al exterior = **CERO**.
  * Quien esté afuera con una antena receptora solo recibe silencio en la banda donde viaja tu trabajo crítico.
  * Inmune a ataques de desautenticación remota (*Deauth*).

---

### 3. LA ESTRATEGIA DEL CEBO / HONEYPOT PERIMETRAL (TV COMO SEÑUELO)
* **Principio de Camuflaje Espectral (Traffic Masking):**
  * Si un adversario intenta monitorear la actividad de la casa, buscará picos anómalos o silencio absoluto.
  * **La Jugada Maestra:** Usar el televisor o una sesión en streaming ordinario (noticias 24/7, música o documentales públicos vía Wi-Fi) para generar un **piso de ruido uniforme y predecible**.
  * A los ojos de cualquier sniffer o algoritmo perimetral externo, la red doméstica se clasifica como tráfico de entretenimiento genérico e inocuo ("Smart TV común consumiendo video").
* **Aislamiento en Segundo Plano:**
  * Mientras el Wi-Fi mantiene entretenido y distraído al observador externo con ruido comercial ordinario, el ThinkPad procesa las bóvedas forenses inmutables y el análisis pericial en local y por cable hacia la pantalla, sin emitir un solo byte revelador al espectro aéreo.

---

### 4. ARTEFACTOS TÉCNICOS CREADOS EN LA ESTACIÓN
1. **Lanzador de Escritorio:** `~/Desktop/Servidor_TV_Soberano.desktop`
2. **Servidor Local Autónomo:** `~/Desktop/SERVIDOR_TV_SOBERANO.py`
3. **Bóveda de Medios Privada:** `~/Resistencia_Digital/` (`Videos/`, `Musica/`, `Fotos/`)
   * Acceso local para el TV: `http://192.168.1.X:8080` (Cero suscripciones, cero DRM, red cerrada).
