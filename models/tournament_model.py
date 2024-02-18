import typing


class Tournament:
    """Base class for tournament to compare images.

    Create a simple tournament grid to compare images.
    Winner will meet to another winner

    """
    def __init__(self, images: list[str]) -> None:
        """Create tournament grid by forming pairs.
        Args:
            images: list of images
        Returns:
            None
        """
        self.pairs: list[tuple[str, str]] = self.form_grid(images)
        self.winners: list[str] = []

    def get_round(self) -> typing.Optional[tuple[str, str]]:
        """Extracts two candidates for comparing
        Args:
            None
        Returns:
            candidate1, candidate2
        """
        if self.pairs:
            return self.pairs[0]
        return None

    def update_winners(self, winner: str) -> None:
        """Update winners list, remove pair from list of pairs
        Args:
            winner: current winner
        Returns:
            None

        """
        self.winners.append(winner)
        self.pairs.pop(0)

    def update_pairs(self) -> None:
        """Update pairs list after all matches were played.
        Forms list of pairs from list of winners.

        Args:
            None
        Returns:
            None
        """
        self.pairs = self.form_grid(images=self.winners)
        self.winners = []

    @staticmethod
    def form_grid(images: list[str]) -> list[tuple[str, str]]:
        """Form grid of pairs for tournament
        Args:
            images: list of images
        Returns:
            list of pairs
        Example:
            form_grid(['image1', 'image2', 'image3', 'image4']) -> [('image1', 'image2'), ('image3', 'image4')]

        """
        return [(images[i], images[i + 1]) for i in range(0, len(images) - 1, 2)]


