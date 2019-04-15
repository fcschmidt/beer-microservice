from flask import jsonify


def resp_successfully(content):
    """Response 200"""
    response = jsonify(content)
    response.status_code = 200
    return response


def resp_not_items():
    """Response 200"""
    response = jsonify({
        'message': 'Data base empty!'
    })
    response.status_code = 200
    return response


def resp_create_successfully():
    """Response 201"""
    response = jsonify({
        'message': 'Beer create successfully!'
    })
    response.status_code = 201
    return response


def resp_update_successfully():
    """Response 200"""
    response = jsonify({
        'message': 'Beer update successfully!'
    })
    response.status_code = 200
    return response


def resp_delete_successfully():
    """Response 202"""
    response = jsonify({
        'message': 'Beer delete successfully!'
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
        'message': 'Ingredient delete successfully!'
    })
    response.status_code = 202
    return response
