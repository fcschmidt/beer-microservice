from flask_restful import abort


def error_does_not_exist(resource):
    """Response 404 Not Found"""
    if not resource:
        abort(http_status_code=404, error=f"Beer does not exist.")
