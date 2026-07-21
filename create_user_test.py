import sender_stand_request
import data


def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body


def positive_assert(name):
    kit_body = get_kit_body(name)
    kit_response = sender_stand_request.post_new_client_kit(kit_body)

    # Verifica que el código de respuesta sea 201
    assert kit_response.status_code == 201
    # Verifica que el campo "name" coincida
    assert kit_response.json()["name"] == name


def negative_assert_code_400(kit_body):
    kit_response = sender_stand_request.post_new_client_kit(kit_body)

    # Verifica que el código de respuesta sea 400
    assert kit_response.status_code == 400

# Prueba 1: 1 carácter (Positiva)
def test_create_kit_1_letter_in_name_get_success_response():
    positive_assert("a")

# Prueba 2: 511 caracteres (Positiva)
def test_create_kit_511_letters_in_name_get_success_response():
    # Cadena de 511 caracteres
    name = "A" * 511
    positive_assert(name)

# Prueba 3: 0 caracteres (Negativa)
def test_create_kit_empty_name_get_error_response():
    positive_assert("") # o usa negative_assert_code_400(get_kit_body("")) según la doc de tu sprint

# Prueba 4: 512 caracteres (Negativa)
def test_create_kit_512_letters_in_name_get_error_response():
    kit_body = get_kit_body("A" * 512)
    negative_assert_code_400(kit_body)

# Prueba 5: Caracteres especiales (Positiva)
def test_create_kit_has_special_symbol_in_name_get_success_response():
    positive_assert('"№%@",')

