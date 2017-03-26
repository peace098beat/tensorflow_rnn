# -*- coding:utf-8 -*-


import csv
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def f1(t, x, y, z):
    return 10. * (y - x)


def f2(t, x, y, z):
    return (28. * x) - y - (x * z)


def f3(t, x, y, z):
    return (-8. / 3.) * z + (x * y)


class Lorenz:
    """
    runge kutta

    http://www.geocities.jp/supermisosan/rksimultaneousequation.html


    :Equation:
    dxdt = 10*(y-x)             --- (1)
    dydt = 28*x - y - x*z       --- (2)
    dzdt = -(8./3.)*z + x*y     --- (3)

    """
    @staticmethod
    def createLorenz(filename="lorenz.csv", dt=0.001, max_count=5000, t0=0, x0=1.0, y0=0, z0=0):
        # time step
        dt = dt
        tmax = dt * max_count
        # initial condition
        t = t0
        x = x0
        y = y0
        z = z0

        k0 = [0, 0, 0]
        k1 = [0, 0, 0]
        k2 = [0, 0, 0]
        k3 = [0, 0, 0]

        Lorenz.writeCsv(filename, ["t", "x", "y", "z"], header=True)

        while t < tmax:

            k0[0] = dt * f1(t, x, y, z)
            k0[1] = dt * f2(t, x, y, z)
            k0[2] = dt * f3(t, x, y, z)

            k1[0] = dt * f1(t + dt / 2.0, x + k0[0] / 2.0,
                            y + k0[1] / 2.0, z + k0[2] / 2.0)
            k1[1] = dt * f2(t + dt / 2.0, x + k0[0] / 2.0,
                            y + k0[1] / 2.0, z + k0[2] / 2.0)
            k1[2] = dt * f3(t + dt / 2.0, x + k0[0] / 2.0,
                            y + k0[1] / 2.0, z + k0[2] / 2.0)

            k2[0] = dt * f1(t + dt / 2.0, x + k1[0] / 2.0,
                            y + k1[1] / 2.0, z + k1[2] / 2.0)
            k2[1] = dt * f2(t + dt / 2.0, x + k1[0] / 2.0,
                            y + k1[1] / 2.0, z + k1[2] / 2.0)
            k2[2] = dt * f3(t + dt / 2.0, x + k1[0] / 2.0,
                            y + k1[1] / 2.0, z + k1[2] / 2.0)

            k3[0] = dt * f1(t + dt, x + k2[0], y + k2[1], z + k2[2])
            k3[1] = dt * f2(t + dt, x + k2[0], y + k2[1], z + k2[2])
            k3[2] = dt * f3(t + dt, x + k2[0], y + k2[1], z + k2[2])

            dx = (k0[0] + 2.0 * k1[0] + 2.0 * k2[0] + k3[0]) / 6.0
            dy = (k0[1] + 2.0 * k1[1] + 2.0 * k2[1] + k3[1]) / 6.0
            dz = (k0[2] + 2.0 * k1[2] + 2.0 * k2[2] + k3[2]) / 6.0

            x = x + dx
            y = y + dy
            z = z + dz

            Lorenz.writeCsv(filename, [t, x, y, z])
            # print(t,x,y,z, k0,k1,k2,k3)
            t = t + dt

    @staticmethod
    def writeCsv(filename, line, header=False):
        # Header
        if header:
            with open(filename, 'w') as f:
                writer = csv.writer(f, lineterminator='\n')  # 改行コード（\n）を指定しておく
                writer.writerow(line)     # list（1次元配列）の場合
        # Body
        if header == False:
            with open(filename, 'a') as f:
                writer = csv.writer(f, lineterminator='\n')  # 改行コード（\n）を指定しておく
                writer.writerow(line)     # list（1次元配列）の場合

    @staticmethod
    def readCsv(filename):
        data = np.loadtxt(filename, delimiter=",", skiprows=1)
        return data

    @staticmethod
    def post(filename, do_plot=True):

        data = Lorenz.readCsv(filename)

        ts = data[:, 0]
        xs = data[:, 1]
        ys = data[:, 2]
        zs = data[:, 3]

        fig = plt.figure()
        ax = fig.gca(projection='3d')

        ax.plot(xs, ys, zs)
        ax.set_xlabel("X Axis")
        ax.set_ylabel("Y Axis")
        ax.set_zlabel("Z Axis")
        ax.set_title("Lorenz Attractor")

        plt.savefig(filename + ".png")

        if do_plot:
            plt.show()

        plt.close()

        del data, ts, xs, ys, zs
        del fig, ax


# ******************************************************
# UnitTEst
# ******************************************************
import unittest


class LorenzTest(unittest.TestCase):

    def setUp(self):
        self.filename = "lorenz_test.csv"
        pass

    def test_create(self):
        Lorenz.createLorenz(self.filename, dt=0.01,
                            max_count=5000, t0=0, x0=1.0, y0=0, z0=0)

    def test_reader(self):
        Lorenz.readCsv(self.filename)

    def test_post(self):
        Lorenz.post(self.filename, do_plot=True)


if __name__ == '__main__':
    unittest.main()
