def query_param_value_to_split(key: str, params: dict):
    value: str | None = params.get(key, None)

    if value is not None:
        return [int(n.strip()) for n in value.split(",")]

    return []
