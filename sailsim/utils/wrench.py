"""A 2d force vector combined with a 1d torque vector."""

from numpy import array, cross, float64, ndarray, append
from numpy.linalg import norm


class Wrench(ndarray):
    """A 2D force vector combined with a 1D torque vector."""

    def __new__(cls, vector: ndarray) -> "Wrench":
        """
        Create a new Wrench.

        Args:
            vector: 3D vector of the wrench
        """
        return vector.view(cls)

    @property
    def force(self) -> float64:
        """Return the scalar force from the wrench."""
        return norm(self[:2])

    @property
    def forceX(self) -> float64:
        """
        Return the X force component from the wrench.

        If this method gets called multiple times it can be replaced with `wrench[0]` which is much more performant.
        """
        return self[0]

    @property
    def forceY(self) -> float64:
        """
        Return the Y force component from the wrench.

        If this method gets called multiple times it can be replaced with `wrench[1]` which is much more performant.
        """
        return self[1]

    @property
    def torque(self) -> float64:
        """
        Return the torque from the wrench.

        If this method gets called multiple times it can be replaced with `wrench[2]` which is much more performant.
        """
        return self[2]

    @staticmethod
    def fromForceAndLever(force: ndarray, lever: ndarray) -> "Wrench":
        """Create a Wrench based of two ndarray."""
        return Wrench(append(force, cross(lever, force)))

    @staticmethod
    def fromForceAndTorque(force: ndarray, torque: float = 0) -> "Wrench":
        """Create a Wrench based of a force."""
        return Wrench(append(force, torque))


if __name__ == "__main__":
    w = Wrench(array([3.0, 4.0, 5.0]))
    print(w)
    print(w.force)
    print(w.torque)
