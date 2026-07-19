
import sender_stand_request
import data

# Esta función clona el cuerpo base y le cambia el nombre para probar diferentes escenarios
def get_user_body(first_name):
    current_body = data.user_body.copy()
    current_body["firstName"] = first_name
    return current_body


def test_create_user_2_letter_in_first_name_get_success_response():
    user_body = get_user_body("Aa")
    user_response = sender_stand_request.post_new_user(user_body)

    # 1. Comprobaciones que ya tenías
    assert user_response.status_code == 201
    assert user_response.json()["authToken"] != ""

    # 2. NUEVO: Traer la tabla de la base de datos
    users_table_response = sender_stand_request.get_users_table()

    # 3. NUEVO: Formatear el string exacto que se guardó en la fila (recuerda que el \ une líneas en Python)
    str_user = user_body["firstName"] + "," + user_body["phone"] + "," \
               + user_body["address"] + ",,," + user_response.json()["authToken"]

    # 4. NUEVO: Comprobar que el usuario aparezca exactamente 1 vez (ni 0, ni duplicado)
    assert users_table_response.text.count(str_user) == 1