from settings import IMAGES_PATH


def _fix_data_format(data_format: str) -> str:
    """Fixes data format if needed.
    Args:
        data_format: raw data format
    Returns:
        fixed data format
    """
    if data_format == "*":
        return data_format
    return f"*.{data_format}"


def collect_images(data_format: str = "*") -> list[str]:
    """Collects all images in local database
    Args:
        data_format: data format
    Returns:
        list with all local images

    """
    data_format = _fix_data_format(data_format=data_format)
    return [p.name for p in IMAGES_PATH.glob(data_format)]
