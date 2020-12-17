import numpy as np


class HyperCubes:
    def __init__(self, start: np.ndarray):
        self.start = start
        self.cubes = np.array([0])

    def run(self, iterations: int) -> None:
        self._initialise(iterations)
        for _ in range(iterations):
            self.step()

    def step(self):
        new_cubes = self.cubes.copy()
        sw, sz, sy, sx = self.cubes.shape
        w_nz = [i for i in range(sw) if self.cubes[i, :, :, :].sum() > 0]
        z_nz = [i for i in range(sz) if self.cubes[:, i, :, :].sum() > 0]
        y_nz = [i for i in range(sy) if self.cubes[:, :, i, :].sum() > 0]
        x_nz = [i for i in range(sx) if self.cubes[:, :, :, i].sum() > 0]
        for w in range(w_nz[0] - 1, w_nz[-1] + 2):
            for z in range(z_nz[0] - 1, z_nz[-1] + 2):
                for y in range(y_nz[0] - 1, y_nz[-1] + 2):
                    for x in range(x_nz[0] - 1, x_nz[-1] + 2):
                        current = new_cubes[w, z, y, x]
                        n = self.neighbours(x, y, z, w)
                        if current == 1:
                            new_cubes[w, z, y, x] = 1 if 2 <= n <= 3 else 0
                        else:
                            new_cubes[w, z, y, x] = 1 if n == 3 else 0
        self.cubes = new_cubes

    def neighbours(self, x: int, y: int, z: int, w: int) -> int:
        sw, sz, sy, sx = self.cubes.shape

        min_x, max_x = max(x - 1, 0), min(x + 1, sx) + 1
        min_y, max_y = max(y - 1, 0), min(y + 1, sy) + 1
        min_z, max_z = max(z - 1, 0), min(z + 1, sz) + 1
        min_w, max_w = max(w - 1, 0), min(w + 1, sw) + 1

        sub = self.cubes[min_w:max_w, min_z:max_z, min_y:max_y, min_x:max_x]
        return sub.sum() - self.cubes[w, z, y, x]

    def _initialise(self, iterations: int):
        sy, sx = self.start.shape
        di = 2 * iterations
        shape = (1 + di, 1 + di, sy + di, sx + di)
        self.cubes = np.zeros(shape, dtype=np.int)
        w, z = iterations, iterations
        for x in range(sx):
            ix = iterations + x
            for y in range(sy):
                iy = iterations + y
                value = self.start[y, x]
                self.cubes[w, z, iy, ix] = value

    @property
    def active(self):
        return self.cubes.sum()


class Cubes:
    def __init__(self, start: np.ndarray):
        self.start = start
        self.cubes = np.array([0])

    def run(self, iterations: int) -> None:
        self._initialise(iterations)
        for _ in range(iterations):
            self.step()

    def step(self):
        new_cubes = self.cubes.copy()
        sz, sy, sx = self.cubes.shape
        z_nz = [i for i in range(sz) if self.cubes[i, :, :].sum() > 0]
        y_nz = [i for i in range(sy) if self.cubes[:, i, :].sum() > 0]
        x_nz = [i for i in range(sx) if self.cubes[:, :, i].sum() > 0]
        for z in range(z_nz[0] - 1, z_nz[-1] + 2):
            for y in range(y_nz[0] - 1, y_nz[-1] + 2):
                for x in range(x_nz[0] - 1, x_nz[-1] + 2):
                    current = new_cubes[z, y, x]
                    n = self.neighbours(x, y, z)
                    if current == 1:
                        new_cubes[z, y, x] = 1 if 2 <= n <= 3 else 0
                    else:
                        new_cubes[z, y, x] = 1 if n == 3 else 0
        self.cubes = new_cubes

    def neighbours(self, x: int, y: int, z: int) -> int:
        sz, sy, sx = self.cubes.shape

        min_x, max_x = max(x - 1, 0), min(x + 1, sx) + 1
        min_y, max_y = max(y - 1, 0), min(y + 1, sy) + 1
        min_z, max_z = max(z - 1, 0), min(z + 1, sz) + 1

        sub = self.cubes[min_z:max_z, min_y:max_y, min_x:max_x]
        return sub.sum() - self.cubes[z, y, x]

    def _initialise(self, iterations: int):
        sy, sx = self.start.shape
        di = 2 * iterations
        shape = (1 + di, sy + di, sx + di)
        self.cubes = np.zeros(shape, dtype=np.int)
        z = iterations
        for x in range(sx):
            ix = iterations + x
            for y in range(sy):
                iy = iterations + y
                value = self.start[y, x]
                self.cubes[z, iy, ix] = value

    @property
    def active(self):
        return self.cubes.sum()


def part_1(cubes: Cubes) -> int:
    cubes.run(6)
    return cubes.active


def part_2(cubes: Cubes) -> int:
    hypercubes = HyperCubes(cubes.start)
    hypercubes.run(6)
    return hypercubes.active


def parse(filename: str) -> Cubes:
    chars = {'#': 1, '.': 0}
    with open(filename, 'r') as f:
        return Cubes(np.array([[chars[c] for c in line.strip() if c in chars] for line in f]))


if __name__ == '__main__':
    cubes = parse('day_17/input.txt')
    print(f'Active cubes after 6 steps: {part_1(cubes)}')
    print(f'Active hypercubes after 6 steps: {part_2(cubes)}')
