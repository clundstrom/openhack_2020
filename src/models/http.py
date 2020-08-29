def status_code(code=None):
    codes = {
        200: "OK",
        201: "Created",
        400: "Bad Request",
        401: "Unauthorized",
        403: "Forbidden",
        404: "Not found",
        500: "Internal Server Error",
    }
    return {"message": codes.get(code, "Internal Server Error")}


def status_custom(custom):
    return {"message": custom}
