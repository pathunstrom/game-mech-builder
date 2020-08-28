"""
A turn based mecha based RPG
"""
import ppb


class MechBuilder(ppb.BaseScene):
    def __init__(self, **props):
        super().__init__(**props)

        self.add(ppb.Sprite(
            image=ppb.Image('mechbuilder/resources/mechbuilder.png'),
        ))


def main():
    ppb.run(
        starting_scene=MechBuilder,
        title='Mech Builder',
    )
