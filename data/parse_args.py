import argparse


def get_argparser() -> argparse.ArgumentParser:
    """
    Handle arguments
    Args:
        None
    Returns:
        ArgumentParser

    """
    parser = argparse.ArgumentParser(
        prog="FacemashNano",
        description="Nano version of facemash"
    )
    parser.add_argument("--data-format", type=str, default="*")

    return parser
