from __future__ import division
from globals import *
from galaxy import Galaxy


def main():
    t = 0
    milky_way = Galaxy(
        num_stars=NUM_STARS_MILKY_WAY,
        pos=vector(-3, 3, 0) * DIST_SCALE,
        vel=vector(0, 0, 0),
        radius=MAX_ORBITAL_RADIUS,
        thickness=MILKY_WAY_GALAXY_THICKNESS,
        color=color.white
    )
    andromeda = Galaxy(
        num_stars=NUM_STARS_ANDROMEDA,
        pos=vector(3, 0, 0) * DIST_SCALE,
        vel=vector(0, 5, 0),
        radius=MAX_ORBITAL_RADIUS,
        thickness=ANDROMEDA_GALAXY_THICKNESS,
        color=color.cyan
    )

    while 1:
        rate(100)

        for i in range(len(milky_way.stars)):
            star = milky_way.stars[i]
            star.vel += accel(star, andromeda) * dt
            star.vel += accel(star, milky_way) * dt
            star.pos += star.vel * dt

        andromeda_mask = np.zeros(len(andromeda.stars))

        for star in andromeda.stars:
            star.vel += accel(star, milky_way) * dt
            star.vel += accel(star, andromeda) * dt
            star.pos += star.vel * dt

        milky_way.vel += accel(milky_way, andromeda) * dt
        milky_way.pos += milky_way.vel * dt

        andromeda.vel += accel(andromeda, milky_way) * dt
        andromeda.pos += andromeda.vel * dt

        t += dt


if __name__ == '__main__':
    main()
