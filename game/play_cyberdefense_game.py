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
            ("5", "Tobias & Bianca", "Perimeter RF & Bluetooth Sniffer Dogs")
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
    else:
        title = "🎮 GUARDIANES DIGITALES: CIBERDEFENSA TÁCTICA (EDICIÓN CLI)"
        welcome = "Bienvenido, Cadete. Defiende el Nodo de la Verdad junto al Escuadrón."
        squad_intro = "Escuadrón Defensor Disponible:"
        agents = [
            ("1", "AndreTaker (AnZaCa)", "Estrategia, Psicología I-O y Resistencia"),
            ("2", "Tycho (Silicio)", "Metrología, Hashes SHA-256 y Lente Cósmico"),
            ("3", "Baba Yaga Core", "Bisturí Forense y Protocolo Anti-Palantir"),
            ("4", "Arturius (11 años)", "Cazador de Enlaces y Puente de Red"),
            ("5", "Tobias y Bianca", "Centinelas Perimetrales y Radar Bluetooth")
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

    print("\n" + "=" * 72)
    print(f"   {title}")
    print("=" * 72)
    print(f"\n{welcome}\n")
    print(f"📋 {squad_intro}")
    for num, name, role in agents:
        print(f"   [{num}] {name} ➔ {role}")
    
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
    
    print("=" * 72)
    print("🌟 ¡Gracias por entrenar con los Guardianes Digitales! Fin del turno de práctica.\n")

if __name__ == "__main__":
    run_game()
