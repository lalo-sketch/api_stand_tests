
import configuration
import requests
import data

def post_new_user(body):
    # Realiza la petición POST para crear usuario
    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
        json=body,
        headers=data.headers
    )

def get_user_token():
    response = post_new_user(data.user_body)
    # --- AGREGA ESTOS DOS PRINTS ---
    print("\n[DEBUG] Status Code:", response.status_code)
    print("[DEBUG] Response Body:", response.text)
    # --------------------------------
    return response.json()["authToken"]


def post_new_client_kit(kit_body):
    # 2. Obtener el token activo llamando a la función de arriba
    auth_token = get_user_token()

    # 3. Copiar los encabezados y agregar el token de autorización
    current_headers = data.headers.copy()
    current_headers["Authorization"] = f"Bearer {auth_token}"

    # 4. Enviar la petición POST para crear el kit
    return requests.post(
        configuration.URL_SERVICE + "/api/v1/kits",
        json=kit_body,
        headers=current_headers
    )