import pyautogui
import pytesseract
import cv2
import numpy as np
import time
import keyboard
import re

from regions import REGIONES

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# =========================
# FUNCIONES
# =========================

def obtener_pos_click(region, click_pos):
    x, y, w, h = region
    if click_pos == "center":
        return x + w // 2, y + h // 2
    if isinstance(click_pos, tuple):
        return click_pos
    return None


def puede_procesar_region(nombre, texto, ultimo_texto, repetir):
    if repetir:
        return True
    return texto != ultimo_texto.get(nombre)


# =========================
# VARIABLES
# =========================

ultimo_texto = {}

# Estado persistente Saque de Centro
saque_estado_activo = False
saque_detectado_en = None
saque_click_hecho = False
saque_tecla_hecha = False

print("BOT OCR INICIADO")
print("Presiona ESC para salir")
time.sleep(1)

# =========================
# LOOP PRINCIPAL
# =========================

while True:
    if keyboard.is_pressed("esc"):
        print("Saliendo...")
        break

    for r in REGIONES:
        x, y, w, h = r["region"]

        screenshot = pyautogui.screenshot(region=(x, y, w, h))
        frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        gray = cv2.GaussianBlur(gray, (5, 5), 0)
        gray = cv2.threshold(gray, 160, 255, cv2.THRESH_BINARY)[1]

        texto = pytesseract.image_to_string(
            gray,
            config=f"--psm {r.get('psm',7)}",
            lang=r.get("lang", "eng")
        )

        texto = texto.upper()
        texto = re.sub(r"[^A-Z0-9 ]", " ", texto)
        texto = re.sub(r"\s+", " ", texto).strip()

        cv2.imshow(r["nombre"], gray)
        cv2.waitKey(1)
        #print(f"[DEBUG] Region: {r['nombre']} | Texto detectado: '{texto}'")
        
        # =========================
        # SAQUE DE CENTRO / REANUDAR
        # =========================
        if r["nombre"] == "Saque de Centro":
            ahora = time.time()

            detecta_saque = ("SAQUE" in texto) or ("CENTRO" in texto)
            detecta_reanudar = "REANUDAR" in texto

            # ---- REANUDAR: solo click, sin estado ----
            if detecta_reanudar:
                pos = obtener_pos_click(r["region"], r.get("click_pos", "center"))
                if pos:
                    print(">>> CLICK REANUDAR")
                    pyautogui.click(
                        x=pos[0],
                        y=pos[1],
                        button=r.get("click_tipo", "left")
                    )
                continue

            # ---- SAQUE DE CENTRO: logica con estado ----
            if detecta_saque and not saque_estado_activo:
                print(">>> SAQUE DE CENTRO DETECTADO")
                saque_estado_activo = True
                saque_detectado_en = ahora

            if saque_estado_activo:
                # CLICK inmediato (una sola vez)
                if not saque_click_hecho:
                    pos = obtener_pos_click(r["region"], r.get("click_pos", "center"))
                    if pos:
                        print(">>> CLICK SAQUE DE CENTRO")
                        pyautogui.click(
                            x=pos[0],
                            y=pos[1],
                            button=r.get("click_tipo", "left")
                        )
                    saque_click_hecho = True

                # TECLA despues de 1 segundo
                if not saque_tecla_hecha and saque_detectado_en:
                    if ahora - saque_detectado_en >= 1:
                        print(">>> TECLA U (SAQUE DE CENTRO)")
                        pyautogui.press("u")
                        saque_tecla_hecha = True

                # Reset completo
                if saque_click_hecho and saque_tecla_hecha:
                    saque_estado_activo = False
                    saque_detectado_en = None
                    saque_click_hecho = False
                    saque_tecla_hecha = False

            continue

        # =========================
        # LOGICA NORMAL
        # =========================

        repetir = r.get("repetir_texto", False)

        if not puede_procesar_region(r["nombre"], texto, ultimo_texto, repetir):
            continue

        ultimo_texto[r["nombre"]] = texto

        coincidencias = sum(1 for p in r["palabras"] if p in texto)
        min_match = r.get("min_match", 1)

        if coincidencias >= min_match:
            print(f">>> ACCION DETECTADA: {r['nombre']}")

            if r.get("click"):
                pos = obtener_pos_click(r["region"], r.get("click_pos", "center"))
                if pos:
                    pyautogui.click(
                        x=pos[0],
                        y=pos[1],
                        button=r.get("click_tipo", "left")
                    )

            if r.get("tecla"):
                time.sleep(r.get("click_delay", 0))
                pyautogui.press(r["tecla"])


    time.sleep(0.1)


cv2.destroyAllWindows()
