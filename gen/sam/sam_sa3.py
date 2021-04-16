import random

from dcs.vehicles import AirDefence

from gen.sam.airdefensegroupgenerator import (
    AirDefenseRange,
    AirDefenseGroupGenerator,
)


class SA3Generator(AirDefenseGroupGenerator):
    """
    This generate a SA-3 group
    """

    name = "SA-3/S-125 Site"
    price = 80

    def generate(self):
        self.add_unit(
            AirDefence.SAM_P19_Flat_Face_SR__SA_2_3, "SR", self.position.x, self.position.y, self.heading
        )
        self.add_unit(
            AirDefence.SAM_SA_3_S_125_Low_Blow_TR,
            "TR",
            self.position.x + 20,
            self.position.y,
            self.heading,
        )

        num_launchers = random.randint(3, 6)
        positions = self.get_circular_position(
            num_launchers, launcher_distance=120, coverage=180
        )

        for i, position in enumerate(positions):
            self.add_unit(
                AirDefence.SAM_SA_3_S_125_Goa_LN,
                "LN#" + str(i),
                position[0],
                position[1],
                position[2],
            )

    @classmethod
    def range(cls) -> AirDefenseRange:
        return AirDefenseRange.Medium
