from flask import jsonify


# def resp_successfully(msg, item):
#     """
#     Response 201: for Created successfully!
#     Response 200: for Updated successfully!
#     Response 202: for Deleted successfully!
#     """
#     messages = [
#         {'message': f'{msg} created successfully!', 'status': 201},
#         {'message': f'{msg} updated successfully!', 'status': 200},
#         {'message': f'{msg} deleted successfully!', 'status': 202}
#     ]
#     response = jsonify(
#         {'message': messages[item]['message']}
#     )
#     response.status_code = messages[item]['status']
#     return response


def resp_content_successfully(content):
    """Response 200"""
    response = jsonify(content)
    response.status_code = 200
    return response


def resp_empty_data_base():
    """Response 200"""
    response = jsonify({
        'message': 'Data base empty!'
    })
    response.status_code = 200
    return response


def resp_create_successfully():
    """Response 201"""
    response = jsonify({
        'message': 'Beer created successfully!'
    })
    response.status_code = 201
    return response


def resp_update_successfully():
    """Response 200"""
    response = jsonify({
        'message': 'Beer updated successfully!'
    })
    response.status_code = 200
    return response


def resp_delete_successfully():
    """Response 202"""
    response = jsonify({
        'message': 'Beer deleted successfully!'
    })
    response.status_code = 202
    return response


def resp_ingredients_create_successfully():
    """Response 201"""
    response = jsonify({
        'message': 'Ingredient added successfully!'
    })
    response.status_code = 201
    return response


def resp_ingredient_delete_successfully():
    """Response 202"""
    response = jsonify({
        'message': 'Ingredient deleted successfully!'
    })
    response.status_code = 202
    return response
