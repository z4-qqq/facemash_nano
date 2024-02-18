from models.tournament_model import Tournament


def create_tournament(images: list[str]) -> Tournament:
    """
    Creates tournament from images
    Args:
        images: list of images
    Returns:
        Tournament
    """
    return Tournament(images=images)

