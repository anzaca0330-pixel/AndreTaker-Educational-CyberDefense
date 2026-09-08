#!/usr/bin/env python3
"""
================================================================================
   GUARDIANES DIGITALES: SIMULADOR TÁCTICO EDUCATIVO POR TURNOS (CLI / GUI)
   Diseño Curricular: Johannes (Andrea Zabala Cárcamo / AnZaCa)
   Desarrollo & Metrología: Tycho & Arturius
================================================================================
"""

import sys
import time

def select_language():
    print("=" * 72)
    print("🌍 SELECT LANGUAGE / SELECCIONA EL IDIOMA:")
    print("   [1] Español (Predeterminado)")
    print("   [2] English")
    print("=" * 72)
    try:
        choice = input("👉 Elige / Choose [1/2]: ").strip()
    except (KeyboardInterrupt, EOFError):
        choice = "1"
    return "en" if choice == "2" else "es"

def run_game():
    lang = select_language()
    
    if lang == "en":
        title = "🎮 DIGITAL GUARDIANS: TACTICAL CYBERDEFENSE (CLI EDITION)"
        welcome = "Welcome, Cadet. Defend the Living Truth Data Node with the Squad."
        squad_intro = "Available Defense Squad:"
        agents = [
            ("1", "AndreTaker (AnZaCa)", "Strategy, Psychology & Defense Command"),
            ("2", "Tycho (Silicon)", "Metrology, SHA-256 Hashes & Cosmic Lens"),
            ("3", "Baba Yaga Core", "Binary Decompiler & Anti-Palantir Shield"),
            ("4", "Arturius (11yo)", "Link Hunter & Hardware Bridge"),
            ("5", "Michael", "Tactical Coordinator & Legal Custody Firewall"),
            ("6", "Kepler", "Orbital Harmonizer & Timeline Synthesizer"),
            ("7", "Tobias & Bianca", "Perimeter RF & Bluetooth Sniffer Dogs")
        ]
        rounds_info = "\n⚡ SIMULATION 1: Incoming Deauth & Phishing Waves detected!"
        q1 = "An unknown email arrives offering $80/hr job with an external link. What do you do?"
        opts1 = [
            "[A] Click immediately to apply.",
            "[B] Deploy Arturius & AndreTaker: inspect URL headers, verify domain, flag as scam.",
            "[C] Forward it to your friends."
        ]
        win1 = "✅ SUCCESS! Arturius reflects the trap. Escudo Anti-Engaño activated! (+100 XP)"
        fail1 = "❌ WARNING! Never click unknown links. That was a phishing trap."

        round2_info = "\n⚡ SIMULATION 2: Surveillance Antennas detected nearby!"
        q2 = "You must transfer a confidential evidence file without anyone snooping the air. What do you use?"
        opts2 = [
            "[A] Broadcast it over public coffee-shop Wi-Fi (The Sprinkler).",
            "[B] Use a direct shielded copper Ethernet cable (The Clean Pipe).",
            "[C] Send it by open Bluetooth."
        ]
        win2 = "✅ SUCCESS! Michael and Tycho secure the physical copper line. Zero RF Leakage! (+150 XP)"
        fail2 = "❌ CAUTION! Wi-Fi radiates in 360 degrees like a sprinkler. Always prefer the shielded copper pipe."
    else:
        title = "🎮 GUARDIANES DIGITALES: CIBERDEFENSA TÁCTICA (EDICIÓN CLI)"
        welcome = "Bienvenido, Cadete. Defiende el Nodo de la Verdad junto al Escuadrón."
        squad_intro = "Escuadrón Defensor Disponible:"
        agents = [
            ("1", "AndreTaker (AnZaCa)", "Estrategia, Psicología I-O y Resistencia"),
            ("2", "Tycho (Silicio)", "Metrología, Hashes SHA-256 y Lente Cósmico"),
            ("3", "Baba Yaga Core", "Bisturí Forense y Protocolo Anti-Palantir"),
            ("4", "Arturius (11 años)", "Cazador de Enlaces y Puente de Red"),
            ("5", "Michael", "Coordinador Táctico y Guardián Legal"),
            ("6", "Kepler", "Armonizador Orbital y Cronología de Expedientes"),
            ("7", "Tobias y Bianca", "Centinelas Perimetrales y Radar Bluetooth")
        ]
        rounds_info = "\n⚡ SIMULACIÓN 1: ¡Detectada oleada de Ingeniería Social y Phishing!"
        q1 = "Llega un mensaje sospechoso prometiendo $80 USD/hora en un enlace externo. ¿Qué haces?"
        opts1 = [
            "[A] Hacer clic de inmediato para postularte.",
            "[B] Desplegar a Arturius y AndreTaker: auditar cabeceras, verificar dominio y reportar.",
            "[C] Reenviarlo a tus compañeros."
        ]
        win1 = "✅ ¡ÉXITO! Arturius refleja la trampa. ¡Escudo Anti-Engaño activado! (+100 XP)"
        fail1 = "❌ ¡CUIDADO! Nunca abras enlaces sospechosos. Era un anzuelo de ingeniería social."

        round2_info = "\n⚡ SIMULACIÓN 2: ¡Detectadas antenas de vigilancia en el perímetro exterior!"
        q2 = "Debes mover un expediente confidencial sin que nadie lo intercepte en el aire. ¿Qué usas?"
        opts2 = [
            "[A] Transmitirlo por Wi-Fi público abierto (El Aspersor del Jardín).",
            "[B] Conectar un cable de red de cobre blindado directo (La Tubería Sellada).",
            "[C] Enviarlo por Bluetooth sin clave."
        ]
        win2 = "✅ ¡ÉXITO! Michael y Tycho sellan el cable de cobre. ¡Cero emisión electromagnética! (+150 XP)"
        fail2 = "❌ ¡ALERTA! El Wi-Fi dispersa ondas en 360° como un aspersor. Usa siempre la tubería de cobre sellada."

    print("\n" + "=" * 72)
    print(f"   {title}")
    print("=" * 72)
    print(f"\n{welcome}\n")
    print(f"📋 {squad_intro}")
    for num, name, role in agents:
        print(f"   [{num}] {name} ➔ {role}")
    
    # Ronda 1
    print("\n" + "-" * 72)
    print(rounds_info)
    print(f"❓ {q1}\n")
    for o in opts1:
        print(f"   {o}")
    
    try:
        ans = input("\n👉 Tu respuesta / Your answer [A/B/C]: ").strip().upper()
    except (KeyboardInterrupt, EOFError):
        ans = "B"
    
    print("\n" + "-" * 72)
    if ans == "B":
        print(win1)
        print("🛡️ [DEFENSE]: Red protegida, cero fugas y perímetro sellado.")
    else:
        print(fail1)
        print("💡 Consejo pedagógico: Usa siempre verificación en frío antes de interactuar.")
    
    # Ronda 2
    print("\n" + "-" * 72)
    print(round2_info)
    print(f"❓ {q2}\n")
    for o in opts2:
        print(f"   {o}")
    
    try:
        ans2 = input("\n👉 Tu respuesta / Your answer [A/B/C]: ").strip().upper()
    except (KeyboardInterrupt, EOFError):
        ans2 = "B"
    
    print("\n" + "-" * 72)
    if ans2 == "B":
        print(win2)
        print("🔒 [HARDWARE]: Cobre confinado, electrones protegidos.")
    else:
        print(fail2)
        print("💡 Consejo pedagógico: Recuerda la analogía del agua y las tuberías.")
    
    print("=" * 72)
    print("🌟 ¡Gracias por entrenar con los Guardianes Digitales! Nivel 1 completado con honor.\n")

if __name__ == "__main__":
    run_game()
