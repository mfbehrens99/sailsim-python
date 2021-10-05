# Changelog

<!---
Template

## [x.x.x] - 20xx-xx-xx

### Added

- this
- that

### Changed

- this
- that

### Removed

- this
- that

--->

## [Unreleased]

### Added

- [[Boat]] Add torques to the boat to make it spin
- [[Simulation]] Run simulation for x steps
- [[Sailor]] Basic rudder steering
- [[GUI]] Display rudder forces in [boatInspector]

### Changed

- [[Boat]] Move forces and torques to their own files
- [[Boat]] Rename waterDrag and waterLift to centerboardDrag and centerboardLift
- [[Sailor]] Don't delete Waypoints after executing them

### Removed

- [[Boat]] Removed Boat::getSpeedSq()



## [0.0.1] - 2021-04-13

### Added

- [[Simulation]] Basic simulation features
- [[World]] Basic functions for World
- [[Boat]] Basic boat behavior
- [[Sailor]] can reach waypoints into all directions
- [[Wind]] Basic wind system
- [[GUI]] Basic GUI for displaying a simulation



<!--- Versions --->
[Unreleased]: https://github.com/mfbehrens99/sailsim/compare/v0.0.1...HEAD
[0.0.2]: https://github.com/mfbehrens99/sailsim/compare/v0.0.1...v0.0.2
[0.0.1]: https://github.com/mfbehrens99/sailsim/releases/tag/v0.0.1

<!--- Parts --->
[Simulation]: https://github.com/mfbehrens99/sailsim/blob/main/sailsim/simulation/Simulation.py
[World]: https://github.com/mfbehrens99/sailsim/blob/main/sailsim/world/World.py
[Boat]:https://github.com/mfbehrens99/sailsim/blob/main/sailsim/boat/Boat.py
[Sailor]: https://github.com/mfbehrens99/sailsim/blob/main/sailsim/sailor/Sailor.py
[Wind]: https://github.com/mfbehrens99/sailsim/blob/main/sailsim/wind/Wind.py
[GUI]: https://github.com/mfbehrens99/sailsim/tree/main/sailsim/gui
[mapView]: https://github.com/mfbehrens99/sailsim/blob/main/sailsim/gui/mapView.py
[boatInspector]: https://github.com/mfbehrens99/sailsim/blob/main/sailsim/gui/boatInspector.py
[utils]: https://github.com/mfbehrens99/sailsim/tree/main/sailsim/utils
