from __future__ import division
from globals import *
from galaxy import Galaxy


def main():

    t = 0
    milky_way = Galaxy(
        num_stars=NUM_STARS_MILKY_WAY,
        pos=vector(-5, 0, 0) * DIST_SCALE,
        vel=vector(0, 0, 0),
        radius=MAX_ORBITAL_RADIUS,
        thickness=MILKY_WAY_GALAXY_THICKNESS,
        color=vector(0.9, 0.9, 1)
    )
    andromeda = Galaxy(
        num_stars=NUM_STARS_ANDROMEDA,
        pos=vector(3, 0, 0) * DIST_SCALE,
        vel=vector(0, 3, 0),
        radius=MAX_ORBITAL_RADIUS,
        thickness=ANDROMEDA_GALAXY_THICKNESS,
        color=vector(0, 0.5, 1)
    )

    while True:
        rate(100)

        mag_difference = milky_way.pos.mag - andromeda.pos.mag


        for i in range(len(milky_way.stars)):
            star = milky_way.stars[i]
            star.vel += accel(star, andromeda) * dt
            star.vel += accel(star, milky_way) * dt
            star.pos += star.vel * dt
            # if(mag_difference == -6+18):
            #     star.obj.color = vector(1, 0.5, 0)
            if(andromeda.pos.mag < 1.1920057081525512e+20):
                star.obj.color = vector(1, 0.5, 0)

        andromeda_mask = np.zeros(len(andromeda.stars))

        for star in andromeda.stars:
            star.vel += accel(star, milky_way) * dt
            star.vel += accel(star, andromeda) * dt
            star.pos += star.vel * dt
            # if(mag_difference < -6+18 and mag_difference > -5e+18):
            #     star.obj.color = vector(1, 0.5, 0)
            if(andromeda.pos.mag < 1.1920057081525512e+20):
                star.obj.color = vector(1, 0.5, 0)

        milky_way.vel += accel(milky_way, andromeda) * dt
        milky_way.pos += milky_way.vel * dt

        andromeda.vel += accel(andromeda, milky_way) * dt
        andromeda.pos += andromeda.vel * dt

        t += dt


if __name__ == '__main__':
    main()
