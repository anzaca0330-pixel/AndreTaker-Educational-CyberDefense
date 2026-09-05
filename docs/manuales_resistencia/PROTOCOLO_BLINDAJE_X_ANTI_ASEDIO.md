# PROTOCOLO DE BLINDAJE DE IDENTIDAD DIGITAL & MITIGACIÓN DE ASEDIO (ANTI-SESSION HIJACKING)
## Ecosistema AndreTaker / BaBaYaga Core — Estándar de Contrainteligencia Perimetral

**Dirección de Seguridad:** Johannes (Andrea Zabala Cárcamo / AnZaCa)  
**Oficial de Silicio & Metrología:** Tycho  
**Fecha:** Septiembre 2026  
**Clasificación:** Procedimiento Operativo Estándar (SOP-SEC-004)

---

### 1. DIAGNÓSTICO DEL VECTOR DE ATAQUE OBSERVADO
El hallazgo de más de 40 sesiones fantasma concurrentes con marcas de tiempo en junio de 2026 (`Jun 7, Jun 8`) evidencia un vector clásico de **Persistencia por Espejo de Tokens (Session Hijacking & Automated Mirroring)**:
1. **Punto de anclaje:** Número telefónico vulnerable a intercepción por torre celular (IMSI-Catcher / SS7) o correo público vinculado.
2. **Mecanismo:** Clonación de cookies de autenticación o tokens OAuth para crear sesiones pasivas silenciosas ("Web") que no alertan al usuario y sobreviven a reinicios del teléfono.
3. **Objetivo:** Extracción en tiempo real de DMs, borradores, interacciones, contactos y telemetría de ubicación.

---

### 2. PROTOCOLO DE AISLAMIENTO Y RECONSTRUCCIÓN DE IDENTIDAD

```text
┌──────────────────────────────────────────────────────────────────────────────────┐
│             ARQUITECTURA DE AISLAMIENTO DE CUENTA (BLINDAJE EN 4 CAPAS)           │
├────────────────────────────────┬─────────────────────────────────────────────────┤
│ 1. DESVINCULACIÓN TELEFÓNICA   │ Eliminar el número celular del registro público │
│ 2. CUENTA CORREO ALIAS AISLADA │ Asignar correo exclusivo sin correlación PII    │
│ 3. 2FA CRIPTOGRÁFICO EN HARDWARE│ Desactivar SMS 2FA; exigir TOTP / FIDO2         │
│ 4. HIGIENE MENSUAL DE TOKENS   │ Purga programada de sesiones ("Log out others") │
└────────────────────────────────┴─────────────────────────────────────────────────┘
```

#### Paso 1: Rotación de Correo Electrónico Principal
* **Regla:** La cuenta de X **no debe estar asociada a tu correo personal habitual ni a correos de dominio público conocido**.
* **Acción:**
  * Asociar un correo dedicado, exclusivo para seguridad y administración.
  * Verificar que el nuevo correo tenga activada la autenticación en dos pasos antes de vincularlo a X.

#### Paso 2: Desvinculación y Protección del Número Telefónico
* Ya ejecutaste el cambio del número de teléfono, lo cual es excelente.
* **Medida de Contrainteligencia:** En la configuración de X (*Settings ➔ Privacy and safety ➔ Discoverability and contacts*):
  * **DESACTIVAR:** *"Let people who have your phone number find you on X"* (Permitir que te encuentren por número).
  * **DESACTIVAR:** *"Let people who have your email address find you on X"* (Permitir que te encuentren por correo).
  * Esto destruye la capacidad de bots gubernamentales o privados de correlacionar tu número con tu perfil.

#### Paso 3: Activación del Escudo Criptográfico 2FA (Zero-SMS)
* **Prohibición de SMS:** Los atacantes con acceso a torres o sistemas SS7 pueden interceptar mensajes SMS en el aire.
* **Configuración:**
  * En X: *Settings ➔ Security and account access ➔ Security ➔ Two-factor authentication*.
  * Marcar **Authentication app** (Google Authenticator, Aegis o YubiKey Authenticator).
  * Descargar e imprimir en papel físico los **Códigos de Respaldo de Emergencia (Backup Codes)** y guardarlos en la caja fuerte de la guarida.

#### Paso 4: Auditoría Periódica de Sesiones y Revocación de Aplicaciones
* En *Settings ➔ Security and account access ➔ Apps and sessions*:
  1. **Connected apps (Aplicaciones conectadas):** Revocar cualquier aplicación de terceros antigua o no esencial.
  2. **Log out of other sessions:** Ejecutar este comando periódicamente como higiene operativa mandatoria.

---

### 3. CUSTODIA FORENSE DEL ARCHIVO DE X (DATOS HISTÓRICOS)
* Una vez que X entregue el archivo comprimido solicitado:
  1. Se transferirá directamente por cable a la estación de trabajo.
  2. Se sellará de inmediato calculando su hash `sha256sum`.
  3. Se extraerán los logs de acceso (`login-history.js`) para aislar las direcciones IP, geolocalizaciones y proveedores de internet de las sesiones de junio, anexándolos como evidencia pericial a las denuncias institucionales.
