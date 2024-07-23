def calculate_buoyancy(v, density_fluid):
    return 9.81 * v * density_fluid


def will_it_float(v, mass):
    return not (mass / v) > 1000


def calculate_pressure(depth):
    return depth * 9.81 * 1000


def calculate_acceleration(F, m):
    return F / m


def calculate_angular_acceleration(tau, I):
    return tau / I


def calculate_moment_of_intertia(m, r):
    return m * r ^ 2


def calculate_auv_acceleration(
    F_magnitude, F_angle, mass=100, volume=0.1, thruster_distance=0.5
):
    return F_magnitude / mass


import numpy as np
import math


def calculate_auv_angular_accelertion(
    F_magnitude, F_angle, inertia=1, thruster_distance=0.5
):
    return (F_magnitude * np.sin(F_angle) * thruster_distance) / inertia


def calculate_auv2_acceleration(T, alpha, theta, mass=100):
    adjustedX = []
    adjustedY = []
    for i in range(len(T)):
        adjustedX.append(T[i] * math.cos(alpha + theta))
        adjustedY.append(T[i] * math.sin(alpha + theta))

    xAccel = adjustedX[2] + adjustedX[3] - adjustedX[0] - adjustedX[1]
    yAccel = adjustedY[0] - adjustedY[1] - adjustedY[2] + adjustedY[3]
    return math.sqrt(xAccel**2 + yAccel**2) / mass


def calculate_auv2_angular_acceleration(T, alpha, L, l, inertia=100):
    netDist = math.sqrt(L**2 + l**2)

    adjustedX = []
    adjustedY = []
    for i in range(len(T)):
        adjustedX.append(T[i] * math.cos(alpha) * netDist)
        adjustedY.append(T[i] * math.sin(alpha) * netDist)

    xAccel = adjustedX[0] + adjustedX[2] - adjustedX[3] - adjustedX[1]
    yAccel = adjustedY[3] + adjustedY[0] - adjustedY[1] - adjustedY[2]
    return math.sqrt(xAccel**2 + yAccel**2) / inertia


import time


def simulate_auv2_motion(
    T, alpha, L, l, mass=100, inertia=100, dt=0.1, t_final=10, x0=0, y0=0, theta0=0
):
    t = [0]
    x = [0]
    y = [0]
    theta = [0]
    v = [0]
    omega = [0]
    a = [0]
    for i in range(0, t_final):
        t.append(i)

        a.append(calculate_auv2_acceleration(T, alpha, theta[i]))
        v.append(calculate_auv2_acceleration(T, alpha, theta[i]) * t[i] + v[i])

        # using x = vt + 1/2 a * t^2, then times trig func theta to get x component
        x.append(
            math.cos(theta[i])
            * (
                x[i]
                + v[i] * t[i]
                + 0.5 * (calculate_auv2_acceleration(T, alpha, theta[i])) * t[i] * t[i]
            )
        )
        y.append(
            math.sin(theta[i])
            * (
                x[i]
                + v[i] * t[i]
                + 0.5 * (calculate_auv2_acceleration(T, alpha, theta[i])) * t[i] * t[i]
            )
        )

        omega.append(
            calculate_auv2_angular_acceleration(T, alpha, L, l) * t[i] + omega[i]
        )

        theta.append(
            theta[i]
            + omega[i] * t[i]
            + 0.5 * calculate_auv2_angular_acceleration(T, alpha, L, l) * t[i] * t[i]
        )
    return "hello"
    # return t, x, y, theta, v, omega, a
